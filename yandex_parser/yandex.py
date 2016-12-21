# -*- coding:utf-8 -*-
import re
import urllib

from pyquery import PyQuery
import lxml.html
from yandex_parser.exceptions import EmptySerp, YandexParserError
from yandex_parser.utils import to_unicode, get_full_domain_without_scheme
from lxml import etree


class YandexParser(object):
    params_regexr = re.U | re.M | re.DOTALL | re.I

    patterns = {
        'pagecount': re.compile(u'found"\:"&mdash;&nbsp;(.*?)отв', params_regexr),
        'infected': re.compile(u'/search/infected\?url=(.*?)&', params_regexr),
        'captcha': re.compile(u'<img class="image form__captcha".*?src=\"([^\"]+)\"', params_regexr),
    }

    def __init__(self, content, snippet_fileds=('d', 'p', 'u', 't', 's', 'm')):
        self.content = to_unicode(content)
        self.snippet_fileds = snippet_fileds

    def get_context_snippet_title(self, content):
        res = re.search(ur'<h2[^>]*?>\s*<a[^>]*?href="([^"]+?)"[^>]*?>\s*(.*?)\s*</a>', content, re.I | re.M | re.S)
        if not res:
            raise YandexParserError(u'Не удалось распарсить тайтл в сниппете: {0}'.format(content))
        return {'u': res.group(1), 't': YandexParser.strip_tags(res.group(2))}

    def get_context_visible_url(self, content):
        res = re.search(ur'<div\s*class="path\s*organic__path"><a[^>]*?href="[^"]+?"[^>]*?>\s*(.*?)\s*</a>\s*</div>', content, re.I | re.M | re.S)
        if not res:
            return
        return YandexParser.strip_tags(res.group(1))

    def get_context_serp(self):
        snippets = re.findall(
            ur'(<(?:li|div)\s*class="serp-item\s+serp-adv-item".*?</div>\s*</div>\s*</(?:li|div)>)',
            self.content,
            re.I | re.M | re.S
        )
        sn = []
        for snippet in snippets:
            item = self.get_context_snippet_title(snippet)
            item['vu'] = self.get_context_visible_url(snippet)
            sn.append(item)

        return {'pc': len(sn), 'sn': sn}

    def get_serp(self):
        if self.is_not_found():
            return {'pc': 0, 'sn': []}

        if not YandexParser.is_yandex(self.content):
            raise YandexParserError(u'content is not yandex')

        pagecount = self.get_pagecount()
        snippets = self.get_snippets()
        
        if not snippets:
            raise EmptySerp()
        
        return {'pc': pagecount, 'sn': snippets}

    def pagination_exists(self):
        return '<span class="pager__group">' in self.content

    @classmethod
    def is_yandex(cls, content):
        return '<a class="logo__link" href="//www.yandex.' in content or u'<title>Яндекс' in content

    def get_clean_html(self):
        return YandexSerpCleaner.clean(self.content)

    def get_pagecount(self):
        if self.is_not_found():
            return 0

        patterns = (
            self.patterns['pagecount'],
            re.compile(ur'"found":"[^\\]\\n([^"]*?)отв', self.params_regexr),
            re.compile(ur'<div class="serp-adv__found">Наш[^ ]+\s+(.*?)рез', self.params_regexr)
        )

        for pattern in patterns:
            match = pattern.search(self.content)
            if match:
                break

        if not match:
            return

        pagecount_raw = match.group(1)
        pagecount = int(pagecount_raw.split()[0])
        if u'тыс' in pagecount_raw:
            pagecount *= 1000
        elif u'млн' in pagecount_raw:
            pagecount *= 1000000
        return pagecount

    def is_not_found(self):
        return u'По вашему запросу ничего не нашлось' in self.content

    def get_snippets(self):

        try:
            dom = PyQuery(self.content)
            serp = dom('.serp-list').children('.serp-item')

            snippets = []
            position = 0
            for sn in serp:
                if 'serp-adv' in sn.attrib['class'] or 'z-' in sn.attrib['class'] \
                    or 'serp-item_keyboard-shortcuts-ignore_yes' in sn.attrib['class'] \
                    or 'template-object-badge' in sn.attrib['class']\
                    or (
                        'template-composite ' in sn.attrib['class']
                        and 't-construct-adapter__extended-snippet' not in sn.attrib['class']
                        and 't-construct-adapter__free-video' not in sn.attrib['class']
                    ):
                    #реклама
                    continue

                # игнорим "расписание, результаты и трансляции на Яндексе"
                if 't-sport-' in sn.attrib['class']:
                    continue

                # игнорим предложения на маркете
                if 't-market-offers' in sn.attrib['class']:
                    continue

                # игонорим тизеры
                if sn.xpath('.//div[contains(@class,"teaser ")]'):
                    continue

                is_video_snippet = 't-construct-adapter__free-video' in sn.attrib['class']

                # видео сниппет
                if is_video_snippet:
                    h2 = sn.xpath('.//div[contains(@class,"video2 ")]')[0]
                else:
                    h2 = sn.find('.//h2')
                    if not h2:
                        raise YandexParserError(u'parse error')

                    if 'serp-item__title' not in h2.attrib['class'] and 'organic__title-wrapper' not in h2.attrib['class']:
                        raise YandexParserError(u'parse error')

                infected = 'template-infected' in sn.attrib['class']
                if infected:
                    link = h2
                    url = sn.find('.//*[@class="template-infected__unsafe"]').find('a').attrib['href']
                else:
                    link = h2.find('a')
                    url = link.attrib['href']

                #Яндекс жжет. Берем домен из гринурла
                if url == 'http://':
                    html = etree.tostring(sn)
                    pattern = re.compile(ur'<div class="serp-item__greenurl.*?<a class="link serp-url__link".*?>(.*?)</a>', re.I | re.M | re.S)
                    res = pattern.search(html)
                    if res:
                        domain = re.sub(ur'<[^>]+>', '', res.group(1), flags=re.I | re.M | re.S)
                        domain = re.sub(ur'\s+', '', domain, flags=re.I | re.M | re.S)
                        url = 'http://{}'.format(domain)

                is_map = url.startswith('http://maps.yandex.ru')
                position += 1

                if 'infected' in url:
                    match_url_infected = self.patterns['infected'].match(url)
                    if match_url_infected:
                        url = urllib.unquote(match_url_infected.group(1))
                        infected = True

                try:
                    domain = get_full_domain_without_scheme(url)
                except UnicodeError as e:
                    raise e

                if ':' in domain:
                    domain = re.sub(ur':\d+$', '', domain)

                snippet = {
                    'd': domain,
                    'domain': domain,
                    'p': position,
                    'u': url,
                    'm': is_map,
                    't': None,  # title snippet
                    's': None,  # body snippet
                    'i': infected,
                    'savedCopy': None,
                    'fl': self._get_fl(sn)
                }

                if 't' in self.snippet_fileds:
                    if is_video_snippet:
                        snippet['t'] = unicode(sn.find('.//*[@class="video2__title"]').text_content())
                    else:
                        snippet['t'] = unicode(link.text_content())

                if 's' in self.snippet_fileds:
                    decr_div = sn.xpath('.//div[contains(@class,"serp-item__text")]') \
                                or sn.xpath('.//div[contains(@class,"serp-item__data")]') \
                                or sn.xpath('.//div[contains(@class,"social-snippet2__text")]') \
                                or sn.xpath('.//div[contains(@class,"organic__text")]') \
                                or sn.xpath('.//div[contains(@class,"extended-text__short")]') # для мобильной выдачи
                    snippet['s'] = unicode(decr_div[0].text_content()) if decr_div else ''
                    snippet['s'] = snippet['s'] or ''
                div_saved_copy_link = sn.xpath('.//div[contains(@class,"popup2")]')
                if div_saved_copy_link:
                    attrib = div_saved_copy_link[0].find('a')
                    if attrib and 'href' in attrib.attrib:
                        snippet['savedCopy'] = attrib.attrib['href']
                    else:
                        snippet['savedCopy'] = None

                snippets.append(snippet)
            result = snippets

            pagecount = self.get_pagecount()
            len_snippets = len(snippets)
            if pagecount > 50 and len_snippets % 10 != 0:
                cut_snippets = []
                # в этом случае убираем поддомены яндекса из серпа, так чтобы получилось число кратное 10
                need_delete = len_snippets - len_snippets / 10  * 10
                p = 0
                for sn in snippets:
                    if need_delete and re.search(ur'^(?:.+\.|)yandex\.ru$', sn['d'], re.I):
                        need_delete -= 1
                        continue
                    p += 1
                    sn['p'] = p
                    cut_snippets.append(sn)
                result = cut_snippets
        except Exception as e:
            raise YandexParserError(str(e))

        return result

    def _get_fl(self, sn):
        els = sn.xpath('.//span[contains(@class,"serp-meta__item")]')
        if not els:
            return 0
        span_text = els[0].text_content() or ''
        return int(span_text.lower() == u'Ссылки на страницу содержат:'.lower())


    def get_region_code(self, default=None):
        dom = PyQuery(self.content)
        inputs = dom.find('input[name=rstr]')
        if inputs:
            return int(inputs[0].attrib['value'].lstrip('-'))
        return default

    def get_captcha_data(self):
        if 'checkcaptcha' not in self.content:
            return

        match_captcha = self.patterns['captcha'].findall(self.content)
        url_image = match_captcha[0]
        html = lxml.html.fromstring(self.content)
        form = html.forms[0]
        form_data = dict(form.form_values())

        return {
            'url': url_image,
            'form_action': form.action,
            'form_data': form_data,
        }

    @classmethod
    def strip_tags(self, html):
        return re.sub(ur' {2,}', ' ', re.sub(ur'<[^>]*?>', '', html.replace('&nbsp;', ' '))).strip()


class YandexSerpCleaner(object):
    flags = re.U | re.I | re.M | re.S

    _patterns = (
        ur'<script.*?<\/script>',
        ur'<style.*?<\/style>',
        ur'onmousedown=".*?"',
        ur'onclick=".*?"',
        ur'target="_blank"',
        ur'title=".*?"',
        ur'ondblclick=".*?"',
        ur'style=".*?"',
        ur'<noscript>.*?<\/noscript>',
        ur'<link.*?/>',
        ur'<!--.*?-->',
        ur'<i\s+><\/i>',
        ur'data-bem=".*?"',
        ur'\r|\n',
        ur' {2,}',
    )
    patterns = []
    for p in _patterns:
        patterns.append(re.compile(p, flags=re.U | re.I | re.M | re.S))
    patterns = tuple(patterns)

    no_space = re.compile(ur'\s+', flags=flags)

    @classmethod
    def clean(cls, content):
        content = content
        for p in cls.patterns:
            content = p.sub('', content)

        content = cls.no_space.sub(' ', content)
        return content