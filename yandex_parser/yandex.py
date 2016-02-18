# -*- coding:utf-8 -*-
import re
import urllib

from pyquery import PyQuery
import lxml.html
from yandex_parser.exceptions import EmptySerp
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

    def get_serp(self):
        if self.is_not_found():
            return {'pc': 0, 'sn': []}

        if not YandexParser.is_yandex(self.content):
            raise Exception(u'content is not yandex')

        pagecount = self.get_pagecount()
        snippets = self.get_snippets()
        
        if not snippets:
            raise EmptySerp()
        
        return {'pc': pagecount, 'sn': snippets}

    def pagination_exists(self):
        return '<span class="pager__group">' in self.content

    @classmethod
    def is_yandex(cls, content):
        return '<a class="logo__link" href="//www.yandex.' in content

    def get_pagecount(self):
        if self.is_not_found():
            return 0

        patterns = (
            self.patterns['pagecount'],
            re.compile(ur'"found":"[^\\]\\n([^"]*?)отв', self.params_regexr)
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

        dom = PyQuery(self.content)
        serp = dom('.serp-list').find('.serp-item')

        snippets = []
        position = 0
        for sn in serp:
            if 'serp-adv' in sn.attrib['class'] or 'z-' in sn.attrib['class'] or 'serp-item_keyboard-shortcuts-ignore_yes' in sn.attrib['class']:
                #реклама
                continue

            h2 = sn.find('.//h2')
            if not h2:
                raise Exception(u'parse error')

            if 'serp-item__title' not in h2.attrib['class']:
                raise Exception(u'parse error')

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
            # if 'serp-item_plain_yes' not in sn.attrib['class']:
            #
            #     if not is_map:
            #         #картинки, видео и прочее, позицию сохраняем
            #         position += 1
            #         continue
            
            position += 1

            infected = False
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
                'savedCopy': None
            }

            if 't' in self.snippet_fileds:
                snippet['t'] = unicode(link.text_content())

            if 's' in self.snippet_fileds:
                decr_div = sn.xpath('.//div[contains(@class,"serp-item__text")]') \
                           or sn.xpath('.//div[contains(@class,"serp-item__data")]') \
                           or sn.xpath('.//div[contains(@class,"social-snippet2__text")]')
                snippet['s'] = unicode(decr_div[0].text_content()) if decr_div else ''
                snippet['s'] = snippet['s'] or ''
            div_saved_copy_link = sn.xpath('.//div[contains(@class,"popup2")]')
            if div_saved_copy_link:
                attrib = div_saved_copy_link[0].find('a').attrib
                if 'href' in attrib:
                    snippet['savedCopy'] = div_saved_copy_link[0].find('a').attrib['href']
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

        return result
    
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

