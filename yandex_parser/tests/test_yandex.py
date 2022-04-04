# -*- coding:utf-8 -*-
import unittest

from yandex_parser.exceptions import YandexParserContentError, YandexParserError
from yandex_parser.tests import YandexParserTests
from yandex_parser.yandex import YandexParser
from yandex_parser.yandex_bar import YandexBarParser
from yandex_parser.yandex_suggest import YandexSuggestParser


class YandexParserTestCase(YandexParserTests):

    def test_captcha_1(self):
        html = self.get_data('captcha_1.html')
        parser = YandexParser(html)

        captcha_data = parser.get_captcha_data()
        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(captcha_data['url'], u'http://yandex.ru/captchaimg?aHR0cDovL3MuY2FwdGNoYS55YW5kZXgubmV0L2ltYWdlP2tleT1kM1I3SDhDRGlTT3RlVzNvYk9zcFo4bk1lc0NOUjhXQw,,_0/1435077202/853e18711cde74266e45da1315dacee2_2bf39001bd241d1c6539b7db6a0464ad')
        self.assertEquals(captcha_data['form_action'], '/checkcaptcha')
        self.assertEquals(captcha_data['form_data']['key'], 'd3R7H8CDiSOteW3obOspZ8nMesCNR8WC_0/1435077202/853e18711cde74266e45da1315dacee2_ff263da232b103004f79fe4c4e139913')
        self.assertEquals(captcha_data['form_data']['retpath'], 'http://yandex.ru/yandsearch?p=0&text=%D0%BA%D0%BE%D0%BC%D0%BC%D0%B5%D1%80%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5+%D0%B1%D0%B0%D0%BD%D0%BA%D0%B8&site=&numdoc=50&lr=213_cefc8bbe530fbaf69685556720f14a26')

       
    def test_bar_info_1(self):
        html = self.get_data('bar_info_1.xml')
        parser = YandexBarParser(html)
        exp = {
            'domain': u'kokoc.com', 
            'title': u'Тема: Продвижение сайтов', 
            'url': u'http://yaca.yandex.ru/yca/', 
            'rang': u'5', 
            'value': u'1600', 
            'textinfo': u"""Тема: Продвижение сайтов
Регион: Москва
Источник: Официальный
Сектор: Коммерческие"""
        }
        bar = parser.get_bar_info()
        for k, v in exp.iteritems():
            self.assertEquals(bar[k], v)
   
    def test_suggest_1(self):
        html = self.get_data('suggest_1.html')
        parser = YandexSuggestParser(html)
        exp = [
            u"окна пластиковые расчет стоимости онлайн",
            u"окна рехау официальный сайт",
            u"окна роста официальный сайт",
            u"окна 21 век официальный сайт",
            u"окна калева официальный сайт",
            u"окна комфорта официальный сайт москва",
            u"окна роста",
            u"окна века или рехау что лучше",
            u"окна хоббит москва официальный сайт",
            u"окна комфорта"        
        ]
        suggest = parser.get_suggest()
        self.assertEquals(suggest, exp)
           
    def test_region_code_1(self):
        html = self.get_data('region_code_1.html')
        parser = YandexParser(html)

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(parser.get_region_code(), 213)
   
    def test_pagination_exists_1(self):
        html = self.get_data('serp_1.html')
        parser = YandexParser(html)

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertTrue(parser.pagination_exists())
   
    def test_pagination_exists_2(self):
        html = self.get_data('serp_3.html')
        parser = YandexParser(html)

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertFalse(parser.pagination_exists())
   
    def test_pagecount_1(self):
        html = self.get_data('serp_1.html')
        parser = YandexParser(html)

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(parser.get_pagecount(), 124000000)
   
    def test_pagecount_2(self):
        html = self.get_data('serp_2.html')
        parser = YandexParser(html)

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(parser.get_pagecount(), 354000)
   
    def test_pagecount_3(self):
        html = self.get_data('serp_3.html')
        parser = YandexParser(html)

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(parser.get_pagecount(), 22)
   
    def test_not_found(self):
        html = self.get_data('not_found_1.html')
        parser = YandexParser(html)

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertTrue(parser.is_not_found())

    def test4(self):
        html = self.get_data('bad-content.html')
        self.assertFalse(YandexParser.is_yandex(html))

    def test12(self):
        html = self.get_data('v1-2016-02-17.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 228000000)
        self.assertEquals(len(serp['sn']), 50)
        self.assertEquals(serp['sn'][0]['d'], 'qpstol.ru')
        self.assertEquals(serp['sn'][49]['d'], 'moskva.tiu.ru')

    def test13(self):
        html = self.get_data('v1-2016-02-17-1.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 195000)
        self.assertEquals(len(serp['sn']), 50)
        self.assertEquals(serp['sn'][0]['d'], 'roomer.ru')
        self.assertEquals(serp['sn'][49]['d'], 'mybabytoys.ru')

    def test14(self):
        html = self.get_data('v1-2016-02-17-2.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 593000)
        self.assertEquals(len(serp['sn']), 50)
        self.assertEquals(serp['sn'][0]['d'], 'youtube.com')
        self.assertEquals(serp['sn'][49]['d'], 'modmine.net')

    def test15(self):
        html = self.get_data('v1-2016-02-17-3.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 3000000)
        self.assertEquals(len(serp['sn']), 20)
        self.assertEquals(serp['sn'][0]['d'], 'irr.ru')
        self.assertEquals(serp['sn'][19]['d'], 'avito.ru')

    def test16(self):
        html = self.get_data('v1-2016-02-17-4.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 527000000)
        self.assertEquals(len(serp['sn']), 50)
        self.assertEquals(serp['sn'][0]['d'], 'watches.ru')
        self.assertEquals(serp['sn'][49]['d'], 'omax-msk.ru')

    def test17(self):
        html = self.get_data('v1-2016-02-18.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 1000000)
        self.assertEquals(len(serp['sn']), 50)
        self.assertEquals(serp['sn'][0]['d'], 'stihi-rus.ru')
        self.assertEquals(serp['sn'][49]['d'], '4ernovik.ru')

    def test18(self):
        html = self.get_data('v1-2016-02-18-1.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 6000000)
        self.assertEquals(len(serp['sn']), 50)
        self.assertEquals(serp['sn'][0]['d'], 'mylcd.info')
        self.assertEquals(serp['sn'][49]['d'], 'shop.bbk.ru')

    def test19(self):
        html = self.get_data('v1-2016-02-20.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 3000000)
        self.assertEquals(len(serp['sn']), 50)
        self.assertEquals(serp['sn'][0]['d'], 'youtube.com')
        self.assertEquals(serp['sn'][49]['d'], 'truba.com')

    def test20(self):
        html = self.get_data('2016-05-19.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 377000000)
        self.assertEquals(len(serp['sn']), 50)
        self.assertEquals(serp['sn'][0]['d'], 'mebelaero.ru')
        self.assertEquals(serp['sn'][0]['s'], u'Стол PICASSO. 07.04.2016 Компания «AERO» является поставщиком продукции в самый большой в Европе и Москве Porsche-центр.')
        self.assertEquals(serp['sn'][49]['d'], 'stolnadom.ru')
        self.assertEquals(serp['sn'][49]['s'], u'Столы. Мебельный интернет-магазин Стол на Дом .RU - магазин стильной мебели. ... Интернет-магазин мебели - простой способ купить столы в Москве и в России.')

    def test21(self):
        html = self.get_data('2016-06-14-one-res.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 1)
        self.assertEquals(len(serp['sn']), 1)
        self.assertEquals(serp['sn'][0]['d'], 'mogilev.pulscen.by')
        self.assertEquals(serp['sn'][0]['s'], u'Информация о предложениях в рубрике Столешницы для кухни для Могилева. ... Столешницы для кухни в Могилеве. 30 товаров и услуг от 2 поставщиков.')

    def test22(self):
        html = self.get_data('2016-06-14-thousands.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 50000)
        self.assertEquals(len(serp['sn']), 30)
        self.assertEquals(serp['sn'][0]['d'], 'mogilev.deal.by')
        self.assertEquals(serp['sn'][0]['s'], u'Широкий выбор поставщиков, у которых можно купить столешницы и комплектующие в Могилеве по лучшей цене. ... Столешницы для кухни Quartzforms.')
        self.assertEquals(serp['sn'][29]['d'], 'mirdereva.ru')
        self.assertEquals(serp['sn'][29]['s'], u'Столешницы для кухни из дерева. от 1082 р/м2.')

    def test23(self):
        html = self.get_data('2016-06-14-millions.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 13000000)
        self.assertEquals(len(serp['sn']), 30)
        self.assertEquals(serp['sn'][0]['d'], 'otdelka-trade.ru')
        self.assertEquals(serp['sn'][0]['s'], u'Столешница в продаже 28 вида товаров. Доставка по Москве и регионам. Звоните!')
        self.assertEquals(serp['sn'][29]['d'], 'mdvm.ru')
        self.assertEquals(serp['sn'][29]['s'], u'Говоря столешница, многие подразумевают кухонные столешницы, но столешницы из ДСП и МДФ используют не только как столешницы для кухни...')

    def test24(self):
        html = self.get_data('2016-06-16.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 612000)
        self.assertEquals(len(serp['sn']), 50)
        self.assertEquals(serp['sn'][0]['d'], 'exmob.net')
        self.assertEquals(serp['sn'][0]['s'], u'На первом месте самый удобный из них, а именно с помощью SMS. Отправляете сообщение с текстом «СТОП 5051» на аналогичный номер 5051.')
        self.assertEquals(serp['sn'][49]['d'], 'depositfiles.com')
        self.assertEquals(serp['sn'][49]['s'], u'...номерам», введя короткий номер или идентификатор услуги в строке поиска ... SMS-сообщение с текстом «СТОП » на номер 5051 (смс бесплатно в домашнем регионе)')

    def test25(self):
        html = self.get_data('2016-06-16-1.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 168000)
        self.assertEquals(len(serp['sn']), 50)
        self.assertEquals(serp['sn'][0]['d'], 'diamed.ru')
        self.assertEquals(serp['sn'][0]['s'], u'О клинике. Клиника «Диамед» у метро Щелковская открыла свои двери для пациентов в мае 2001 года.')
        self.assertEquals(serp['sn'][49]['d'], 'clinics.webtst.ru')
        self.assertEquals(serp['sn'][49]['s'], u'«Диамед» - это сеть клиник, удобно расположенных в районах Москвы. ... В медицинском центре «Диамед» на Щелковской работают опытные...')

    def test26(self):
        html = self.get_data('2016-07-26.html')

        parser = YandexParser(html)
        serp1 = parser.get_serp()

        cleaned_html = parser.get_clean_html()
        parser = YandexParser(cleaned_html)
        serp2 = parser.get_serp()
        self.assertDictEqual(serp1, serp2)

    def test27(self):
        html = self.get_data('2016-07-31.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 29000000)
        self.assertEquals(len(serp['sn']), 50)
        self.assertEquals(serp['sn'][0]['d'], 'videopartner.kinopoisk.ru')
        self.assertEquals(serp['sn'][0]['t'], u'КонтрольКиноПоиск')
        self.assertEquals(serp['sn'][0]['s'], u'')
        self.assertEquals(serp['sn'][49]['d'], '8serials.ucoz.ru')
        self.assertEquals(serp['sn'][49]['s'], u'Чтобы смотреть Контроль (2004) онлайн бесплатно - регистрация не нужна и смс отправлять не надо, у нас все БЕСПЛАТНО. Для просмотра бесплатных фильмов, мультфильмов, сериалов...')

    def test28(self):
        html = self.get_data('2016-08-01.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 2000000)
        self.assertEquals(len(serp['sn']), 30)
        self.assertEquals(serp['sn'][0]['d'], 'otvet.mail.ru')
        self.assertEquals(serp['sn'][0]['t'], u'Ответы@Mail.Ru: Посоветуйте профессионального фотографа в Кемерово. И желательно что бы можно...')
        self.assertEquals(serp['sn'][0]['s'], u'Пользователь натуська задал вопрос в категории Обработка и печать фото и получил на него 1 ответ...')

        self.assertEquals(serp['sn'][2]['d'], 'xn----gtbm8afgk0g.xn--p1ai')
        self.assertEquals(serp['sn'][2]['fl'], 1)
        self.assertEquals(serp['sn'][2]['t'], u'Студия F"')

        self.assertEquals(serp['sn'][29]['d'], 'kindtoys.ru')
        self.assertEquals(serp['sn'][29]['s'], u'Свадебный фотограф кемерово. 21:42:01 - Диана:Каталог свадебных фирм в Кемерово в рубрике Фотографы.')

    def test29(self):
        html = self.get_data('2016-08-12.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 5000000)
        self.assertEquals(len(serp['sn']), 50)
        self.assertEquals(serp['sn'][0]['d'], 'kinopoisk.megogo.net')
        self.assertEquals(serp['sn'][0]['t'], u'НянькиКиноПоиск')
        self.assertEquals(serp['sn'][0]['s'], u'')

        self.assertEquals(serp['sn'][1]['d'], 'kinogo.co')
        self.assertEquals(serp['sn'][1]['fl'], 0)
        self.assertEquals(serp['sn'][1]['t'], u'Няньки (1995) смотреть онлайн бесплатно')

        self.assertEquals(serp['sn'][49]['d'], 'filmix.net')
        self.assertEquals(serp['sn'][49]['s'], u'Трейлеры, семейный, комедия. Режиссер: Ашот Кещян. В ролях: Николай Наумов, Арарат Кещян, Аглая Шиловская и др. Главная героиня – жесткая и хваткая бизнес-леди по имени Валентина, которая является владелицей успешной туристической компании.')

    def test30(self):
        html = self.get_data('2016-08-15.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 9000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'ttfr.ru')
        self.assertEquals(serp['sn'][0]['t'], u'Федерация настольного тенниса России')
        self.assertEquals(serp['sn'][0]['s'], u'Календарь и результаты соревнований. Рейтинги теннисистов. Описание структуры федерации. Список официальных документов. Новости настольного тенниса. Контакты.')

        self.assertEquals(serp['sn'][49]['d'], 'ttplayspb.com')
        self.assertEquals(serp['sn'][49]['t'], u'ttplayspb - forum ttplayspb')
        self.assertEquals(serp['sn'][49]['s'], u'Admin » 06 авг 2016, 15:56 » в форуме World table tennis. ... ЛЮБИТЕЛЬСКИЙ настольный теннис в г.Санкт-Петербург.')

    def test31(self):
        html = self.get_data('2016-08-15-1.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 323000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'novaposhta.ua')
        self.assertEquals(serp['sn'][0]['t'], u'Термінова і експрес доставка: транспортно-логістичні...')
        self.assertEquals(serp['sn'][0]['s'], u'Весь спектр логістичних послуг, швидка та надійна доставка документів, кореспонденції та листів по Україні ★ Клієнтська подтримка 24/7 ☎ 0-800-500-609...')

        self.assertEquals(serp['sn'][39]['d'], '_www.nm.ru')
        self.assertEquals(serp['sn'][39]['t'], u'_www.nm.ru')
        self.assertEquals(serp['sn'][39]['s'], '')
        self.assertEquals(serp['sn'][39]['savedCopy'], None)

        self.assertEquals(serp['sn'][49]['d'], 'market.yandex.ru')
        self.assertEquals(serp['sn'][49]['t'], u'Купить холодильник Indesit BIA 18 — выгодные цены...')
        self.assertEquals(serp['sn'][49]['s'], u'DPD, Энергия, Экспресс-почта, Эксист, УралТрансСервис, Экспресс-курьер, Почта России, ПЭК, Новая Почта, Желдорэкспедиция, ЖелдорАльянс, Деловые Линии...')

    def test32(self):
        html = self.get_data('2016-09-14.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 22000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'vashdommebel.ru')
        self.assertEquals(serp['sn'][0]['t'], u'Кухонные столы: фото и цены. Купить кухонный стол...')
        self.assertEquals(serp['sn'][0]['s'], u'Кухонные столы. Стол на кухню – это, пожалуй, самый главный предмет мебели ... Мы предлагаем Вам купить кухонный стол по действительно демократичным ценам.')

        self.assertEquals(serp['sn'][49]['d'], 'almekor.ru')
        self.assertEquals(serp['sn'][49]['t'], u'Купить кухонный стол от производителя в Москве.')
        self.assertEquals(serp['sn'][49]['s'], u'Кухонные гарнитуры под заказ. Обеденные столы. ... Товар дня: Стол компьютерный Милан-2Я белый. Цена: 4 000 руб.')

    def test33(self):
        html = self.get_data('2016-10-19.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 19000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'msk.blizko.ru')
        self.assertEquals(serp['sn'][0]['t'], u'Купить встраиваемые стиральные машины в Москве...')
        self.assertEquals(serp['sn'][0]['s'], u'Встраиваемые стиральные машины в Москве. Вам нужна качественная и недорогая встраиваемая машина для стирки?')

        self.assertEquals(serp['sn'][49]['d'], 'bosch.washing-machines.ru')
        self.assertEquals(serp['sn'][49]['t'], u'Стиральные машины Bosch встраиваемые - цены')
        self.assertEquals(serp['sn'][49]['s'], u'Встраиваемые стиральные машины часто устанавливаются на кухню или в ванную комнату. Они позволяют сохранить единый дизайн интерьера...')

    def test34(self):
        html = self.get_data('context-2016-11-23.html')

        parser = YandexParser(html)
        serp = parser.get_context_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 7)

        self.assertEquals(serp['sn'][0]['t'], u'Квартиры от 1,8 млн.руб. Спешите! / barkli-md.ru')
        self.assertEquals(serp['sn'][0]['vu'], u'barkli-md.ru/КупитьКвартиру')
        self.assertEquals(serp['sn'][0]['u'], 'http://yabs.yandex.ru/count/1in6qAYC42440000gO10ZhftLOC5KfK1cm9kGxS198YtUZ7c1edtcy6hkafdiGoTeEyk5PgpdSkK1AQB28gw1xWA1zouRVFO2BsrbZmW1gekfQ0ka0cyh8991eq1tG7Ua2JqaRNHnLW9b_1zAPhsKCHP1fE53Pa5GeoZ3oW9jgmtlmArgF9J0g2bHIeHhwCFA0cpe31T1BIeybC2sQL5AX7Qe31T19IQsWwdbhSBgB10MNC7fB000006hlDn0edKpz0E1h43igGG00AveEyk5Rlj09z9MbYYui7__________m_2yj8q-WXzX1iAn075Zm_J0ku1s_zyDGeTlu1b0T-53V84vP3oA-s3A7WW?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80%D1%83')

        self.assertEquals(serp['sn'][1]['t'], u'Купите апартаменты в ЗАО – Акция!')
        self.assertEquals(serp['sn'][1]['vu'], u'lp.matchpointhouse.ru/Match-Point')
        self.assertEquals(serp['sn'][1]['u'], 'http://yabs.yandex.ru/count/1in6q6Xtz8a40000gO10ZhftLOC5KfK1cm9kGxS193A8l4lxOGI9-nVb1lvG0B02c8qKdQTyB1MQfSwF1AP5YhiouAW6tBwyQNO8lRvYQ-K5gYwbeP5A2RokmVS8ZG7T0TwG9FIHjT75M0cNy7qfclPGn5a6auKDcGL2ZAthkWIsh4Ph0RMet3C1eAsaUWclhUkw1BEeyMW2jAZSCm7PhM2I4jgelRW4b98f4AUHc1UejaJoN0Eai00000Qkyt42YTJFq0u6iGEof1000hcdV2mLk-q0dqbQMABYmV__________3yBoqZJw27s46mh5Zm_J0ku1s_zyDGeTlu1b0T-53V84vP3oA-s3A7WW?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80%D1%83')

        self.assertEquals(serp['sn'][2]['t'], u'ЖК Остоженка 11. Застройщик – Индивидуальный проект')
        self.assertEquals(serp['sn'][2]['vu'], u'ostozenka11.ru')
        self.assertEquals(serp['sn'][2]['u'], 'http://yabs.yandex.ru/count/1in6q1GsVT440000gO10ZhftLOC5KfK1cm9kGxS193E8jRalGWA9_xs6WYwZSj0AdQ5u1nQQggjL2AOZYh44OCGAtBX9f_KBlR-b9Fi7gYwbeG-F2uq1tG7Ua2JqaRNHnLW9b_1zAPhsKCHP1fE53Pa5GeojxrmEjgmKJmIrgD2c0w2eLc0PhwtlN0wpg9np1hIeqAO3sQ0JbndQe8U11fIRHGwdbNq7gA0LtI6ai00000Qkyt42YTJFq0u6iGEof1000hcXU0SMk-q0dqbQMABYmV__________3yBoqZJw27s46mh5Zm_J0ku1s_zyDGeTlu1b0T-53V84vP3oA-s3A7yU?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80%D1%83')

        self.assertEquals(serp['sn'][3]['t'], u'Новостройки в Москве и области / pik.ru')
        self.assertEquals(serp['sn'][3]['vu'], u'pik.ru/Группа-Компаний-ПИК')
        self.assertEquals(serp['sn'][3]['u'], 'http://yabs.yandex.ru/count/1in6q2y0JL040000gO10ZhftLOC5KfK2cm5kGxS2BG68iUGfqmQ9g43LV9YD59sc-ouLfeO8Yh74nEK7tBOAnvq9lRr_U9a6gYwbh78N2hoa5WKAZG7T0TwG9FJqiaN801cHjT75M0cNy7qfclPGn5a6auKDcGL2ZA1Vz0Qsg1mM0hMWeyG1eALOyWsle5_q1hEWjui3jA2Zn07PfQ502DgW71a2b9yviwUNNGUei41PSmUai00000Qkyt42YTJFq0u6iG6of1400hcc-ouLk-q0dqbQMABYmV__________3yBoqZJw27s46mh5Zm_J0jIJoepk0Tl_V3KA7R-0PG7VXGtbaF8hxOCeVny0?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80%D1%83')

        self.assertEquals(serp['sn'][4]['t'], u'Купите квартиру в 12 км от МКАД! / pirogovo-riviera.ru')
        self.assertEquals(serp['sn'][4]['vu'], u'pirogovo-riviera.ru/купить квартиру')
        self.assertEquals(serp['sn'][4]['u'], 'http://yabs.yandex.ru/count/1in6q4pJLPm40000gO10ZhftLOC5KfK2cm5kGxS2BG4oYBCUot45YQKhctoTg-kE4gPMYhQDBACAtBI1-xeBlR6y8TS7gYwbgVPv2xogVc4BZG7T0TwG9FJqjZsDqXoHjT75M0cNy7qfclPGn5a6auKDcGL2ZAZZbWgsf4Gj0xMeDR42eA3oO0olgEEM2hEWgYK3jAWriGBPeF9W3DgWgYK3b9TstwUQd0Eei41PSmUai00000Qkyt42YTJFq0u6iG6of1400hchwuuIk-q0dqbQMABYmV__________3yBoqZJw27s46mh40SMF3zC2xW7R_tmr2Xs_W6K1tuKDvP3oA-s3A7eV?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80%D1%83')

        self.assertEquals(serp['sn'][5]['t'], u'Купить квартиру в Красногорске – От 2,7 млн. рублей!')
        self.assertEquals(serp['sn'][5]['vu'], u'urbangroup.ru/Красногорск-квартиры')
        self.assertEquals(serp['sn'][5]['u'], 'http://yabs.yandex.ru/count/1in6qAwFyMa40000gO10ZhftLOC5KfK2cm5kGxS2BG4pYAKTBVA9lOWgZWMThPEc2QOEYhT-2-G9tB40lYeBlRZ6CeG7gYwbhnO52xoX8yS4ZG7T0TwG9FIHjT75M0cNy7qfclPGn5a6auKDcGL2ZAlArmcseF3p0hMWe802eAl9K0glgyhN2REWOvy2jA2WW0BPbHBmsf09FPINRzgdcWe4gB10MNC7fB000006hlDn0edKpz0E1h41igGH00AvhPEc2Rlj09z9MbYYui7__________m_2yj8q-WXzX1iAnOyFqmBKdyYbxW7R_tmr2Xs_W6K1tuKDvP3oA-s3A7mU?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80%D1%83')

        self.assertEquals(serp['sn'][6]['t'], u'Выкуп квартир в Москве! – Максимально дорого и быстро!')
        self.assertEquals(serp['sn'][6]['vu'], u'elite-tn.ru')
        self.assertEquals(serp['sn'][6]['u'], 'http://yabs.yandex.ru/count/1in6q3SxX_040000gO10ZhftLOC5KfK2cm5kGxS2BG4qYBFNC281YQX0rNoOH9sXFaa4fX6AiWHILGRSiYCL9WYzjLqQjGMgBgManz88lAA3f0YD0Tq1tf0azFIocqX45f6rqSLO2PVmVIcQzb34MGQJXGsP1KACgu9D2RQWU5q2jQ1uNGAWfKLd2w-hWaq9iw0mvWAqe7XT0jcbHMSBsg0mvWAKacFHfv9e1AYcEST-fB000006hlDn0edKpz0E1h41igGH00AveJv91Blj09z9MbYYui7__________m_2yj8q-WXzX1iAn075Z0_J0ku1s_zyDGeTlu1b0T-53Us3A7yU?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80%D1%83')

    def test35(self):
        html = self.get_data('context-2016-11-23-1.html')

        parser = YandexParser(html)
        serp = parser.get_context_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 7)

        self.assertEquals(serp['sn'][0]['t'], u'Столешницы из ДСП купить / лавуччи.рф')
        self.assertEquals(serp['sn'][0]['vu'], u'лавуччи.рф')
        self.assertEquals(serp['sn'][0]['u'], 'http://yabs.yandex.ru/count/3B7F6lnBK3m40000gO10ZhYMLuC5KfK1cm9kGxS198Yti9zH18cZbaK3c0UTfXWp5QP4YhCB1gO3tBqtR_i4lRNGNAm3gYwbf-cD1hobSri6ZG7T0TwG9FIHlK_lp0kNy3Z14_PGn5a6auKDcGL2ZAkUr06sa9QCjP0aTw2Zi3C2hwkUr06pc4-Fj90aTzcZi3C2sfXFZvIHYXUdbkabgA5H20wai00000Qk-hw0BQT0KWy6iG6of3000hcc63CLk-q0dqbQMABYmV__________3yBm6M5GecpNrmN5ZW_J0ku1s_zyDGeTlu1b0T-53UMGyYljWoXy7G00?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB%D0%B5%D1%88%D0%BD%D0%B8%D1%86%D1%83')

        self.assertEquals(serp['sn'][1]['t'], u'Купить деревянную столешницу – со скидкой 18%')
        self.assertEquals(serp['sn'][1]['vu'], u'dilektwood.ru/столешницы')
        self.assertEquals(serp['sn'][1]['u'], 'http://yabs.yandex.ru/count/3B7F6gwpsaS40000gO10ZhYMLuC5KfK1cm9kGxS193A8jbDLC069iqofiWIOZHITgcn34AOIYhUdDNC7tBtgYq89lR0I9606gYwbg0JH2Roexcu3ZG7T0TwG9FIHlK_lp0kNy3Z14_PGn5a6auKDcGL2ZACTYWAsd0Z3jPX8fQ2hRi4IhwCTYWApeBJ41BIOIANPgsx14jgWjCG4b95S5wUGLIUei41PSmUai00000Qk-hw0BQT0KWy6iG6of1000hcgR4CGk-q0dqbQMABYmV__________3yBm6M5GecpNrmN40SMF3zC2xW7R_tmr2Xs_W6K1tuKDvP3oA-s3A7mU?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB%D0%B5%D1%88%D0%BD%D0%B8%D1%86%D1%83')

        self.assertEquals(serp['sn'][2]['t'], u'Купить столешницу. Качество! – Искусственный камень!')
        self.assertEquals(serp['sn'][2]['vu'], u'akrilion.ru')
        self.assertEquals(serp['sn'][2]['u'], 'http://yabs.yandex.ru/count/3B7F6h81oEC40000gO10ZhYMLuC5KfK1cm9kGxS193E8lhOKe0M9jW56CGMOZHITeDrQ5QPPYhvw89W9tBsPwUa9lRWZfyO6gYwbffFT2hoW9H8AZG7T0TwG9FJqj7iDL1cHlK_lp0kNy3Z14_PGn5a6auKDcGL2ZAtC60Asb0gXjPXvYA2WB402hwtC60Apa7oIj9XvYDcWB402sf1yafILLXYdaXubgBxzgyW5fB000006hlg-W2sdG58F1h41igGG00AveDrQ5Rlj09z9MbYYui7__________m_2y1bXKA9irzS5n075Zm_J0ku1s_zyDGeTlu1b0T-53UMGyYljWoXu7m00?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB%D0%B5%D1%88%D0%BD%D0%B8%D1%86%D1%83')

        self.assertEquals(serp['sn'][3]['t'], u'Купить деревянную столешницу – со скидкой 18%')
        self.assertEquals(serp['sn'][3]['vu'], u'lesnoywood.ru/столешницы')
        self.assertEquals(serp['sn'][3]['u'], 'http://yabs.yandex.ru/count/3B7F6ife0Ru40000gO10ZhYMLuC5KfK2cm5kGxS2BG68lk4fW069iqofiWIOZHITgChW4QONYh4IcEi9tBEilwyAlRyvypm7gYwbehMv2hoj9743ZG7T0TwG9FIHlK_lp0kNy3Z14_PGn5a6auKDcGL2ZA3ZBWAscAgdjP0NZg2hRi4Ihw3ZBWApeBJ41BIG5uxPgsx14jgWjCG4b9UeuwUQo1EeiE7xNG6ai00000Qk-hw0BQT0KWy6iG6of1400hceok0Hk-q0dqbQMABYmV__________3yBm6M5GecpNrmN5Zm_J0ku1s_zyDGeTlu1b0T-53UMGyYljWoXw7W00?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB%D0%B5%D1%88%D0%BD%D0%B8%D1%86%D1%83')

        self.assertEquals(serp['sn'][4]['t'], u'Кварцевые столешницы! – Большой выбор цветов')
        self.assertEquals(serp['sn'][4]['vu'], u'synstone.ru/кварцевые-столешницы')
        self.assertEquals(serp['sn'][4]['u'], 'http://yabs.yandex.ru/count/3B7F6WckWtK40000gO10ZhYMLuC5KfK2cm5kGxS2BG4oYASVBkA9y4F4EVMuUB8Cc8qKdQph1XEQedugzwODYhBxnUS8tBARapSAlRARIlK6gYwbhW5w2hodkciAZG7T0TwG9FIHlK_lp0kNy3Z14_PGn5a6auKDcGL2ZAj3WWIsg4TQ0RMWTIK1eAXeM0MlgqE21BEevbi1jA1r9G7Pg6XO1Tgevbi1b9j3iAUQ1mQeiVvPrGIai00000Qk-hw0BQT0KWy6iGEof1400hciwmOJk-q0dqbQMABYmV__________3yBm6M5GecpNrmN5Zm_J0ku1s_zyDGeTlu1b0T-53V84vP3oA-s3A7WW?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB%D0%B5%D1%88%D0%BD%D0%B8%D1%86%D1%83')

        self.assertEquals(serp['sn'][5]['t'], u'Гранитные столешницы / albiongranit.ru')
        self.assertEquals(serp['sn'][5]['vu'], u'albiongranit.ru/Гранитные-столешницы')
        self.assertEquals(serp['sn'][5]['u'], 'http://yabs.yandex.ru/count/3B7F6frnX0K40000gO10ZhYMLuC5KfK2cm5kGxS2BG4pYAb8jz29yAaX9cjCJFmEc8qKdQ35hH6QkU0ak0Ic38gud_E41zor0yTI2Rsvdvfg1gekfQTT80ED0Tq1teW-aRrFxymBb_0umHFsKCHP1fE53Pa5Geobt6a3jgWe1W6ra2lUeA1ol0ElfTnf0xEGAlEqa2lUsQjG80JQe8uC0PIHcwMddXa9g9be_QIm00001gxwle0jfq1I3mQn0xAa4G02kQ35hH6xxG2VILfOekB1__________yFml0POL2YRDVN1SG1nOyFqmBk0Tl_V3KA7R-0PG7VXGto4UMGyYljWoXu7m00?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB%D0%B5%D1%88%D0%BD%D0%B8%D1%86%D1%83')

        self.assertEquals(serp['sn'][6]['t'], u'Купить столешницу – Искусственный камень')
        self.assertEquals(serp['sn'][6]['vu'], u'stolkit.ru/столешницы')
        self.assertEquals(serp['sn'][6]['u'], 'http://yabs.yandex.ru/count/3B7F6ZVKFwG40000gO10ZhYMLuC5KfK2cm5kGxS2BG4qYBoE4T04YQVjRNsOZHITeqOJ4wPCYhj55N8AtBUcJgeBlRmG2Sy7gYwbgjTQ2xoisbaBZG7T0TwG9FJqlH1Rl1oHlK_lp0kNy3Z14_PGn5a6auKDcGL2ZADCNmEsfFq20RMOUzkWfKd00w-ZJ5y3iv0azBIOUzlPfKd00zgG9FIKadtffvb32QYeYIQPfB000006hlg-W2sdG58F1h41igGH00AveqOJ4xlj09z9MbYYui7__________m_2y1bXKA9irzS5n075Zm_J0ku1s_zyDGeTlu1b0T-53UMGyYljWoXu7m00?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB%D0%B5%D1%88%D0%BD%D0%B8%D1%86%D1%83')

    def test36(self):
        html = self.get_data('context-2016-11-25.html')

        parser = YandexParser(html)
        serp = parser.get_context_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 11)

        self.assertEquals(serp['sn'][0]['t'], u'Купить стол для кухни недорого / malinki-mebel.ru')
        self.assertEquals(serp['sn'][0]['vu'], u'malinki-mebel.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://yabs.yandex.ru/count/5MIiU7H2VxG40000gO10ZhhdVeC5KfK1cmDkGxS198Yb7nboYPchHPXddQdoxnMc1egr4ZiN2zo-xurB3BsvN4ze1wekfQjyvWgyhhpb2eq1tG7Ua2JqaRuvdR4Db-1Nny7nBv6kau4CeeKDcGL2Z9rYLxQKDngrc3SMe9MniA-TObUpaEmij9Wt5jcLiR3QaEmib9dj5AUPb1sehVikBAJ00000V0skyiA0OCdpiHW6iG6of10C0hcfykyLk-q0dqbQMABYmV__________3yBnJUVJ5lC3Y0Z5Zm_J0ku1s_zyDGeTlu1b0T-13EMGyYljWoXv7G00?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB')
        self.assertEquals(serp['sn'][0]['a'], 't')

        self.assertEquals(serp['sn'][1]['t'], u'HOFF.ru - Купите Стол 1990 руб. / hoff.ru')
        self.assertEquals(serp['sn'][1]['vu'], u'hoff.ru/куплю-стол-недорого')
        self.assertEquals(serp['sn'][1]['u'], 'http://yabs.yandex.ru/count/5MIiUAi-t-C40000gO10ZhhdVeC5KfK1cmDkGxS193A8i3ZP0GM9jZywZGIOCPsk-CW8fa-Aj8WcrGVSjI3LaWczlw5SaWQgBgMaY0iAlANRkmcD0Tq1tf0azFIr7MZ1696-EPsn3PVWLyV1yI-HhfE13AA53Pa5GeoLxp6saFiEjP2o3A2OSfwlbUynivX8ABIGiWpPc7AUsfX8A9IGDnYdcRqrgB10MNC7fC00001y3Qxome1WoVEn60Qn0RAa40m2kQxuo0YxxG2VILfOekB1__________yFml5DvzCMymE82CMF3zC2xW7R_tmr2Xs_W6K1tu4CvP3oA-s3A7mU?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB')
        self.assertEquals(serp['sn'][1]['a'], 't')

        self.assertEquals(serp['sn'][2]['t'], u'Стол ЭЛИС 140 90-ОВШ Лидер мебель')
        self.assertEquals(serp['sn'][2]['vu'], u'az-stil.ru')
        self.assertEquals(serp['sn'][2]['u'], 'http://yabs.yandex.ru/count/5MIiU6VvUA040000gO10ZhhdVeC5KfK2cmHkGxS2BG68hNXDCOdxvM_yvXeHH0-OPvsiTAe3cgcZdlwc0egstryF1Toz08p31hstWCZL1AekfQxBKGAyhld30eq1tG7Ua2JqaRuvdR4Db-1Nny7nBv6kau4CeeKDcGL2Z91XFxQO0nEra1qGeA2qMG6la64_iv3aLxIG7H3PeBHP0TgGv5UKdPwhfv1W1QYngELM0gJ00000V0skyiA0OCdpiHW6iGEoh14S0hciTAe3k-q0dqbQMABYmV__________3yBnJUVJ5lC3Y0Z40SMF3zC2xW7R_tmr2Xs_W6K1tu4CyWJbaF8hxOCeV1y0?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB')
        self.assertEquals(serp['sn'][2]['a'], 'r')

        self.assertEquals(serp['sn'][3]['t'], u'Стол + стулья по шоколадной цене!')
        self.assertEquals(serp['sn'][3]['vu'], u'1fab.org/Акция-стол-и-стулья')
        self.assertEquals(serp['sn'][3]['u'], 'http://yabs.yandex.ru/count/5MIiU9imcga40000gO10ZhhdVeC5KfK2cmHkGxS2BG4oYBk0xZ43YRO-bn85c0UTe_t04gOoYhBb1DO2tBKl-mC4lR7X-kS2gYwbfVsD1Oq1tG7Ua2JqaRuvdR4Db-1Nny7nBv6kau4CeeKDcGL2Z9s78xQSg0grc0W9e9sJEg-TXoEpcEGEj9W82TcLTJtQaA0Fb9pqugUUXWgeeVqc1wJ00000V0skyiA0OCdpiHW6iG6oh14C0hcZ_S0Ik-q0dqbQMABYmV__________3yBnJUVJ5lC3Y0Z40SMF3zC2xW7R_tmr2Xs_W6K1tu4CvP3oA-s3A7iT?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB')
        self.assertEquals(serp['sn'][3]['a'], 'r')

        self.assertEquals(serp['sn'][4]['t'], u'Обеденный стол от производителя!')
        self.assertEquals(serp['sn'][4]['vu'], u'stol26.ru//katalog/stoly/')
        self.assertEquals(serp['sn'][4]['u'], 'http://yabs.yandex.ru/count/5MIiUFfj5f040000gO10ZhhdVeC5KfK2cmHkGxS2BG4pYBda5S81YRRqiPO1c6UTfUAq4QORYhs8SO88tBfza-m9lRR0ECW6gYwbfls02RoaIb49ZG7T0TwG9FIHlZcTiGsNu5V7mV4laQwJWGoYXGsP1KACdGqljfmT3hMOzWkWc492hvqDBxEOs12qcFOBsPX2GjgOs12KdfNYfvq71gYl7ESjfC00001y3Qxome1WoVEn60Qn0RAiCGm2kQNYj16xxG2VILfOekB1__________yFml5DvzCMymE82DC2xW7R_tmr2Xs_W6K1tu4CvP3oA-s3A7iT?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB')
        self.assertEquals(serp['sn'][4]['a'], 'r')

        self.assertEquals(serp['sn'][5]['t'], u'Стол Melody, Futura скидка −20%')
        self.assertEquals(serp['sn'][5]['vu'], u'gardeck.ru')
        self.assertEquals(serp['sn'][5]['u'], 'http://yabs.yandex.ru/count/5MIiU0ZKh2O40000gO10ZhhdVeC5KfK2cmHkGxS2BG4qYA4Buw69zD-0fTpvSRyAc8WhdQrX6GMQlY1_4mEc2Ogzpxix0zop53MN1BsxD2Dg0wekfQZY8GQyfT182Oq1tG7Ua2JqaRuvdR4Db-1Nny7nBv6kau4CeeKDcGL2Z9YyDhQSQn2rcEeDe9jCGQ-Ol3Qpa9eGj9Zg3TcL1s3Qa6eOb9t6dQUHlGIejK5J7W6am00007mDhlB2W639yx4O1h43igmH30AvhM4P1Rlj09z9MbYYui7__________m_2yKtdqnRp0uW8n075Zm_J0ku1s_zyDGeTlu1b0T-13F82vP3oA-s3A7qV?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB')
        self.assertEquals(serp['sn'][5]['a'], 'r')

        self.assertEquals(serp['sn'][6]['t'], u'Столы купить')
        self.assertEquals(serp['sn'][6]['vu'], u'mebelandia.com/столы-купить')
        self.assertEquals(serp['sn'][6]['u'], 'http://yabs.yandex.ru/count/5MIiUEQfk2K40000gO10ZhhdVeC5KfK2cmLkGxS2BG4rYBk7lY45YQYFIfYOM9sfNVS3fb6AkhBtLGhSkfzcaGkzjL36m0UgBgMfbqWBlAhepmgD0Tq1tf0az96-EPsn3PVWLyV1yI-HhfE13AA53Pa5GeoJ5XQsbA06jPYT1Q2GpnolanOMiv1J1xIOdGNPaCySsf1J1vIJ4GwdaMiCgAaq9Akam00007mDhlB2W639yx4O1h41igmG30AvgLtt0xlj09z9MbYYui7__________m_2yKtdqnRp0uW8n075Zm_J0ku1s_zyDGeTlu1b0T-13EMGyYljWoX_7G00?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB')
        self.assertEquals(serp['sn'][6]['a'], 'r')

        self.assertEquals(serp['sn'][7]['t'], u'Купить стол')
        self.assertEquals(serp['sn'][7]['vu'], u'youcom.spb.ru')
        self.assertEquals(serp['sn'][7]['u'], 'http://yabs.yandex.ru/count/5MIiUFRPEoG40000gO10ZhhdVeC5KfK2cmLkGxS2BG4sYB5--c41YR-rLK83c0UTeSKB0wOLYh2gJbO2tBv6Erq3lRAygfa2gYwbg3hZ1BolBDi9ZG7T0TwG9FIHlZcTiGsNu5V7mV4laQwJWGoYXGsP1KACbI0LjfXM1hMGNmMWaCyShvKW5REGKmUqa5y5sP3F7DgGKmUKc5i7fvCe2AYc-l9PfC00001y3Qxome1WoVEn60Qn0RAi40m2kQ752mExxG2VILfOekB1__________yFml5DvzCMymE82CMF3zC2xW7R_tmr2Xs_W6K1tu4CvP3oA-s3A7uT?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB')
        self.assertEquals(serp['sn'][7]['a'], 'r')

        self.assertEquals(serp['sn'][8]['t'], u'Купите стол в магазине Купистол.')
        self.assertEquals(serp['sn'][8]['vu'], u'qpstol.ru')
        self.assertEquals(serp['sn'][8]['u'], 'http://yabs.yandex.ru/count/5MIiU1dN0ye40000gO10ZhhdVeC5KfK2cmLkGxS2BG4tYBjqz8O6YRTafmq2c6UTfbGn0gPoYhOXl3i7tBRoinS9lRlKI4K6gYwbemfb2RoZys03ZG7T0TwG9FJqiwb6w1UHlZcTiGsNu5V7mV4laQwJWGoYXGsP1KACa4aHjfWl1RMGPGIWa4aHhv194REGPGIqa6K4sP194TgGPGIKceG5fvMp1gYmG5bp1wJ00000V0skyiA0OCdpiHW6iG6oh10C0hccL342k-q0dqbQMABYmV__________3yBnJUVJ5lC3Y0Z5Zm_J0ku1s_zyDGeTlu1b0T-13EMGyYljWoXz7W00?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB')
        self.assertEquals(serp['sn'][8]['a'], 'r')

        self.assertEquals(serp['sn'][9]['t'], u'Мебель ИКЕА цены')
        self.assertEquals(serp['sn'][9]['vu'], u'ikea-vsem.ru/Доставка-ИКЕА-Москва')
        self.assertEquals(serp['sn'][9]['u'], 'http://yabs.yandex.ru/count/5MIiU2JpHRq40000gO10ZhhdVeC5KfK2cmLkGxS2BG4u0OYtU9Nq1edwp5lTGmFlL0sOPvskO1uBcgBZQ3EcZmYAk6lKPGhSkl8Gd0kzjUIqnWUgBgMkXbCBZG7T0TwG9FIHlZcTiGsNu5V7mV4laQwJWGoYXGsP1KACarCGjfpb1BMO9WIWcpGJhvDJ4BEGuWIqc2O4sPiq4zgGuWIdc6e5gAst8UAam00007mDhlB2W639yx4O1h43igoG30Avhc0U2xlj09z9MbYYui7__________m_2yKtdqnRp0uW8nOyFqmBk0Tl_V3KA7R-0PG7VWGpo0kMGyYljWoXw7W00?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB')
        self.assertEquals(serp['sn'][9]['a'], 'r')

        self.assertEquals(serp['sn'][10]['t'], u'Кухонные столы от 3500 рублей')
        self.assertEquals(serp['sn'][10]['vu'], u'mebelmarket.su')
        self.assertEquals(serp['sn'][10]['u'], 'http://yabs.yandex.ru/count/5MIiUDlNGSq40000gO10ZhhdVeC5KfK2cmLkGxS2BG4v0OYqusv10ecsiQEK0fW7dQudfmgc8ugn4hTZ0jomywbk0xsqXOQb0gekfQvi5WMD0Tq1tf0az96-EPsn3PVWLyV1yI-HhfE13AA53Pa5GeoLcWcscE42jP1n0g2LcWclbPe9iv1n0hIGSGBPbPe9sf1n0fIS-WgddUe7gAEUXXEam00007mDhlB2W639yx4O1h41igmm30AvhYUd2hlj09z9MbYYui7__________m_2yKtdqnRp0uW8qmBk0Tl_V3KA7R-0PG7VWGpbaF8hxOCeVnm0?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB')
        self.assertEquals(serp['sn'][10]['a'], 'r')

    def test37(self):
        html = self.get_data('2016-12-21.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], None)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'spec.drom.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://spec.drom.ru/moskva/bus/')
        self.assertEquals(serp['sn'][0]['t'], u'Продажа автобусов в Москве. Цены. Купить автобус...')
        self.assertEquals(serp['sn'][0]['s'], u'Дром Спецтехника и грузовики: объявления о продаже и покупке Купить автобус б/у или новый. Продажа автобусов в Москве. Купить автобус в Москве. Все города | Москва | Выбрать город... Модель Тип Цена Состояние Год Количество мест Наличие фото. ... Автобус Higer KLQ 6928 Q 35 мест 2013 год Москва, 6 700 куб. см., 35 мест. 17:09, вчера 290. 1 290 000 р. Higer, 2007. Higer KLQ6840 автобус, 5 880 куб. см., 33 места. 16:54, вчера 9. 700 000 р. Скрыть')

        self.assertEquals(serp['sn'][1]['d'], 'm.irr.ru')
        self.assertEquals(serp['sn'][1]['u'], 'http://m.irr.ru/cars/commercial/buses/')
        self.assertEquals(serp['sn'][1]['t'], u'Автобусы в Москве и области продажа, цены | купить автобус...')
        self.assertEquals(serp['sn'][1]['s'], u'ИЗ РУК В РУКИ - Коммерческий транспорт в Москве и области. Купить автобус б/у или новый - частные объявления и предложения дилеров. Продать автобус - подай объявление в своём городе. Скрыть')

        self.assertEquals(serp['sn'][2]['d'], 'farpost.ru')
        self.assertEquals(serp['sn'][2]['u'], 'http://www.farpost.ru/moskva/auto/spectech/bus/')
        self.assertEquals(serp['sn'][2]['t'], u'Купить АВТОБУС в Москве. Новый или БУ автобус. Цены. Фото.')
        self.assertEquals(serp['sn'][2]['s'], u'Купить автобус в Москве. Продажа автобусов в Москве с фото. Аукционные, новые и б.у. Производство: Корея, Япония, Китай, Россия и др. Автобус без пробега по РФ или с пробегом. Модель Тип Цена Состояние Год Количество мест Наличие фото. Скрыть')

        self.assertEquals(serp['sn'][49]['d'], 'moskva.regmarkets.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://moskva.regmarkets.ru/igrushechnye-avtobusy-11419/')
        self.assertEquals(serp['sn'][49]['t'], u'Игрушечные автобусы модели, паз, лиаз купить в Москве.')
        self.assertEquals(serp['sn'][49]['s'], u'Чтобы узнать, как купить модель игрушечного автобуса паз, с открывающимися дверями в Москве по доступной цене, воспользуйтесь нашим сервисом. Вы найдете дешевые товары и самые выгодные предложения с описанием, фото, отзывами и адресами. Цены и магазины недорогих игрушечных автобусов лиаз можно посмотреть в нашем онлайн интернет каталоге товаров Москвы, а так же узнать, где продаются большие игрушечные автобусы оптом в Москве. Скрыть')

    def test38(self):
        html = self.get_data('2016-12-21-1.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], None)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'eldorado.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://www.eldorado.ru/promo/Notebook_SUPER_Sale/')
        self.assertEquals(serp['sn'][0]['t'], u'Тотальная распродажа ноутбуков')
        self.assertEquals(serp['sn'][0]['s'], u'Ноутбуки для бизнесаМаксимальные возможности и свобода передвижений для вас и вашего бизнеса. Вам не обязательно все время находиться на рабочем месте. Основными преимуществами является долгое время работы, большой объем памяти, максимальная комплектация и мощная операционная система. Ноутбук Acer AS3830T-2414G50n. Скрыть')

        self.assertEquals(serp['sn'][49]['d'], 'chel.blizko.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://chel.blizko.ru/predl/computer/computer/notebook/noutbuki')
        self.assertEquals(serp['sn'][49]['t'], u'Ноутбуки Acer в Челябинске - Портал выгодных покупок BLIZKO.ru')
        self.assertEquals(serp['sn'][49]['s'], u'Вам нужно купить в Челябинске ноутбук марки Acer? Данную задачу будет легко решить с помощью раздела «Ноутбуки». Здесь вы сможете быстро выбрать наиболее подходящую вам модель ноутбука от Acer. Раздел позволяет ознакомиться с ассортиментом ноутбуков этой марки, сравнить цены, а также быстро получить всю необходимую контактную информацию по магазинам Челябинска, занимающихся их продажей. ... Каталог актуальных акций и распродаж. Посмотреть >. Ультрабук Dell Latitude E7270 (7270-0523). Скрыть')

    def test39(self):
        html = self.get_data('2016-12-21-2.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], None)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'svyaznoy.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://www.svyaznoy.ru/catalog/phone/224')
        self.assertEquals(serp['sn'][0]['t'], u'Мобильные телефоны - купить сотовый телефон в кредит, цены...')
        self.assertEquals(serp['sn'][0]['s'], u'Интернет магазин Связной предлагает ознакомиться с каталогом мобильных телефонов, в котором представлены модели с ценами от 1 390 до 76 890 рублей. На страницах нашего сайта Вы можете изучить технические характеристики всех представленных моделей, прочитать отзывы, сравнить стоимость и ознакомиться с условиями покупки в кредит. Скрыть')

        self.assertEquals(serp['sn'][49]['d'], 'lorena-kuhni.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://lorena-kuhni.ru/catalog/')
        self.assertEquals(serp['sn'][49]['t'], u'Каталог')
        self.assertEquals(serp['sn'][49]['s'], u'Каталог. «Современная коллекция/Модерн» (17) «Городская классика» (18) «Классика» (20). Если классика – вне моды, то модерн всегда на самом ее пике. ... Отправить отзыв директору. Ваше имя*. Телефон*. Ваш город. Альметьевск Астана Астрахань Барнаул Белгород Березники Владивосток Владимир Волгоград Дзержинск Екатеринбург Иваново Иркутск Казань Калуга Каменск-Уральский Кемерово Киров Краснодар Красноярск Курган Липецк Магнитогорск Махачкала Миасс Москва Набережные Челны Находка Нефтекамск Нефтеюганск Нижневартовск Нижнекамск Нижний Новгород Нижний Тагил Новокузнецк Новороссийск Новосибирск Новый Уренгой Ноябрьск Нягань Обнинск Октябрьский Омск Оренбург Орск Пермь Ростов-на-Дону Рязань Салехард Самара Санкт-Петербург Серов Снежинск Сочи Стерлитам... Скрыть')

    def test40(self):
        html = self.get_data('2016-12-21-3.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], None)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'm.avito.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://m.avito.ru/samarskaya_oblast/telefony/iphone?p=3')
        self.assertEquals(serp['sn'][0]['t'], u'Купить iPhone 7, 6S, 6, 5SE, 5S, 5, 4S, 4 в Самарской области...')
        self.assertEquals(serp['sn'][0]['s'], u'Бесплатные объявления о продаже мобильных телефонов iPhone 7, Айфон 6, iPhone 6S, 5SE, iPhone 5S, 5C, Айфон 5, 4S 4 в Самарской области. Самая свежая база объявлений на Avito. ... Самара. Вчера, 21:59. Айфон 4s 8Гб. 6 000 руб. Самара. Вчера, 21:51. iPhone 4s 32 gb. 7 500 руб. Новокуйбышевск. Скрыть')

        self.assertEquals(serp['sn'][49]['d'], 'electronics.wikimart.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://electronics.wikimart.ru/communication/cell/tag/iphone4/')
        self.assertEquals(serp['sn'][49]['t'], u'Купить iPhone 4 в Москве в интернет магазине. Айфон 4: цены...')
        self.assertEquals(serp['sn'][49]['s'], u'7 моделей Apple iPhone 4 от 5335 руб. в наличии! Покупайте Apple iPhone 4 ✈✈✈ с доставкой на Викимарт. ... Apple iPhone 4 отличаются дорогими высококачественными материалами, большим количеством приложений и функций. По сравнению с телефонами предыдущего поколения модели оснащены новой операционной системой. Корпус и рамка смартфонов состоят из металла, торцы изделий исполняют роль антенн. Скрыть')

    def test41(self):
        html = self.get_data('2016-12-21-4.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], None)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'eldorado.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://www.eldorado.ru/cat/1667707/SONY/')
        self.assertEquals(serp['sn'][0]['t'], u'MP3-плееры SONY – купить MP3-плеер Sony (Сони), цены, отзывы.')
        self.assertEquals(serp['sn'][0]['s'], u'Продажа MP3-плееров SONY (Сони). В нашем каталоге вы можете ознакомиться с ценами, отзывами покупателей, подробным описанием, фотографиями и техническими характеристиками MP3-плееров Sony. В интернет-магазине ЭЛЬДОРАДО можно купить MP3-плеер Сони с гарантией и доставкой. Скрыть')

        # Тут внимание - пустой заголовок сниппета
        self.assertEquals(serp['sn'][40]['d'], 'sportlifeabout.ru')
        self.assertEquals(serp['sn'][40]['u'], 'http://sportlifeabout.ru/1/useful-articles/74-obzor-pleera-sony-nw-w273')
        self.assertEquals(serp['sn'][40]['t'], None)
        self.assertEquals(serp['sn'][40]['s'], u'В отличие от большинства других плееров Сони, изобилующих различными опциями — одни из которых делают звук «кристально чистым», другие чудодейственным образом на лету «восстанавливают» потерянные при сжатии детали звука, третьи «прокачивают» наушники мощным басом, в Sony Walkman W273 нет никаких эквалайзеров в принципе. ... Недовольных этим параметром точно не будет. Звукоизоляция. К четвертому поколению серии W инженеры Сони наконец-то добились этого! Скрыть')

        self.assertEquals(serp['sn'][49]['d'], 'vk.com')
        self.assertEquals(serp['sn'][49]['u'], 'https://vk.com/topic-35092860_28777272')
        self.assertEquals(serp['sn'][49]['t'], u'компьютер не "видит" плеер |  Sony NWZ-E463 / NWZ-E464...')
        self.assertEquals(serp['sn'][49]['s'], u'Последнее время массово компьютеры перестают видеть плееры от сони, вся проблемА в прошивке у плеера, но так как на большинстве моделей плееров она не переустанавливается то проблема актуальна. Какого-то конкретного способа для приведения плеера в "чувства" пока не найдено. Ниже выкладываю переписку решения такой проблемы, может кому-то поможет (для просмотра: поделиться>загрузить оригинал на диск). И да, все действия с плеером вы делаете на свой страх и риск!!! Скрыть')

    def test42(self):
        html = self.get_data('2016-12-22.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], None)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'e-katalog.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://www.e-katalog.ru/SAMSUNG-GALAXY-S2.htm')
        self.assertEquals(serp['sn'][0]['t'], u'Samsung Galaxy S2 – купить мобильный телефон, сравнение цен...')
        self.assertEquals(serp['sn'][0]['s'], u'Закрыть. Шапка. Samsung Galaxy S2. Диагональ дисплея:4.3. "Стандарты:3G. ... Быстро привык к оболочке Самсунга. Хорошая цена. Беспокоит Андроид - вопросы постоянных прошивок и прочий геммор, при поддержке Самса - это реализовано не совсем идеально. Может стоит подождать 4го Андройда если Вы планируете купить Galaxy S2 (мой совет). Размер телефона вроде и не особо большой, но после моего Gio S5660 кажется лопатой. Эконом Мобайл: пользуюсь Samsung Galaxy S2 несколько месяцев. Комментарии 3. Обсудить. Телефон стоит своих денег однозначно!!!Хотя скоро думаю цена упадет еще немного. 23 июля 2011 #. Продал свой айфон 4 , и купил гэлакси.Считаю самым продуманным своим решение... Скрыть')

        self.assertEquals(serp['sn'][49]['d'], '1galaxy.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://www.1galaxy.ru/mobilnye-ustrojstva/')
        self.assertEquals(serp['sn'][49]['t'], u'Мобильные устройства Samsung Galaxy')
        self.assertEquals(serp['sn'][49]['s'], u'Новый флагман Samsung - Galaxy S7 Edge. Высокотехнологичный дизайн, покрытие 2,5 D Очень стильный и удобный смартфон с невероятно тонким корпусом. Samsung предлагает несколько цветов для вашего корпуса. Классический чёрный, белый, серебреный и золотой. - Операционная система&nbs.. 59 990 р. Без НДС: сравнение. Смартфон Samsung Galaxy S7 Edge SM-G935 32 Гб Синий коралл (SM-G935FZBUSER). Новый флагман Samsung - Galaxy S7 Edge. Скрыть')

    def test43(self):
        html = self.get_data('2016-12-27.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 7000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'bash-news.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://bash-news.ru/84437-forvard-salavata-yulaeva-kaprizov-hochet-letom-perebratsya-za-okean.html')
        self.assertEquals(serp['sn'][0]['t'], u'Форвард «Салавата Юлаева» Капризов хочет летом...')
        self.assertEquals(serp['sn'][0]['s'], u'Медиа: Фото: IIHF. Одной из главных звезд в составе сборной России на молодежном чемпионате мира, который стартует сегодня в канадском Торонто...')

        self.assertEquals(serp['sn'][49]['d'], 'bp01.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://www.bp01.ru/public.php?public=3904')
        self.assertEquals(serp['sn'][49]['t'], u'Ежемесячный журнал «Бельские Просторы»')
        self.assertEquals(serp['sn'][49]['s'], u'Твой дядя Хайрулла Кульмухаметов, опрашивая старых людей ещё в 50-х годах, установил, что ваш род восходит к Салавату Юлаеву.')

    def test44(self):
        html = self.get_data('2016-12-27-1.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 38000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'gazeta.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://www.gazeta.ru/auto/2013/09/02_a_5619521.shtml')
        self.assertEquals(serp['sn'][0]['t'], u'Первые номера новой серии 777 в Москве выдали...')
        self.assertEquals(serp['sn'][0]['s'], u'Внимание московских автомобилистов оказалось приковано к новым номерам с кодом региона 777, выдачу которых столичная ГИБДД начала на прошлой неделе.')

        self.assertEquals(serp['sn'][49]['d'], 'motustrans.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://www.MotusTrans.ru/regions/')
        self.assertEquals(serp['sn'][49]['t'], u'Автомобильные коды регионов России. Номера регионов.')
        self.assertEquals(serp['sn'][49]['s'], u'20 Код региона Чеченская Республика (старые номера). ... 49 Код региона Магаданская область. 177 Код региона г. Москва (также 77, 97, 99, 197, 777).')


    def test45(self):
        html = self.get_data('2017-01-20.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 57000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'youtube.com')
        self.assertEquals(serp['sn'][0]['u'], 'https://www.youtube.com/watch?v=nxgNQZ4kSzA')
        self.assertEquals(serp['sn'][0]['t'], u'как сделать лего двигатель | мистер LEGO - YouTube')
        self.assertEquals(serp['sn'][0]['s'], u'Всем привет! в этом видео я покажу вам как сделать лего двигатель.')

        self.assertEquals(serp['sn'][21]['d'], 'chinimavto.ru')
        self.assertEquals(serp['sn'][21]['u'], 'http://chinimavto.ru/show/VvNiyyEFIz4/kak_sdelat_mashinu_iz_lego_s_motorom.html')
        self.assertEquals(serp['sn'][21]['t'], u'Как сделать машину из лего с мотором.')
        self.assertEquals(serp['sn'][21]['s'], u'► Lego-самоделки #8. Лего машина на радиоуправлении. +Power Functions. ... PrototypeNo97. ► Первый в мире вечный двигатель из ЛЕГО!! Канал Пудры. ► Как сделать самую быструю машину из лего техник на пульте управления.')
        self.assertTrue(serp['sn'][21]['i'])

        self.assertEquals(serp['sn'][23]['d'], 'prigotovit.org')
        self.assertEquals(serp['sn'][23]['u'], 'http://prigotovit.org/show/KR5oZWEVBRc/kak_sdelat_lego_motor.html')
        self.assertEquals(serp['sn'][23]['t'], u'Как сделать лего мотор. Как приготовить?')
        self.assertEquals(serp['sn'][23]['s'], u'Как сделать лего мотор. Похожие видео. ► How To Make A Custom 9V Lego Motor. Multidomar. ... мистер John. ► Вечный двигатель из Лего конструктора. Mr. kriper. ► как сделать двигатель из LEGO. Тюнинг_ ММ_TV.')
        self.assertTrue(serp['sn'][23]['i'])

        self.assertEquals(serp['sn'][49]['d'], 'stiralka2.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://stiralka2.ru/sxuZdCZGM2w/kak_sdelat_dvigatel_iz_lego.html')
        self.assertEquals(serp['sn'][49]['t'], u'как сделать двигатель из LEGO. Стиральные машины')
        self.assertEquals(serp['sn'][49]['s'], u'► как сделать лего двигатель | мистер LEGO. ... ► Лего Техник 42007 Кроссовый мотоцикл, обзор на русском языке (Lego Technic 42007 MOTO CROSS BIKE).')

    def test46(self):
        html = self.get_data('2017-01-20-1.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 83000000)
        self.assertEquals(len(serp['sn']), 10)

        self.assertEquals(serp['sn'][0]['d'], 'svyaznoy.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://www.svyaznoy.ru/catalog/phone/225/apple/iphone-7')
        self.assertEquals(serp['sn'][0]['t'], u'Смартфон Apple iPhone 7 цена, купить Айфон 7 в Москве...')
        self.assertEquals(serp['sn'][0]['s'], u'В интернет магазине Связной телефоны Эпл Айфон 7 в наличии и сравнительно недорого: цены от 55 990 руб. Здесь Вы можете купить Apple iPhone 7 в Москве...')

        self.assertEquals(serp['sn'][9]['d'], 'cifrus.ru')
        self.assertEquals(serp['sn'][9]['u'], 'http://www.cifrus.ru/catalog/smartfony/apple/iphone-7')
        self.assertEquals(serp['sn'][9]['t'], u'Купить смартфон Apple iPhone 7 – все модели, цены...')
        self.assertEquals(serp['sn'][9]['s'], u'Купить смартфон Apple iPhone 7 в интернет-магазине Цифрус по лучшей цене. ... Есть возможность купить смартфон Эпл Айфон 7 в кредит.')

    def test47(self):
        html = self.get_data('2017-01-20-2.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 43000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'chtooznachaet.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://ChtoOznachaet.ru/vyrazhenie_zhi_est.html')
        self.assertEquals(serp['sn'][0]['t'], u'Что означает выражение «жи есть»')
        self.assertEquals(serp['sn'][0]['s'], u'В больших городах России часто можно услышать в разговоре слова, заимствованные из языков народов кавказской национальности. Если к англоязычным словам по типу «девайс» или «аутсорсинг» привыкают быстро...')

        self.assertEquals(serp['sn'][49]['d'], 'privatelife.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://www.privatelife.ru/2005/cg05/n12/4.html')
        self.assertEquals(serp['sn'][49]['t'], u'Сто косичек для бога Джа')
        self.assertEquals(serp['sn'][49]['s'], u'...(умер в 1975 году), короновавшийся под именем Хайле Селассие I, что в переводе с эфиопского означает «власть ... У растафари, как и у всех верующих людей, есть свои заповеди, которые они всегда соблюдают согласно воле великого бога Джа')

    def test48(self):
        html = self.get_data('2017-01-23.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 58000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'samelectrik.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://samelectrik.ru/kakie-byvayut-kabelnye-mufty.html')
        self.assertEquals(serp['sn'][0]['t'], u'Какие бывают кабельные муфты?')
        self.assertEquals(serp['sn'][0]['s'], u'Классификация и назначение кабельных муфт. Узнайте, какие существуют соединители для проводов и для чего используется каждый отдельный вид.')

        self.assertEquals(serp['sn'][49]['d'], 'elox-prom.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://www.elox-prom.ru/production/kabelnye-mufty/soedinitelnye-mufty-str-kzp/')
        self.assertEquals(serp['sn'][49]['t'], u'Соединительные кабельные термоусаживаемые муфты...')
        self.assertEquals(serp['sn'][49]['s'], u'Муфта соединительная кабельная ELOX (СтР-КзП) - состав комплекта: 1.1. Электрический соединитель.')

    def test49(self):
        u"""игнорим почтовые индексы"""
        html = self.get_data('2017-01-23-1.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 19000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'port3.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://www.PORT3.ru/info/KAGER/841428')
        self.assertEquals(serp['sn'][0]['t'], u'84-1428 Пружина ходовой части KAGER - описание, фото...')
        self.assertEquals(serp['sn'][0]['s'], u'Аналоги KAGER 841428')

        self.assertEquals(serp['sn'][49]['d'], 'voloton.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://voloton.ru/price/HYUNDAI/841428D400')
        self.assertEquals(serp['sn'][49]['t'], u'Купить HYUNDAI 841428D400, цены, доставка, наличие')
        self.assertEquals(serp['sn'][49]['s'], u'Купить от компании HYUNDAI 841428D400. Во всех магазинах города Санкт-Петербург и Москва.')

    def test50(self):
        u"""игнорим конвертер единиц"""
        html = self.get_data('2017-01-23-2.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 34000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'inmaks.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://inmaks.ru/auxpage_tablica-santimetry-djujmy/')
        self.assertEquals(serp['sn'][0]['t'], u'Tаблица (сантиметры дюймы) ― Инмакс')
        self.assertEquals(serp['sn'][0]['s'], u'Мы решили составить еще одну таблицу сантиметры – дюймы. Один сантиметр, это 0,3937007874015748 дюйма, округляем и получаем, что в одном сантиметре – 0,4 дюйма.')

        self.assertEquals(serp['sn'][49]['d'], 'snowboarding.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://www.snowboarding.ru/content/view/35/0')
        self.assertEquals(serp['sn'][49]['t'], u'Snowboarding.ru - Как определить размер ноги?')
        self.assertEquals(serp['sn'][49]['s'], u'Как измерить свою ногу · Измерять можно и в сантиметрах, и в дюймах. Для перевода дюймов в сантиметры, просто умножь на 2,54; · Сядь, поставь ногу на лист бумаги; · Обведи карандашом свою стопу...')

    def test51(self):
        html = self.get_data('context-2017-02-27.html')

        parser = YandexParser(html)
        serp = parser.get_context_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 11)

        self.assertEquals(serp['sn'][0]['t'], u'Купить столы для кухни и комнат! - Огромный выбор столов')
        self.assertEquals(serp['sn'][0]['vu'], u'lifemebel.ru/Купить-стол-на-кухню')
        self.assertEquals(serp['sn'][0]['u'], 'http://yabs.yandex.ru/count/UkhWMQ_3fYy40000gO10ZhXnGei5XPpGBfK1cmDkGxS198Ywmn-W0ucooXZC1PXddQ8_B0IcEOgzUgD80zopke6g1BstXQHs0wekfQju50Iygud30eq1tG7Ua2JqzBkLPUqFaRe_00q5b_1zAPeMxUSU3PE53Pa5GeoODQIsb4CnjPY_AQ2ZTKS1hvWrfBEOG5EqcByfsQDrHm7Qc41Jb9o35AUTPpEei41PSmUai00000QkxQs0S5urvS6n0RAa40m2-UsjW71UDUN1kQ8_B0IxxG2VILfOekB1__________yFml5DvzCMymE82CMF3zC2xW7R_tmr2Xs_W6K1tuKDvP3oA-s3AFN9UmCBsAtsqeC3cIwOL7mX?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB')
        self.assertEquals(serp['sn'][0]['a'], 't')

        self.assertEquals(serp['sn'][1]['t'], u'HOFF.ru - Купите Стол 1690 руб. / hoff.ru')
        self.assertEquals(serp['sn'][1]['vu'], u'hoff.ru/купить-стол-недорого')
        self.assertEquals(serp['sn'][1]['u'], 'http://yabs.yandex.ru/count/UkhWMIjPhzq40000gO10ZhXnGei5XPpGBfK1cmDkGxS193A8keNf8069juYl_0AOPvsk-CW8fX6Ak21PrGVSkHJJaWczke1RaWQgBgMhXmiAlANRkmcD0Tq1tf0az96wFm0D1PVmVIcQ5ktd7WsJXGsP1KACctoTjf0_BxMG2YYWbHBmhvjydREG2Jsqa0eesPKIyDgG2JsKb_OOfvc6DQYmG5bp1wIm00001gxjhO1mNZNbmR41igGG30BvxQs0S5urvS6vhlZ82Blj09z9MbYYui7__________m_2yKtdqnRp0uW8nOyFqmBk0Tl_V3KA7R-0PG7VXGtbaF8hxOCezSbx0mlOhVRIWmEPBfXKVI00?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB')
        self.assertEquals(serp['sn'][1]['a'], 't')

        self.assertEquals(serp['sn'][2]['t'], u'Купите стол фабрики СТОЛПЛИТ')
        self.assertEquals(serp['sn'][2]['vu'], u'stolplit.ru/купить стол')
        self.assertEquals(serp['sn'][2]['u'], 'http://yabs.yandex.ru/count/UkhWMRzAIi040000gO10ZhXnGei5XPpGBfK2cmHkGxS2BG68lHIF40E9g8_TW9XddPM25wOmYh57d9u9tBNw3FCAlQwqJhYgBgMhdqa2lAzFo0AD0Tq1tf0az96wFm0D1PVmVIcQ5ktd7WsJXGsP1KACc-fwjf3W9BMGG1-WbQMPhvlgUhEG42Uqa40VsPqzYzgOPYEKaNFZfvlJ3wYmG5bp1wIm00001gxjhO1mNZNbmR41igoH30BvxQs0S5urvS6vbO8Nk-q0dqbQMABYmV__________3yBnJUVJ5lC3Y0Z5Zm_J0ku1s_zyDGeTlu1b0T-53UMGyYljWoZroNi32zYjzjA30vakc5Hv8000?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB')
        self.assertEquals(serp['sn'][2]['a'], 'r')

        self.assertEquals(serp['sn'][10]['t'], u'Купите дизайнерский стол WESTWING')
        self.assertEquals(serp['sn'][10]['vu'], u'westwing.ru/Уникальные-скидки')
        self.assertEquals(serp['sn'][10]['u'], 'http://yabs.yandex.ru/count/UkhWMLBcX5q40000gO10ZhXnGei5XPpGBfK2cmLkGxS2BG4v0OYom93m0ucX8rUgc6UTfh2m2QO-YhilREiCtBtn5DWDlRrIbmS9gYwbhFac3RolMDq9ZG7T0TwG9FIHkZy03GMNy7qfcXRjvnuDauKDcGL2Z9KiBBQOG0sra3iBe9ZvCA-LB2opc7CCj90x2zcT6KRQcD8Hb9Fs2wUHNmkei41PSmUai00000QkxQs0S5urvS6n0RAyC0m2GFdjhO1mNZNbmRcciB09k-q0dqbQMABYmV__________3yBnJUVJ5lC3Y0Z5Zm_J0ku1s_zyDGeTlu1b0T-53UMGyYljWoZroNi32zYjzjA30vakc5H_8000?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB')
        self.assertEquals(serp['sn'][10]['a'], 'r')

    def test52(self):
        html = self.get_data('context-2017-02-27-1.html')

        parser = YandexParser(html)
        serp = parser.get_context_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 5)

        self.assertEquals(serp['sn'][0]['t'], u'Купите участок на Луне! Недорого! - Официальная продажа!')
        self.assertEquals(serp['sn'][0]['vu'], u'star-kosmos.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://yabs.yandex.ru/count/9rhZMIjJ9qu40000gO10Zh1_Gui5XPpGBfK1cm9kGxS198Ypi2d118c_QYuH0vX4dQhk91EcIugoUWus0zozmoMG1Bs-ws5b0wekfQzHoWIyhE6f0uq1tG7Ua2JqaRfY7Pe1b_1zAPeMxUSU3PE53Pa5GeoODYksdFOCjPZy2g2OYiolc3OhivW0DBIO_0hPc8hCsfW0D9IMdXodcSS_gB7J_mi4fB000006hkPm0cobTYN2iG6oj1000a3vvd02RALs9SAvgkua4xlj09z9MbYYui7__________m_2-fl6TV21syG1nOyFqmBk0Tl_V3KA7R-0PG7VXGtbaF8hxOCezTiPSETaS0BstKHLgJwOL7uW?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D0%BB%D1%83%D0%BD%D1%83')
        self.assertEquals(serp['sn'][0]['a'], 't')

        self.assertEquals(serp['sn'][1]['t'], u'Хотите купить луну? - Распродажа участков на луне!')
        self.assertEquals(serp['sn'][1]['vu'], u'moon-sale.com')
        self.assertEquals(serp['sn'][1]['u'], 'http://yabs.yandex.ru/count/9rhZMPTlnAe40000gO10Zh1_Gui5XPpGBfK1cm9kGxS193A8hssDW8c_YWyp19X4dQL3vmkc1ugevRXTtAQOK8AzgoDwWAekfQUnnm6D0Tq1tf0az96wOXsQ0PVmVIcQ5ktd7WsJXGsP1KACa4aHjfWl1RMGPGIWa4aHhv194REGPGIqa6K4sP194TgGPGIKaiOQfvgPBQYbg-CSfB000006hkPm0cobTYN2iG6oj1000a3vvd02RALs9SAvfKFd2xlj09z9MbYYui7__________m_2-fl6TV21syG1qmBk0Tl_V3KA7R-0PG7VXGtbaF8hxOCezTiPSETaS0BstKHLgJwOL7eV?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D0%BB%D1%83%D0%BD%D1%83')
        self.assertEquals(serp['sn'][1]['a'], 't')

        self.assertEquals(serp['sn'][2]['t'], u'DFC Luna / alterprice.ru')
        self.assertEquals(serp['sn'][2]['vu'], u'alterprice.ru')
        self.assertEquals(serp['sn'][2]['u'], 'http://yabs.yandex.ru/count/9rhZMOm2ANm40000gO10Zh1_Gui5XPpGBfK2cm5kGxS2BG68hDEEy8ccOdK4c5-TgLP25QOEYhGrdKiDtBpxoIyElRd1R389gYwbh1DY3RoaiNqAZG7T0TwG9FIHkc8TcW6Ny7qfcXRjvnuDauKDcGL2Z9FD1BQSS06rc3W1e9262w-JpGIpaEu2j9Wu0TcGXWlQaEu2b9G3rQUVYWEegLiB3QIm00001gxcS09ifNObmh41ihGn0090-UPm0cobTYN2kQbMGXMxxG2VILfOekB1__________yFmlgRndNmWTl40TC2xW7R_tmr2Xs_W6K1tuKDvP3oA-s3AFNR6N3dP702zjr4LQa-c5Hv8000?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D0%BB%D1%83%D0%BD%D1%83')
        self.assertEquals(serp['sn'][2]['a'], 'b')

        self.assertEquals(serp['sn'][3]['t'], u'Молокоотсос электрический Luna! / akusherstvo.ru')
        self.assertEquals(serp['sn'][3]['vu'], u'akusherstvo.ru')
        self.assertEquals(serp['sn'][3]['u'], 'http://yabs.yandex.ru/count/9rhZMKZxHfG40000gO10Zh1_Gui5XPpGBfK2cm5kGxS2BG4oYAlk0FA9fus_O9Y2ivsLcHYc3egtiB4z1ToyhZBn1hsyHxxp1AekfQXq_WUyexEV18q1tG7Ua2JqaRfY7Pe1b_1zAPeMxUSU3PE53Pa5GeoOf0Ysd9S2jPWo0g2Ja0glcAG8ivYl0hIOCWBPav0AsfYl0fIIiygddOi1gBcJLaW7fB000006hkPm0cobTYN2iG6oj1400a3vvd02RALs9SAvbPaOk-q0dqbQMABYmV__________3yBwcyPry87Rn0740SMF3zC2xW7R_tmr2Xs_W6K1tuKDvP3oA-s3AFNR6N3dP702zjr4LQa-c5H_8000?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D0%BB%D1%83%D0%BD%D1%83')
        self.assertEquals(serp['sn'][3]['a'], 'b')

        self.assertEquals(serp['sn'][4]['t'], u'Купить выгодно и удобно в OZON.ru / ozon.ru')
        self.assertEquals(serp['sn'][4]['vu'], u'ozon.ru/Купить')
        self.assertEquals(serp['sn'][4]['u'], 'http://yabs.yandex.ru/count/9rhZMGOTKDi40000gO10Zh1_Gui5XPpGBfK2cm5kGxS2BG4pYB1E6041YRVz4Vi5c5-TWZEc3ug-hEBV2DosWOKg2hsxuMlj1gekfQJmT0gyfS821eq1tG7Ua2JqaRfY7Pe1b_1zAPeMxUSU3O-xbHwO1v-uWze62fE53Pa5GeoGmmMscBe1jP1t0Q2GpnolaCC5iv1J1xIGTm7PaCySsf1J1vIPnfgda582gB10MNC7fB000006hkPm0cobTYN2iG6oj1400a3vvd02RALs9SAvWZExxG2VILfOekB1__________yFmlgRndNmWTl40SMF3zC2xW7R_tmr2Xs_W6K1tuKDvP3oA-s3AFNR6N3dP702zjr4LQa-c5Hu8W00?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D0%BB%D1%83%D0%BD%D1%83')
        self.assertEquals(serp['sn'][4]['a'], 'b')

    def test53(self):
        html = self.get_data('context-2017-02-27-2.html')

        parser = YandexParser(html)
        serp = parser.get_context_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 7)

    def test54(self):
        html = self.get_data('context-2017-02-28.html')

        parser = YandexParser(html)
        serp = parser.get_context_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 7)

        self.assertEquals(serp['sn'][0]['t'], u'Стандартные пластиковые окна! – Скидка 20%!')
        self.assertEquals(serp['sn'][0]['vu'], u'oknaforbis.ru/Пластиковые-Окна')
        self.assertEquals(serp['sn'][0]['u'], 'http://yabs.yandex.ru/count/Jy3pEMwPIHu40000ZhcYLOi5KfK1cm9kGxS198Yz8PtX0ecpyWhT19YD59sblyWEfYsAlpiCr0hSjdGs_GkziJaJ_mUgBgMjZfWBlAMjXGkD0Tq1tf0az96_JpkO3vVmVIcQ5ktd7WsJXGsYP9a5GeohNaK3jf0s-xMGvDIWg23E1A-hNaK3iwY-E06qaEJKsQWWpWJQgBuu0PIOInIdaHGqgBd13Ue3fC00002H0QxYSS9fqf1unh41igGG00Bvud72QTAGUCQvfR_83hlmiNz0VmaLkWV1__________yFmlE7lN0Dx9rw2SMF3zB__________m_J__________yFxW7RyF7OiuO95Re7tuKDvP3oA-s3AFNVnAHH9t42zjA7u6zJcLHy8m00?q=%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D1%8B%D0%B5+%D0%BF%D0%BB%D0%B0%D1%81%D1%82%D0%B8%D0%BA%D0%BE%D0%B2%D1%8B%D0%B5+%D0%BE%D0%BA%D0%BD%D0%B0+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%80%D1%8B')
        self.assertEquals(serp['sn'][0]['a'], 't')

        self.assertEquals(serp['sn'][1]['t'], u'Стандартные окна ПВХ / shop.oknagorizont.ru')
        self.assertEquals(serp['sn'][1]['vu'], u'shop.oknagorizont.ru')
        self.assertEquals(serp['sn'][1]['u'], 'http://yabs.yandex.ru/count/Jy3pELmzLaG40000ZhcYLOi5KfK1cm9kGxS193A8lDC0m0I9fYSeVvYD59sap-e1fakAfU99GDoX-fLKlQPvbLIgBgMlRvW1ZG7T0TwG9FJqjuIujGcHlqyxc0-Ny7qfcXRjvnuDauKDecIP1KACe2eo0xQGS_Mra0BGeAtwPWEle2eo0xEORzsqa0BGsQtwPWFQc6_Tb9Yn4wUPq32egzg2UAJ00000aG6kud72QTAGUCQn0RAa4002-U9nmcdIa7Z6kQJFwW6xyB5_G7y95Re7mV__________3yBpXxrm3UoTUWd5Zm_I__________yFq___________3-u1s_3nsBE62HMw1z-53UMGyYljWoZrtyIaKITn0lRIX-1lKvbKVo80?q=%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D1%8B%D0%B5+%D0%BF%D0%BB%D0%B0%D1%81%D1%82%D0%B8%D0%BA%D0%BE%D0%B2%D1%8B%D0%B5+%D0%BE%D0%BA%D0%BD%D0%B0+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%80%D1%8B')
        self.assertEquals(serp['sn'][1]['a'], 't')

        self.assertEquals(serp['sn'][2]['t'], u'Пластиковые окна Железнодорожный / ecoplastika.ru')
        self.assertEquals(serp['sn'][2]['vu'], u'ecoplastika.ru/Пластиковые-окна')
        self.assertEquals(serp['sn'][2]['u'], 'http://yabs.yandex.ru/count/Jy3pEVKEk5040000ZhcYLOi5KfK1cm9kGxS193E8lilZPWQ9ziqk1j6SPciBc8qKdQcebn6Qj58qMmAcQegiWAVvtBb2VM01lRNTE3a1gYwbhH8G0uq1tG7Ua2JqaRzFEvWFb_1zAPeMxUSU3PE53Q9acGL2ZAt1ImUsh5Cm0hMesje1eAZHaWUlhS5B1xEew-m1jAZQsW7Pg4Th2Tge2MK2b9TN0gUJ5nQefBU13gJ00000aG6kud72QTAGUCQn0xAa4002-U9nmcdIa7Z6kQcebn6xyB5_G7y95Re7mV__________3yBpXxrm3UoTUWd40SMF3zB__________m_J__________yFxW7RyF7OiuO95Re7tuKDyWxbaF8hxOCezT_4f54dSGBsqeVWRrEPL7ya?q=%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D1%8B%D0%B5+%D0%BF%D0%BB%D0%B0%D1%81%D1%82%D0%B8%D0%BA%D0%BE%D0%B2%D1%8B%D0%B5+%D0%BE%D0%BA%D0%BD%D0%B0+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%80%D1%8B')
        self.assertEquals(serp['sn'][2]['a'], 't')

        self.assertEquals(serp['sn'][3]['t'], u'Пластиковые окна. Цена: 2190 руб. – Дешевле нет!')
        self.assertEquals(serp['sn'][3]['vu'], u'nedorogieokna.ru/недорого-в-москве')
        self.assertEquals(serp['sn'][3]['u'], 'http://yabs.yandex.ru/count/Jy3pEJfXJOq40000ZhcYLOi5KfK2cm5kGxS2BG68jcS-80A9j4UdtmAOZHITeMCs5QOXYhYBKSi4tBcxqeS6lRx97Ra3gYwbgyZl1BoWKjK2ZG7T0TwG9FIHlqyxc0-Ny7qfcXRjvnuDZx6ZlGa5dxucnYuCauKDecIP1KACg50g1RQiiOm1jQWkK06We6421g-eK2e5iw0TXm6qg2vG0Tch8fK8sg2OBWAKdQwifv7c1wY_S1hW1AJ00000aG6kud72QTAGUCQn0RAq4G02GFdYSS9fqf1unhcXOpOLk_2nVq1_2HMw1y7__________m_2yuUzS0tidNe9nOyFql__________3zF__________m_k0TlmyTYpXWaLkWVVXGtbaF8hxOCezT_4f54dSGBsqeVWRrEPL7qb?q=%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D1%8B%D0%B5+%D0%BF%D0%BB%D0%B0%D1%81%D1%82%D0%B8%D0%BA%D0%BE%D0%B2%D1%8B%D0%B5+%D0%BE%D0%BA%D0%BD%D0%B0+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%80%D1%8B')
        self.assertEquals(serp['sn'][3]['a'], 'b')

        self.assertEquals(serp['sn'][4]['t'], u'Пластиковые окна "Rehau" / zavod.dom-okon.su')
        self.assertEquals(serp['sn'][4]['vu'], u'zavod.dom-okon.su/Окна-Домком-Москва')
        self.assertEquals(serp['sn'][4]['u'], 'http://yabs.yandex.ru/count/Jy3pEQdII_S40000ZhcYLOi5KfK2cm5kGxS2BG4oYBlMZ904YQ9C46oTghuz3gP8Yhn9wbyDtB9bia4ElRWZFpm9gYwbh5ro3RoZv1m4ZG7T0TwG9FIHlqyxc0-Ny7qfcXRjvnuDZx6ZlGa5dxucnYuCauKDecIP1KACfKEM1hQWuVa1jQ2sh06We5vj1w-bGvO6iw1cum6qeBQi0TcWhxO3sf2pyPIVsAgdcsu5gB10MNC7fC00002H0QxYSS9fqf1unh41ihGH0090-U9nmcdIa7Z6kQg-FGwxyB5_G7y95Re7mV__________3yBpXxrm3UoTUWd5Zm_I__________yFq___________3-u1s_3nsBE62HMw1z-53UMGyYljWoZrtyIaKITn0lRIX-1lKvbKUIK0?q=%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D1%8B%D0%B5+%D0%BF%D0%BB%D0%B0%D1%81%D1%82%D0%B8%D0%BA%D0%BE%D0%B2%D1%8B%D0%B5+%D0%BE%D0%BA%D0%BD%D0%B0+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%80%D1%8B')
        self.assertEquals(serp['sn'][4]['a'], 'b')

        self.assertEquals(serp['sn'][5]['t'], u'Пластиковые окна. Цены 2015! – Скидка 50% +подарок!')
        self.assertEquals(serp['sn'][5]['vu'], u'eurookna.ru')
        self.assertEquals(serp['sn'][5]['u'], 'http://yabs.yandex.ru/count/Jy3pEIScVe840000ZhcYLOi5KfK2cm5kGxS2BG4pYBQgNS01YRCw0I83c8qKdP132wORYhl8Mcq9tBCScSOAlRULcxe3gYwbe3vz1hohlra4ZG7T0TwG9FIHlqyxc0-Ny7qfcXRjvnuDZx6ZlGa5dxucnYuCauKDecIP1KAChH271BQak5i1jQYj9W6WfTV61Q-j48S4iw3wTm6qgAqc0TcbryO5sg3wTm6KdqMyfvsh2QYmFN0S0gJ00000aG6kud72QTAGUCQn0RAq4G02GFdYSS9fqf1unhcGGmkxyB5_G7y95Re7mV__________3yBpXxrm3UoTUWd40SMF3zB__________m_J__________yFxW7RyF7OiuO95Re7tuKDvP3oA-s3AFNVnAHH9t42zjA7u6zJcLH-9G00?q=%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D1%8B%D0%B5+%D0%BF%D0%BB%D0%B0%D1%81%D1%82%D0%B8%D0%BA%D0%BE%D0%B2%D1%8B%D0%B5+%D0%BE%D0%BA%D0%BD%D0%B0+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%80%D1%8B')
        self.assertEquals(serp['sn'][5]['a'], 'b')

        self.assertEquals(serp['sn'][6]['t'], u'Окна ПВХ оп заводским ценам! / zavodskieokna.ru')
        self.assertEquals(serp['sn'][6]['vu'], u'zavodskieokna.ru')
        self.assertEquals(serp['sn'][6]['u'], 'http://yabs.yandex.ru/count/Jy3pERat9NO40000ZhcYLOi5KfK2cm5kGxS2BG4qYBv6Bp02YRJ9QwS3c8qKdQSZyGEc8egvdcg81Dor5ay_1hsqhSf-1AekfQR3OWUD0Tq1tf0az96_JpkO3vVmVIcQ5ktd7WsJXGsYP9a5GeoeQcO4jgpiKG6rg60U0Q2jkjS4hwXgPWIpg2yx0RIeO1u1sQswrmJQg2yx0PIMMkUdaHiAgA7PBcgam0000941hk9nmcdIa7Z6iG6of1400ldYSS9fqf1unhcd8_43k_2nVq1_2HMw1y7__________m_2yuUzS0tidNe9n075Zm_I__________yFq___________3-u1s_3nsBE62HMw1z-53UMGyYljWoZrtyIaKITn0lRIX-1lKvbKVIC0?q=%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D1%8B%D0%B5+%D0%BF%D0%BB%D0%B0%D1%81%D1%82%D0%B8%D0%BA%D0%BE%D0%B2%D1%8B%D0%B5+%D0%BE%D0%BA%D0%BD%D0%B0+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%80%D1%8B')
        self.assertEquals(serp['sn'][6]['a'], 'b')

    def test55(self):
        html = self.get_data('context-2017-02-28-1.html')

        parser = YandexParser(html)
        serp = parser.get_context_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 7)

        self.assertEquals(serp['sn'][0]['t'], u'Купить стол-трансформер в Москве! - От 2 600 р!')
        self.assertEquals(serp['sn'][0]['vu'], u'lifemebel.ru/Столы-Трансформеры')
        self.assertEquals(serp['sn'][0]['u'], 'http://yabs.yandex.ru/count/JuWipDY16VW40000ZhptLOi5XPpGBfK1cm9kGxS198YsjpKW0ecyAN6X0fXddQ8_B0Ic8OgwBaXt0jozYWwA0xs-2jIt0gekfQczJ0Mygud30eq1tG7Ua2JqzBloK6KDaRXM_m0Ab_0umHCMxUSU3PE53Pa5GeoT9LssdF4RjPYk5w2LrdoldILTiv2z7xIOhXVPbTPysf2z7vIP91UdcgDHgB10MNC7fB000006hksbG39uuup6iG6of1000ldjfK0oUEECnhcYFom4k-q0dqbQMABYmV__________3yB-HDt4xDEPsWR5Zm_J0ku1s_zyDGeTlu1b0T-53UMGyYljWoZroIGprD6bzjJnYOHOcLH_8000?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB+%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B0+%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%84%D0%BE%D1%80%D0%BC%D0%B5%D1%80')
        self.assertEquals(serp['sn'][0]['a'], 't')

        self.assertEquals(serp['sn'][1]['t'], u'Стол трансформер купить в Москве! / dolce-mebel.ru')
        self.assertEquals(serp['sn'][1]['vu'], u'dolce-mebel.ru/столы')
        self.assertEquals(serp['sn'][1]['u'], 'http://yabs.yandex.ru/count/JuWip9BaA-W40000ZhptLOi5XPpGBfK1cm9kGxS193A8gSjay8czJLIW19XddQ7hwX6c3egnQ8Ki1zoyHsNl2BsuqWaj1gekfQmogmcygXoR2Oq1tG7Ua2JqaRXM_m0Ab_0umHCMxUSU3PE53Pa5GeoGRLQscEqPjP3v5Q2GRLQla6rMiv3v5RIG-HNPa6rMsf3v5PIJf0cdcwTOgB50MNC7fB000006hksbG39uuup6iG6oj1000a3vxQL0CdZZZCQveUlg4Rlj09z9MbYYui7__________m_2_aJTnEpJcTe6n075Zm_J0ku1s_zyDGeTlu1b0T-53UMGyYljWoZroIGprD6bzjJnYOHOcLHy8000?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB+%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B0+%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%84%D0%BE%D1%80%D0%BC%D0%B5%D1%80')
        self.assertEquals(serp['sn'][1]['a'], 't')

        self.assertEquals(serp['sn'][2]['t'], u'HOFF.ru - Купите Стол 1690 руб. / hoff.ru')
        self.assertEquals(serp['sn'][2]['vu'], u'hoff.ru/столы-трансформеры')
        self.assertEquals(serp['sn'][2]['u'], 'http://yabs.yandex.ru/count/JuWip5H6jju40000ZhptLOi5XPpGBfK1cm9kGxS193E8keNf8069ha9Q6vXddQxuo0Yc4Ogu8IRL1zo-4zEI2RsmW5kI1gekfQk72mgyfTkx2Oq1tG7Ua2JqaRXM_m0Ab_0umHCMxUSU3O-sJbYw0P-zcxzw29E53Pa5GeoJ5O-sdEmgjPXW9A2L4l2lanMFiv09FRIOO2JPbHBmsf09FPIGrWkdds4mgB10MNC7fB000006hksbG39uuup6iG6of1000ldjfK0oUEECnhck-CW8k-q0dqbQMABYmV__________3yB-HDt4xDEPsWR5Zm_J0ku1s_zyDGeTlu1b0T-53UMGyYljWoZroIGprD6bzjJnYOHOcLHz8G00?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB+%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B0+%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%84%D0%BE%D1%80%D0%BC%D0%B5%D1%80')
        self.assertEquals(serp['sn'][2]['a'], 't')

        self.assertEquals(serp['sn'][3]['t'], u'Стол трансформер для кухни купить - Производство мебели!')
        self.assertEquals(serp['sn'][3]['vu'], u'3kon.ru/Заказать-со-скидкой')
        self.assertEquals(serp['sn'][3]['u'], 'http://yabs.yandex.ru/count/JuWipFa5jJy40000ZhptLOi5XPpGBfK2cm5kGxS2BG68ilAki069zFxDMikLDsC5c6UTgmqj29grl8qM0QOQYhBmShS7tBaS4uC9lRHMOuW6gYwbe_Bt2Rohs949ZG7T0TwG9FIHk5R_00gNy3Z14nRjvnuDauKDcGL2Z9FnIRQOp1ArcCmIe90ySw-JyKcpa4mTj9ZC4jcGF7FQa4mTb9ZJowUKq1oeiK1PSmUai00000QkxQL0CdZZZCQn0xAq4G02GFdjfK0oUEECnhch3Iq8k-q0dqbQMABYmV__________3yB-HDt4xDEPsWR5Zm_J0ku1s_zyDGeTlu1b0T-53V8ExOCezSaaCzJHfVRKyOc4M9bKUo40?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB+%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B0+%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%84%D0%BE%D1%80%D0%BC%D0%B5%D1%80')
        self.assertEquals(serp['sn'][3]['a'], 'b')

        self.assertEquals(serp['sn'][4]['t'], u'Купите стол-трансформер в Москве / kresla-otido.ru')
        self.assertEquals(serp['sn'][4]['vu'], u'kresla-otido.ru/Столы-книжки')
        self.assertEquals(serp['sn'][4]['u'], 'http://yabs.yandex.ru/count/JuWip2z06u440000ZhptLOi5XPpGBfK2cm5kGxS2BG4oYB-EI002YQSEXSwOPvsOunMc7ug_XGfa1jorAEur2BssaOo-1QekfQ7LtmYyhyRV28q1tG7Ua2JqaRXM_m0Ab_0umHCMxUSU3PE53Pa5GeoRnZMsa28GjP2i3Q2RqaolcyOriv284xIGh0tPcz9Csf284vILyUYdcRmdgBKl1sy3fB000006hksbG39uuup6iG6of1400ldjfK0oUEECnhcOunMxxG2VILfOekB1__________yFmlv4tSJiqvdQ1iG1nOyFqmBk0Tl_V3KA7R-0PG7VXGtbaF8hxOCezSaaCzJHfVRKyOc4M9bKUY00?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB+%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B0+%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%84%D0%BE%D1%80%D0%BC%D0%B5%D1%80')
        self.assertEquals(serp['sn'][4]['a'], 'b')

        self.assertEquals(serp['sn'][5]['t'], u'Стол-трансформер Москва! - 87 моделей столов!')
        self.assertEquals(serp['sn'][5]['vu'], u'interpremium.ru/Столы-трансформеры')
        self.assertEquals(serp['sn'][5]['u'], 'http://yabs.yandex.ru/count/JuWip8JUT9u40000ZhptLOi5XPpGBfK2cm5kGxS2BG4pYBIZckW6YRgfEqO4c6UTgQ8R0QQC28g-b1ah1jopIs_y1xsvzmoQ1QekfQVrimYyfsYi1Oq1tG7Ua2JqzBlzP_KLaRXM_m0Ab_0umHCMxUSU3O-_Y7s90f-z7EbD3PE53Pa5GeoJvJAsd4GFjPZm3A2L-qYla-Koiv2E4hIOy0pPbVj8sf2E4fIUqysdc-4dgB50MNC7fB000006hksbG39uuup6iG6oj1400a3vxQL0CdZZZCQvgQ8R0Rlj09z9MbYYui7__________m_2_aJTnEpJcTe6nOyFqmBk0Tl_V3KA7R-0PG7VXGtbaF8hxOCezSaaCzJHfVRKyOc4M9bKVo80?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB+%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B0+%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%84%D0%BE%D1%80%D0%BC%D0%B5%D1%80')
        self.assertEquals(serp['sn'][5]['a'], 'b')

        self.assertEquals(serp['sn'][6]['t'], u'Столы-трансформеры / mnogomeb.ru')
        self.assertEquals(serp['sn'][6]['vu'], u'mnogomeb.ru')
        self.assertEquals(serp['sn'][6]['u'], 'http://yabs.yandex.ru/count/JuWip3X6zn040000ZhptLOi5XPpGBfK2cm5kGxS2BG4qYBHe3c05YRPkjf42c6UThr560gPLYhw0Xq42tB34Fa43lRPDb8O2gYwbe-m71RoisNi4ZG7T0TwG9FIHk5R_00gNy3Z14nRjvnuDauKDcGL2Z9X_FBQK9XArc64Fe9lIJA-OVpopa8WJj9XX3zcRqapQa8WJb9_wwQUGLHseiF-GQGIai00000QkxQL0CdZZZCQn0RAq4G02GFdjfK0oUEECnhclKKO2k-q0dqbQMABYmV__________3yB-HDt4xDEPsWR5Zm_J0ku1s_zyDGeTlu1b0T-53UMGyYljWoZroIGprD6bzjJnYOHOcLHy8000?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB+%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B0+%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%84%D0%BE%D1%80%D0%BC%D0%B5%D1%80')
        self.assertEquals(serp['sn'][6]['a'], 'b')

    def test56(self):
        u"""игнорим конвертер единиц"""
        html = self.get_data('2017-03-09.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 21000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'ru.wikipedia.org')
        self.assertEquals(serp['sn'][0]['u'], 'https://ru.wikipedia.org/wiki/%D0%A3%D1%8D%D1%81%D0%BA%D0%B0')
        self.assertEquals(serp['sn'][0]['t'], u'Уэска — Википедия')
        self.assertEquals(serp['sn'][0]['s'], u'Уэ́ска (исп. Huesca, араг. Uesca, лат. Osca) — город в Испании, автономное сообщество Арагон, центр одноимённой провинции. Существовала ещё в доримскую эпоху. Статус города (с названием Оска) пожаловал в 30 г. н. э. император Август.')

        self.assertEquals(serp['sn'][49]['d'], 'spanish-info.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://spanish-info.ru/ueska/')
        self.assertEquals(serp['sn'][49]['t'], u'Уэска')
        self.assertEquals(serp['sn'][49]['s'], u'Провинция Уэска знаменита тем, что здесь находятся самые высокие пики арагонских Пиренеев. Туристы специально приезжают сюда...')

    def test57(self):
        html = self.get_data('context-2017-03-31.html')

        parser = YandexParser(html)
        serp = parser.get_context_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 7)

        self.assertEquals(serp['sn'][0]['a'], 't')
        self.assertEquals(serp['sn'][1]['a'], 't')
        self.assertEquals(serp['sn'][2]['a'], 't')
        self.assertEquals(serp['sn'][3]['a'], 'b')
        self.assertEquals(serp['sn'][4]['a'], 'b')
        self.assertEquals(serp['sn'][5]['a'], 'b')
        self.assertEquals(serp['sn'][6]['a'], 'b')

    def test58(self):
        html = self.get_data('context-2017-03-31-1.html')

        parser = YandexParser(html)
        serp = parser.get_context_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 11)

        self.assertEquals(serp['sn'][0]['a'], 't')
        self.assertEquals(serp['sn'][1]['a'], 't')
        self.assertEquals(serp['sn'][2]['a'], 'r')
        self.assertEquals(serp['sn'][10]['a'], 'r')

    def test59(self):
        html = self.get_data('mobile-2017-05-16.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], None)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'hi-tech.mail.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://hi-tech.mail.ru/review/fitness_band_sony_garmin_huawei/')
        self.assertEquals(serp['sn'][0]['t'], u'Обзор фитнес-браслетов Garmin, Huawei и Sony - Hi-Tech Mail.Ru')
        self.assertEquals(serp['sn'][0]['s'], u'Читайте первую часть сводного обзора фитнес-браслетов: Polar, Jawbone, Fitbit, Nike. Huawei Talkband B1. Этот браслет был представлен публике на выставке MWC, которая прошла...')

        self.assertEquals(serp['sn'][49]['d'], 'avito.ru')
        self.assertEquals(serp['sn'][49]['u'], 'https://www.avito.ru/rossiya?sgtd=1&q=%D1%84%D0%B8%D1%82%D0%BD%D0%B5%D1%81+%D0%B1%D1%80%D0%B0%D1%81%D0%BB%D0%B5%D1%82+huawei')
        self.assertEquals(serp['sn'][49]['t'], u'фитнес браслет huawei - Доска объявлений от частных лиц...')
        self.assertEquals(serp['sn'][49]['s'], u'Продам умные часы-фитнес браслет Huawei Honor Band. 2 500 руб. Фитнес-браслет Huawei TalkBand B2. 8 000 руб. Спорт и отдых.')

    def test60(self):
        html = self.get_data('mobile-2017-05-16-1.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], None)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'svyaznoy.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://www.svyaznoy.ru/catalog/phone/224/nokia')
        self.assertEquals(serp['sn'][0]['t'], u'Купить телефоны Nokia, цены на мобильные телефоны Нокия...')
        self.assertEquals(serp['sn'][0]['s'], u'Заказать и купить телефон Nokia по низкой цене, в том числе в рассрочку, можно через наш интернет магазин - продажа сотовых телефонов Нокия осуществляется с доставкой по России - Москва.')

        self.assertEquals(serp['sn'][49]['d'], 'market.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://market.ru/category/c257-sotovye-telefony/nokia')
        self.assertEquals(serp['sn'][49]['t'], u'Мобильные телефоны Nokia цены в Москве | купить...')
        self.assertEquals(serp['sn'][49]['s'], u'Интернет магазин Маркет - низкие цены на Мобильные телефоны Nokia в Москве - отзывы, доставка, каталог, сравнение цен в магазинах города.')

    def test61(self):
        html = self.get_data('mobile-2017-05-16-2.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], None)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'svyaznoy.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://www.svyaznoy.ru/catalog/phone/224/senseit')
        self.assertEquals(serp['sn'][0]['t'], u'Купить телефоны SENSEIT, цены на мобильные телефоны...')
        self.assertEquals(serp['sn'][0]['s'], u'В нашем каталоге Вы можете подобрать сотовый телефон Сэнсит по техническим параметрам, отзывам покупателей и Главная Телефоны Все телефоны Мобильные телефоны SENSEIT.')

        self.assertEquals(serp['sn'][49]['d'], 'service-centers.ru')
        self.assertEquals(serp['sn'][49]['u'], 'https://service-centers.ru/senseit')
        self.assertEquals(serp['sn'][49]['t'], u'Сервисные центры Senseit, ремонт Senseit в Москве — полный...')
        self.assertEquals(serp['sn'][49]['s'], u'Сервисные центры Senseit. Мы нашли для вас 219 сервисных центров Senseit в Москве. Ремонт внешних аккумуляторов, мобильных телефонов Senseit.')

    def test62(self):
        html = self.get_data('2017-08-30.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 109000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'krost.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://www.krost.ru/sale/15632/')
        self.assertEquals(serp['sn'][0]['t'], u'Беспроцентная рассрочка при покупке квартиры в жилом...')
        self.assertEquals(serp['sn'][0]['s'], u'Рассрочка в жилом комплексе «Новая Звезда». ... Концерн «КРОСТ» предлагает своим клиентам воспользоваться рассрочкой платежа при покупке квартиры в жилом комплексе «Новая Звезда».')

        self.assertEquals(serp['sn'][49]['d'], 'living.papacarlostudio.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://living.papacarlostudio.ru/msk/objects/detail/zhk_novaya_zvezda_11205/')
        self.assertEquals(serp['sn'][49]['t'], u'ЖК «Новая Звезда» — купить квартиру от застройщикав...')
        self.assertEquals(serp['sn'][49]['s'], u'ЖК «Новая Звезда»- это жилой комплекс, расположенный в Северо-Западном административном округе. ... Застройщик: Крост Недвижимость. Высота зданий от 11 до 24 этажей. В комплексе предусмотрены :1к.кв., 2к.кв., 3к.кв.. В ЖК можно...')

    def test63(self):
        html = self.get_data('2017-08-30-1.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 91000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'kalkulator.pro')
        self.assertEquals(serp['sn'][0]['u'], 'http://kalkulator.pro/inches-to-centimeters.html')
        self.assertEquals(serp['sn'][0]['t'], u'Калькулятор Дюймы в Сантиметры | Сколько...')
        self.assertEquals(serp['sn'][0]['s'], u'Преобразование дюймов в сантиметры (инчи в см) и наоборот в режиме он-лайн, бесплатный сервис калькулятор.про. ... Калькулятор Дюймы в Сантиметры. Онлайн конвертер дюйм см (инч см).')

        self.assertEquals(serp['sn'][49]['d'], 'tentology.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://tentology.ru/spravka-inch-%26-foot.htm')
        self.assertEquals(serp['sn'][49]['t'], u'Дюйм в см, Чему равен дюйм и фут? Как перевести...')
        self.assertEquals(serp['sn'][49]['s'], u'Сколько сантиметров в дюйме? ... 1 дюйм = 2,54 см. 1 фут = 12 дюймов = 0,3048 метра. Обозначение. В современном русском языке общепринятого буквенного сокращения для обозначения дюймов нет.')

    def test64(self):
        html = self.get_data('2017-08-30-2.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 21000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'voda-schet.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://voda-schet.ru/')
        self.assertEquals(serp['sn'][0]['t'], u'Поверка счетчиков воды в москве и московской области')
        self.assertEquals(serp['sn'][0]['s'], u'Ваши данные не будут переданы третьим лицам. Все поля обязательны для заполнения. +7 (495) 357-30-11.')

        self.assertEquals(serp['sn'][49]['d'], 'standtel.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://standtel.ru/')
        self.assertEquals(serp['sn'][49]['t'], u'Стандарт телеком - Москва')
        self.assertEquals(serp['sn'][49]['s'], u'Оставить заявку можно на сайте, по телефону +7 (495) 357-07-07 или по почте sale@standtel.ru Стандарт Телеком — новый стандарт качества!')

    def test65(self):
        html = self.get_data('2017-08-30-3.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 63000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'mos.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://www.mos.ru/city/projects/renovation/')
        self.assertEquals(serp['sn'][0]['t'], u'Список домов, включенных в программу реновации')
        self.assertEquals(serp['sn'][0]['s'], u'Дом не включен в программу реновации. Если у вас есть вопросы, позвоните в Единую справочную службу Москвы +7 (495) 777-77-77.')

        self.assertEquals(serp['sn'][49]['d'], 'law03.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://law03.ru/news/read/renovaciya-zhilya-v-moskve-2017')
        self.assertEquals(serp['sn'][49]['t'], u'Реновация жилья в Москве 2017: последние новости')
        self.assertEquals(serp['sn'][49]['s'], u'Закон о реновации жилищного фонда в Москве был принят Мосгордумой 17 мая 2017 года. В нем закреплены дополнительные гарантии для тех граждан...')

    def test66(self):
        html = self.get_data('2017-08-30-4.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 156000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'kp.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://www.kp.ru/guide/zabolevanie-gorla-i-gortani.html')
        self.assertEquals(serp['sn'][0]['t'], u'Заболевание горла и гортани: симптомы, признаки...')
        self.assertEquals(serp['sn'][0]['s'], u'Где можно пройти обследование? МРТ горла и гортани — диагностический метод обследования ... При частых ЛОР-заболеваниях вам нужны комплексы для улучшения работы иммунной системы, а также препараты-иммуномодуляторы.')

        self.assertEquals(serp['sn'][49]['d'], 'stopparodontoz.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://StopParodontoz.ru/bolezni-gorla-i-gortani/')
        self.assertEquals(serp['sn'][49]['t'], u'Болезни горла и гортани: симптомы и лечение')
        self.assertEquals(serp['sn'][49]['s'], u'Хронические заболевания горла чаще имеют совсем другие причины ― это воспалительные заболевания носа или пищеварительного тракта. ... При первых признаках затяжного процесса в горле необходимо пройти обследование.Раннее...')

    def test67(self):
        html = self.get_data('mobile-2017-12-11.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], None)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'e-katalog.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://www.e-katalog.ru/PHILIPS-XENIUM-V387.htm')
        self.assertEquals(serp['sn'][0]['t'], u'Philips Xenium V387 – купить мобильный телефон, сравнение цен...')
        self.assertEquals(serp['sn'][0]['s'], u'Цена: от 9990 р. до 9990 р. >>> Мобильный телефон Philips Xenium V387 ✔ Купить по лучшей цене ✔ Описание, фото, видео ✔ Рейтинги, тесты, сравнение ✔ Отзывы, обсуждение пользователей. ... Гаджеты Компьютеры Офис Фото TV Аудио Бытовая техника Климат Детские товары Авто Инструмент и сад Туризм Спорт Дом Часы и украшения. Каталог / Мобильные и связь / Мобильные и аксессуары / Мобильные телефоны / Philips /. Мобильный телефон Philips Xenium V387. Где купить Описание Характеристики Отзывы 72 Обсуждение 10 Аксессуары 10+. Видео 3 Фото 7. Последняя цена: 9 990 р. Этот смартфон рассчитан прежде всего для тех, кому нужен крупный экран в сочетании с автономностью и компактностью. Скрыть')

        self.assertEquals(serp['sn'][49]['d'], '1001planshet.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://www.1001planshet.ru/kupit/smartphones/philips-xenium-v387-16gb-dual-sim-black')
        self.assertEquals(serp['sn'][49]['t'], u'Продажа смартфона Philips Xenium V387 16Gb Dual SIM Black.')
        self.assertEquals(serp['sn'][49]['s'], u'смартфон Philips Xenium V387. гарнитура. зарядное устройство. кабель питания. документация. Похожие товары. Highscreen Zera F (rev.S) Black 9 990 р. Highscreen Zera S Power Black 14 990 р. Philips Xenium I908 Black 21 990 р. ... Мы не перекупщики, поэтому у нас выгодные цены, вследствие чего с нами легко экономить! Мы продаем смартфоны и планшеты уже 5 лет! Мы настоящие Эксперты мобильной техники. Заполните форму сейчас: Ваше имя. Мобильный телефон. Специалист свяжется с вами и ответит на все вопросы! Скрыть')

    def test68(self):
        html = self.get_data('mobile-2017-12-12.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], None)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'm.avito.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://m.avito.ru/moskva/telefony?q=Samsung+galaxy+NOTE+3')
        self.assertEquals(serp['sn'][0]['t'], u'Samsung galaxy NOTE 3 - Купить мобильный телефон, смартфон...')
        self.assertEquals(serp['sn'][0]['s'], u'Samsung Galaxy Note 3 Neo SM-N7502 Duos 16Gb White. 8 000 руб. м. Площадь революции. ... Samsung galaxy note 8 64gb black черный евротест. 49 000 руб. м. Новокосино. Скрыть')

        self.assertEquals(serp['sn'][49]['d'], 'moscow-tablet.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://moscow-tablet.ru/best_tablet.php?price=1')
        self.assertEquals(serp['sn'][49]['t'], u'Планшет Самсунг Галакси Ноут 10.1 N8000 16Гб купить...')
        self.assertEquals(serp['sn'][49]['s'], u'Распродажа 2017 планшетов Samsung (самсунг) Galaxy Note 10.1 N8000 16Gb со клада в Москве. ... Планшет Samsung (самсунг) Galaxy Note 10.1 N8000 16Gb: купить, г. Москва. Цена: 16399 руб.')

    def test69(self):
        html = self.get_data('mobile-2017-12-13.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], None)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], '4pda.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://4pda.ru/forum/index.php?showtopic=654520')
        self.assertEquals(serp['sn'][0]['t'], u'[Android Wear] WatchMaker Watch Face - 4PDA | Форум')
        self.assertEquals(serp['sn'][0]['s'], u'Требуется Android: 2.3+ Поддерживаемый экран: Круглый, Квадратный Русский интерфейс: Нет. Скачать: WatchMaker Watch Face v4.6.5. Прошлые версии. версия: v4.6.4 [Android Wear] WatchMaker Watch Face (Пост Giacomino #67412238) версия: v4.6.2 [Android Wear] WatchMaker Watch Face (Пост vutak #64514188) версия: v4.4.6 [Android Wear] WatchMaker Watch Face (Пост Alex0047 #63303306) версия: v4.4.5 [Android Wear] WatchMaker Watch Face (Пост Alex0047 #63197798) версия: v4.4.4 [Android Wear] WatchMaker Watch. Скрыть')

        self.assertEquals(serp['sn'][49]['d'], 'revdl.com')
        self.assertEquals(serp['sn'][49]['u'], 'https://www.revdl.com/despicable-me-android.html/')
        self.assertEquals(serp['sn'][49]['t'], u'Minion Rush Despicable Me 5.1.0g Apk + MOD Free Purchase/Unlocked | RevDL | Download Android Apps & Games')
        self.assertEquals(serp['sn'][49]['s'], u'Direct Download Android Minion Rush Despicable Me Apk 5.1.0g + MOD (Free Purchase/Unlocked) + Data + MEGA MOD From RevDL .')

    def test70(self):
        html = self.get_data('mobile-2017-12-15.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], None)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'dns-shop.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://www.dns-shop.ru/product/21587dd97a653330/52-smartfon-elephone-s3-16-gb-seryj/')
        self.assertEquals(serp['sn'][0]['t'], u'Купить 5.2" Смартфон Elephone S3 16 ГБ серый в интернет...')
        self.assertEquals(serp['sn'][0]['s'], u'Купить с гарантией качества 5.2" Смартфон Elephone S3 16 ГБ серый в интернет магазине DNS. Выгодные цены на Elephone S3 в сети магазинов DNS. Можно купить в кредит или рассрочку. ... Грамотные и дружелюбные продавцы-консультанты сориентируют Вас в широком ассортименте магазина и помогут выбрать нужный товар высочайшего качества, даже если Вы еще не знаете, что именно хотите приобрести. Интернет-дискаунтер – это доступные цены, удобство заказа и широчайший ассортимент в клике от Вас! В TechnoPoint нет продавцов-консультантов и торговых залов в привычном их понимании, но качество товара остается на высоте. Закажите доставку «до двери» или заберите вашу покупку в любой точке выдачи в удобное для Вас время! Перейти на сайт. Скрыть')

        self.assertEquals(serp['sn'][49]['d'], 'ru.gearbest.com')
        self.assertEquals(serp['sn'][49]['u'], 'https://ru.gearbest.com/elephone-s3-_gear/')
        self.assertEquals(serp['sn'][49]['t'], u'Elephone S3 - купить Elephone S3 по лучшей цене... | GearBest')
        self.assertEquals(serp['sn'][49]['s'], u'Elephone S3 16 Гб 4G Смартфон 5.2 дюйма MTK6753 3GB RAM 13MP камера 2.5D FHD дисплей Android 6.0 64 битный 8 ядер 1.3GHz сканер отпечатков пальцев. 199.41. видео. Добавить в корзину. Добавить в избранное (1276) (55). "Elephone S3" (Посмотреть все 575 результаты). Hesvit S3 Smart Hesvitband Умный браслет Отображение температуры влажности сердечного ритма. 64.86. Добавить в избранное (695) (14). Добавить в корзину. сравните. Hesvit S3 Smart Hesvitband Умный браслет Отображение температуры влажности сердечного ритма. 64.86. Добавить в избранное (85) (14). Добавить в корзину. сравните. K... Скрыть')

    def test71(self):
        html = self.get_data('context-2018-01-01.html')

        parser = YandexParser(html)
        serp = parser.get_context_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 8)

        self.assertEquals(serp['sn'][0]['a'], 't')
        self.assertEquals(serp['sn'][1]['a'], 't')
        self.assertEquals(serp['sn'][2]['a'], 't')
        self.assertEquals(serp['sn'][3]['a'], 't')
        self.assertEquals(serp['sn'][4]['a'], 'b')
        self.assertEquals(serp['sn'][5]['a'], 'b')
        self.assertEquals(serp['sn'][6]['a'], 'b')
        self.assertEquals(serp['sn'][7]['a'], 'b')

    def test72(self):
        html = self.get_data('context-2018-01-12.html')

        parser = YandexParser(html)
        serp = parser.get_context_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 8)

        self.assertEquals(serp['sn'][0]['a'], 't')
        self.assertEquals(serp['sn'][1]['a'], 't')
        self.assertEquals(serp['sn'][2]['a'], 't')
        self.assertEquals(serp['sn'][3]['a'], 't')
        self.assertEquals(serp['sn'][4]['a'], 'b')
        self.assertEquals(serp['sn'][5]['a'], 'b')
        self.assertEquals(serp['sn'][6]['a'], 'b')
        self.assertEquals(serp['sn'][7]['a'], 'b')


    def test73(self):
        html = self.get_data('2018-01-24.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 7000000)

        self.assertEquals(serp['sn'][0]['d'], 'megapolisfit.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://megapolisfit.ru/')
        self.assertEquals(serp['sn'][0]['t'], u'Megapolis. Фитнес-клуб')
        self.assertEquals(serp['sn'][0]['s'], u'Приходите и займите свой фитнес-квартал в Мегаполисе! ... Семь минут пешком от м.Савёловская.')

        self.assertEquals(serp['sn'][49]['d'], 'megapolis-parking.ru')
        self.assertEquals(serp['sn'][49]['u'], 'https://megapolis-parking.ru/')
        self.assertEquals(serp['sn'][49]['t'], u'Парковочный комплекс ТРЦ Мегаполис')
        self.assertEquals(serp['sn'][49]['s'], u'Посетители ТРЦ Мегаполис могут воспользоваться подземным паркингом на 170 машиномест или многоуровневым паркингом на 450 машиномест...')

    def test74(self):
        html = self.get_data('2018-01-24-1.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 170000000)

        self.assertEquals(serp['sn'][0]['d'], 'mirkasko.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://MirKasko.ru/kasko_na_honda_cr-v.html')
        self.assertEquals(serp['sn'][0]['t'], u'Стоимость КАСКО на Honda CR-V (Хонда срв)')
        self.assertEquals(serp['sn'][0]['s'], u'СК. Honda CR-V 2012г. ... 131 824. 106 964. КАСКО для наиболее стандартного портрета водителя - расчет КАСКО произведен для условий')

        self.assertEquals(serp['sn'][49]['d'], '98rus.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://98rus.ru/poslednie-zastrahovannye-mashiny/kasko-na-honda-cr-v')
        self.assertEquals(serp['sn'][49]['t'], u'Сколько стоит КАСКО на Honda CR-V в Санкт-Петербурге?')
        self.assertEquals(serp['sn'][49]['s'], u'КАСКО на Honda CR-V Страховая сумма 900 000 Страховая премия 47 000 Страховая компания Сургутнефтегаз. Рассчитайте стоимость КАСКО на свой автомобиль прямо сейчас по ссылке.')

    def test75(self):
        html = self.get_data('mobile-2018-01-24.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], None)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'e-katalog.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://www.e-katalog.ru/list/122/asus/')
        self.assertEquals(serp['sn'][0]['t'], u'Мобильные телефоны Asus - каталог цен, где купить...')
        self.assertEquals(serp['sn'][0]['s'], u'Мобильные телефоны Asus. цены на 49 моделей. Asus. ... Каталог Asus 2018 - новинки, хиты продаж, купить мобильные телефоны. Модели. в продаже все. Бренды. Alcatel Apple Asus BQ Fly HTC Huawei LG Meizu Motorola Nokia Samsung Sony Xiaomi ZTE Все бренды. Asus (корпус). Корпус По направлениям Операционная система Серия без разрезов. моноблок. Скрыть')

        self.assertEquals(serp['sn'][49]['d'], 'svyaztelecom.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://www.svyaztelecom.ru/catalog/65.html')
        self.assertEquals(serp['sn'][49]['t'], u'Сотовые телефоны ASUS - купить, цена смартфона ASUS...')
        self.assertEquals(serp['sn'][49]['s'], u'В каталоге Сотовые телефоны интернет магазина Связь Телеком представлен широкий выбор моделей ASUS. В нем Вы можете подобрать, заказать и купить смартфоны ASUS по привлекательной цене с доставкой по Москве. Скрыть')

    def test76(self):
        html = self.get_data('mobile-2018-01-25.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], None)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'fb.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://fb.ru/article/217598/skobyanyie-izdeliya---chto-eto-takoe-vidyi-i-harakteristika-skobyanyih-izdeliy')
        self.assertEquals(serp['sn'][0]['t'], u'Скобяные изделия - что это такое? Виды и характеристика...')
        self.assertEquals(serp['sn'][0]['s'], u'Во все времена пользовались высоким спросом скобяные изделия. Что это такое? Это различные металлические детали, которые применяются в самых разных сферах. ... В очень разных ситуациях нам могут пригодиться скобяные изделия. Что это такое, мы уже узнали. Осталось разобраться, какими они бывают и где целесообразно их использовать. Скрыть')

        self.assertEquals(serp['sn'][49]['d'], 'bmskirov.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://www.bmskirov.ru/catalog/zamochno_skobyanye_izdeliya/')
        self.assertEquals(serp['sn'][49]['t'], u'ЗАМОЧНО-СКОБЯНЫЕ ИЗДЕЛИЯ')
        self.assertEquals(serp['sn'][49]['s'], u'ЗАМОЧНО-СКОБЯНЫЕ ИЗДЕЛИЯ купить в Кирове по низкой цене. Распилим. Погрузим. Доставим. Скидка на весь ассортимент 5% в будни с 18 до 19 и в воскресенье. ... ЗАМОЧНО-СКОБЯНЫЕ ИЗДЕЛИЯ. 12 3 4 ... 45 След. Сортировать по:имени цене. Скрыть')

    def test77(self):
        html = self.get_data('2018-01-25.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 61000000)

        self.assertEquals(serp['sn'][0]['d'], 'entero.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://www.Entero.ru/item/49964')
        self.assertEquals(serp['sn'][0]['t'], u'Зонт вытяжной Кобор ЗПВ-150/80')
        self.assertEquals(serp['sn'][0]['s'], u'Вытяжной зонт Кобор ЗПВ-150/80 предназначен для очистки воздуха от жира, масла, дыма и водяного пара на предприятиях пищевой промышленности...')

        self.assertEquals(serp['sn'][49]['d'], 'xn------8cdkhe3aqic9ag3b0g4e.xn--p1ai')
        self.assertEquals(serp['sn'][49]['u'], 'http://www.xn------8cdkhe3aqic9ag3b0g4e.xn--p1ai/category_name-78/category_name-35')
        self.assertEquals(serp['sn'][49]['t'], u'Зонты вентиляционные')
        self.assertEquals(serp['sn'][49]['s'], u'Купить. В закладки. В сравнение. Зонт вытяжной пристенный ЗПВ -150/80.')

    def test78(self):
        html = self.get_data('mobile-2018-01-26.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], None)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'svyaznoy.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://www.svyaznoy.ru/catalog/phone/224/ginzzu')
        self.assertEquals(serp['sn'][0]['t'], u'Мобильные телефоны Ginzzu купить в Москве, цена сотового телефона Гинззу в интернет-магазине Связной')
        self.assertEquals(serp['sn'][0]['s'], u'В интернет-магазине Связной представлен широкий выбор сотовых телефонов Ginzzu. В нашем каталоге Вы можете подобрать мобильный телефон Гинззу. Заказать и купить мобильный телефон Ginzzu по привлекательной цене, можно в интернет-магазине – продажа осуществляется с доставкой по России. Скрыть')

        self.assertEquals(serp['sn'][49]['d'], 'mobilecatalog.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://www.mobilecatalog.ru/ginza/')
        self.assertEquals(serp['sn'][49]['t'], u'Мобильные телефоны Ginza - каталог мобильных телефонов')
        self.assertEquals(serp['sn'][49]['s'], u'Мобильные телефоны ginza. Ginza MS100 Поддерживаемые стандарты: GSM 1800/GSM 1900/GSM 850/GSM 900 Размеры телефона: 108x46x17 мм Вес телефона: 95 г. Год выпуска: 2007 г. Сотовые телефоны Ginza: все модели. Ginza MS100. Сотовые телефоны Ginza. Наши рассылки Новости мобильной связи Всё о мобильной связи Обзор основных событий за прошедшую неделю Последние модели мобильных телефонов. На форуме. Бюро переводов. Скрыть')

    def test79(self):
        html = self.get_data('2018-01-26.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 38000000)

        self.assertEquals(serp['sn'][0]['d'], 'aviashop.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://www.AviaShop.ru/')
        self.assertEquals(serp['sn'][0]['t'], u'Авиабилеты ДЕШЕВО - купить билет на самолет! - Москва')
        self.assertEquals(serp['sn'][0]['s'], u'Вы покупаете авиабилеты по ценам авиакомпаний. ... Узнать стоимость авиабилетов можно в режиме онлайн и по телефонам.')

        self.assertEquals(serp['sn'][49]['d'], 'farf.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://www.farf.ru/deshevie-bileti-na-samolet/')
        self.assertEquals(serp['sn'][49]['t'], u'Купить самые дешевые авиабилеты (билеты на самолет)...')
        self.assertEquals(serp['sn'][49]['s'], u'Мы поможем Вам выбрать наиболее удачный рейс, учитывая все Ваши пожелания, в том числе и предпочтительную стоимость авиабилетов.')

    def test80(self):
        html = self.get_data('2018-01-29.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 95000000)

        self.assertEquals(serp['sn'][0]['d'], 'coffeemag.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://www.coffeemag.ru/Bumazhnye-stakany-250ml')
        self.assertEquals(serp['sn'][0]['t'], u'Бумажные стаканы 250 мл млкупить Бумажные стаканы...')
        self.assertEquals(serp['sn'][0]['s'], u'Бумажные стаканы 250 мл выпускаются разноцветными и белыми, с рисунком или специально нанесенным логотипом.')

        self.assertEquals(serp['sn'][49]['d'], 'geo-vita.com')
        self.assertEquals(serp['sn'][49]['u'], 'https://geo-vita.com/gofrirovannyj-stakan-240-ml/')
        self.assertEquals(serp['sn'][49]['t'], u'Одноразовый гофрированный стаканчик для кофе 250 мл')
        self.assertEquals(serp['sn'][49]['s'], u'Одноразовый биоразлагаемый стакан премиального качества GEOVITA: - дольше сохраняет напиток горячим или холодным - не обжигает руку - биоразлагаемый и экологически чистый продукт - уникальный дизайн...')

    def test81(self):
        html = self.get_data('2018-01-29-1.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 178000000)

        self.assertEquals(serp['sn'][0]['d'], 'ru.wikipedia.org')
        self.assertEquals(serp['sn'][0]['u'], 'https://ru.wikipedia.org/wiki/%D0%A0%D0%BE%D0%B7%D0%BE%D0%B2%D1%8B%D0%B9_%D1%86%D0%B2%D0%B5%D1%82')
        self.assertEquals(serp['sn'][0]['t'], u'Розовый цвет — Википедия')
        self.assertEquals(serp['sn'][0]['s'], u'Розовый — цвет, образующийся при смешивании красного и белого. Хотя иногда его описывают как светло-красный, однако точнее будет сказать, что это ненасыщенный красный цвет, причём чаще всего с примесью пурпурного.')

        self.assertEquals(serp['sn'][49]['d'], 'fashiony.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://fashiony.ru/tag.php?id_t=1160')
        self.assertEquals(serp['sn'][49]['t'], u'розовый')
        self.assertEquals(serp['sn'][49]['s'], u'Сочетать розовый и красный в рамках одного лука?! Если вы находите эту идею интересной (а, возможно, у вас уже есть не один образ...')

    def test82(self):
        html = self.get_data('2018-01-30.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 87000000)

        self.assertEquals(serp['sn'][0]['d'], 'kp.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://www.kp.ru/guide/analizy-na-vich.html')
        self.assertEquals(serp['sn'][0]['t'], u'Анализы на ВИЧ: какие анализы сдают и как проводят...')
        self.assertEquals(serp['sn'][0]['s'], u'Анализы на выявление ВИЧ и СПИД: когда они назначаются, где проводятся и как трактуются результаты. Молекулярно-биологическое исследование крови на ДНК вируса иммунодефицита человека ВИЧ-1 (Humman immunodeficiency virus HIV-1)...')

        self.assertEquals(serp['sn'][49]['d'], 'ztema.ru')
        self.assertEquals(serp['sn'][49]['u'], 'https://ztema.ru/inspect/analiz-krovi-na-vich')
        self.assertEquals(serp['sn'][49]['t'], u'Анализ крови на ВИЧ')
        self.assertEquals(serp['sn'][49]['s'], u'Конечной развернутой стадией ВИЧ-инфекции является СПИД – синдром приобретенного иммунодефицита. ... В каких случаях следует сдать анализ на ВИЧ? Вирус бессимптомно может жить в организме человека несколько лет.')

    def test83(self):
        html = self.get_data('2018-02-01.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 98000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'matchtv.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://matchtv.ru/on-air')
        self.assertEquals(serp['sn'][0]['t'], u'Матч ТВ: прямой эфир, футбольные трансляции...')
        self.assertEquals(serp['sn'][0]['s'], u'Овечкин выиграл конкурс на силу броска в мастер-шоу Матча звезд НХЛ. Мартин Сундбю: «Решение МОК по Устюгову?')

        self.assertEquals(serp['sn'][49]['d'], 'goal-online.org')
        self.assertEquals(serp['sn'][49]['u'], 'http://goal-online.org/')
        self.assertEquals(serp['sn'][49]['t'], u'Смотрите футбол онлайн - Прямые трансляции матчей')
        self.assertEquals(serp['sn'][49]['s'], u'Онлайн трансляции футбольных матчей в HD, SopCast, AceStream. Видео обзоры голов, таблицы, новости.')

    def test84(self):
        html = self.get_data('2018-02-01-1.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 53000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'sports.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://www.sports.ru/chelsea/news/')
        self.assertEquals(serp['sn'][0]['t'], u'Новости команды Челси на Sports.ru')
        self.assertEquals(serp['sn'][0]['s'], u'Челси, Новости на Sports.ru - все новости, состав, календарь, интервью, фото и видео. История и форма команды, форумы и блоги болельщиков.')

        self.assertEquals(serp['sn'][49]['d'], 'profootball.ua')
        self.assertEquals(serp['sn'][49]['u'], 'http://www.profootball.ua/2018/01/31/chelsi_obyavil_o_perehode.html')
        self.assertEquals(serp['sn'][49]['t'], u'"Челси" объявил о переходе Эмерсона | ПРО ФУТБОЛ')
        self.assertEquals(serp['sn'][49]['s'], u'Комментарии новостей. ... "Челси" объявил о переходе Эмерсона. Защитник "Ромы" Эмерсон Палмиери дос Сантос продолжит карьеру в "Челси", сообщает...')

    def test85(self):
        html = self.get_data('2018-02-12.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 58000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'alltime.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://www.alltime.ru/watch/filter/params:skeleton/')
        self.assertEquals(serp['sn'][0]['t'], u'Наручные часы скелетоны купить в интернет-магазине...')
        self.assertEquals(serp['sn'][0]['s'], u'Популярные наручные часы скелетоны. женские мужские. Вниманию истинных часовых гурманов представляет наш интернет магазин - наручные часы скелетоны!')

        self.assertEquals(serp['sn'][49]['d'], 'xn----7sbbibna0c5aqo4e8e.xn--p1ai')
        self.assertEquals(serp['sn'][49]['u'], 'http://xn----7sbbibna0c5aqo4e8e.xn--p1ai/katalog/chasy-skeleton')
        self.assertEquals(serp['sn'][49]['t'], u'Купить часы-скелетоны')
        self.assertEquals(serp['sn'][49]['s'], u'Часы скелетоны. Кроме настенных часов скелетонов довольно много настольных моделей.')

    def test86(self):
        html = self.get_data('context-2018-04-05.html')

        parser = YandexParser(html)
        serp = parser.get_context_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 8)

        self.assertEquals(serp['sn'][0]['a'], 't')
        self.assertEquals(serp['sn'][1]['a'], 't')
        self.assertEquals(serp['sn'][2]['a'], 't')
        self.assertEquals(serp['sn'][3]['a'], 't')
        self.assertEquals(serp['sn'][4]['a'], 'b')
        self.assertEquals(serp['sn'][5]['a'], 'b')
        self.assertEquals(serp['sn'][6]['a'], 'b')
        self.assertEquals(serp['sn'][7]['a'], 'b')

    def test87(self):
        html = self.get_data('mobile-2018-04-17.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], None)
        self.assertEquals(len(serp['sn']), 10)

        self.assertEquals(serp['sn'][0]['d'], 'takelag-partner.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://www.takelag-partner.ru/service/rigging/shop-move')
        self.assertEquals(serp['sn'][0]['t'], u'Такелаж торгового оборудования - Такелаж-Партнер')
        self.assertEquals(serp['sn'][0]['s'], u'Именно такую услугу, как такелаж торгового оборудования по Москве и за её пределами, предлагает наша компания «Такелаж-Партнёр». Цены на перевозку торгового оборудования. Наименование услуги. Масса перемещаемого оборудования. Кол-во такелажников. Чел./час. Минимальное кол-во часов. Стоимость за кг перемещаемого оборудования. Масса от 1 т. от 1 т. Скрыть')

        self.assertEquals(serp['sn'][2]['d'], 'takelaj-gruz.ru')
        self.assertEquals(serp['sn'][2]['u'], 'http://takelaj-gruz.ru/takelazh/torgobogo-oborudovaniya/')
        self.assertEquals(serp['sn'][2]['t'], u'Такелаж торгового оборудования в Москве - "Столичное..."')
        self.assertEquals(serp['sn'][2]['s'], u'Перевозка и такелаж торгового оборудования может быть выполнены по Москве и Московской области и в другие регионы по территории России. В зависимости от пункта назначения, торговое оборудование может быть перевезено автомобильным транспортом, по железной дороге (в контейнере, крытом или в сборном вагоне). Этапы организации такелажных работ: Звонок менеджеру. Выезд оценщика. Скрыть')

        self.assertEquals(serp['sn'][9]['d'], 'takelazhnye-uslugi.ru')
        self.assertEquals(serp['sn'][9]['u'], 'http://takelazhnye-uslugi.ru/takelazh-torgovogo-oborudovaniya.html')
        self.assertEquals(serp['sn'][9]['t'], u'Такелаж торгового оборудования')
        self.assertEquals(serp['sn'][9]['s'], u'Такелаж торгового оборудования – одна из ключевых услуг нашей компании. Каждая организация, занимающаяся таким видом деятельности, как торговля, обязательно время от времени выполняет переноску и транспортировку своего вспомогательного оборудования. Случается, что торговые точки по каким-то причинам, например, высокой аренды, переезжают из одного места в другое, для качественной и осторожной перевозки техники предприниматели обращаются к компаниям, оказывающим такелажные услуги. Скрыть')

    def test88(self):
        html = self.get_data('context-2018-05-10.html')

        parser = YandexParser(html)
        serp = parser.get_context_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 7)

        self.assertEquals(serp['sn'][0]['a'], 't')
        self.assertEquals(serp['sn'][1]['a'], 't')
        self.assertEquals(serp['sn'][2]['a'], 't')
        self.assertEquals(serp['sn'][3]['a'], 't')
        self.assertEquals(serp['sn'][4]['a'], 'b')
        self.assertEquals(serp['sn'][5]['a'], 'b')
        self.assertEquals(serp['sn'][6]['a'], 'b')

    def test89(self):
        html = self.get_data('context-2018-06-13.html')

        parser = YandexParser(html)
        serp = parser.get_context_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 7)

        self.assertEquals(serp['sn'][0]['a'], 't')
        self.assertEquals(serp['sn'][1]['a'], 't')
        self.assertEquals(serp['sn'][2]['a'], 't')
        self.assertEquals(serp['sn'][3]['a'], 'b')
        self.assertEquals(serp['sn'][4]['a'], 'b')
        self.assertEquals(serp['sn'][5]['a'], 'b')
        self.assertEquals(serp['sn'][6]['a'], 'b')

    def test90(self):
        html = self.get_data('2018-07-25.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 87000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'zavod-svai.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://www.zavod-svai.ru/ceny/')
        self.assertEquals(serp['sn'][0]['t'], u'Винтовые сваи, цены - купить винтовые сваи для...')
        self.assertEquals(serp['sn'][0]['s'], u'Наиболее актуальным решением купить винтовые сваи класса "Премиум" будет в случаях, когда: на участке большое количество корней деревьев; попадается щебень, гравий, гранитная крошка или строительный мусор ... Также оформить заказ на винтовые сваи в Москве можно в нашем офисе. Мы гарантируем, что цена на наши винтовые сваи и их монтаж - ниже, чем у конкурентов. Остались вопросы? Скрыть')

        self.assertEquals(serp['sn'][23]['d'], 'svaybur.ru')
        self.assertEquals(serp['sn'][23]['u'], 'https://www.SvayBur.ru/tseny')
        self.assertEquals(serp['sn'][23]['t'], u'Винтовые сваи - цена от 749 рублей | Купить недорого...')
        self.assertEquals(serp['sn'][23]['s'], u'Цена на винтовые сваи с монтажом и без. Купить в Москве недорого заводские винтовые сваи в компании «СВАЙБУР» круглосуточно.')

        self.assertEquals(serp['sn'][49]['d'], 'svai-vintovie-moskva.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://svai-vintovie-moskva.ru/')
        self.assertEquals(serp['sn'][49]['t'], u'svai-vintovie-moskva.ru - Москва')
        self.assertEquals(serp['sn'][49]['s'], u'')

    def test91(self):
        html = self.get_data('2018-08-23.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 244000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'lustra-house.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://lustra-house.ru/katalog/lyustry/nedorogie/')
        self.assertEquals(serp['sn'][0]['t'], u'Купить люстры недорого, интернет-магазин недорогих...')
        self.assertEquals(serp['sn'][0]['s'], u'Интернет-магазин люстр и светильников. ... Недорогие люстры. Люстра Lumion 3057/5C. Наличие уточняйте. Цена: 2 740 руб. Купить. Люстра Lumion 3099/5C. Наличие уточняйте. Цена: 2 616 руб. Купить. Люстра Lumion 3234/5C. Наличие уточняйте. Цена: 2 159 руб. Купить. Скрыть')

        self.assertEquals(serp['sn'][49]['d'], 'europalight.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://www.EuropaLight.ru/catalog/lyustry/')
        self.assertEquals(serp['sn'][49]['t'], u'Люстры из Европы купить недорого в Москве')
        self.assertEquals(serp['sn'][49]['s'], u'Интернет-магазин Europa Light предлагает купить Люстры в Москве: низкие цены, качественные фото. Бесплатная доставка. ... Смелые идеи воплотили дизайнерские люстры: купить оригинальные светильники теперь стало проще. Окунуться в красоту деталей можно в каталоге: • Выразить технический прогресс в люстрах? Легко! Четкие линии, металл и ахроматические цвета для стиля хай-тек; • Подчеркнут античный стиль (ампир) изогнутые светильники, напоминающие свечи; • Лампы простых форм уравновесят стиль минимализма; • Для поклонников кантри – люстры, выполненные из дерева или скрытые от глаз плотным абажуром; • Роскошный арт-деко находит выражение в причудливых сочетаниях металла и органзы. Скрыть')

    def test92(self):
        html = self.get_data('2018-11-13.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 133000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'baza-nakalinovke.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://baza-nakalinovke.ru/')
        self.assertEquals(serp['sn'][0]['t'], u'База отдыха в Астрахани – «На Калиновке»')
        self.assertEquals(serp['sn'][0]['s'], u'База отдыха категории 3 звезды для семейного и корпоративного досуга, охоты и рыбалки. Описание номеров различных категорий с фотографиями. Транспортные услуги: трансфер, теплоход, катера, квадроциклы, скутеры. Развлечения для детей и взрослых, оздоровительные и познавательные мероприятия. Стоимость. Фото- и видеогалереи, виртуальный обзор, отзывы, статьи. Контакты, онлайн-бронирование. Скрыть')

        self.assertEquals(serp['sn'][49]['d'], 'sites.reformal.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://sites.reformal.ru/baza-nakalinovke.ru')
        self.assertEquals(serp['sn'][49]['t'], u'baza-nakalinovke.ru... База отдыха в Астрахани – «На...»')
        self.assertEquals(serp['sn'][49]['s'], u'База отдыха в Астрахани – «На Калиновке». Мета-описание: Рыболовные и охотничьи туры в Астраханской области, комфортные номера, ухоженная территория, бассейн, все условия для семейного отдыха.. Проживание с комфортом Комфортные номера четырех категорий - Стандарт, Полулюкс, Люкс и VI... Рейтинг Alexa. Скрыть')

    def test93(self):
        html = self.get_data('2018-11-14.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 136000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], '101hotels.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://www.101hotels.ru/main/cities/ekaterinburg/hostels_center')
        self.assertEquals(serp['sn'][0]['t'], u'Хостелы Екатеринбурга в центре недорого: цены...')
        self.assertEquals(serp['sn'][0]['s'], u'Здесь представлены недорогие хостелы и отели в центре Екатеринбурга с ценами, отзывами, актуальными скидками и спецпредложениями. ... Здесь представлены недорогие хостелы и отели в центре Екатеринбурга с ценами, отзывами, актуальными скидками и спецпредложениями. Воспользуйтесь поиском по датам, чтобы уточнить стоимость и доступность номеров на выбранные даты. Поиск гостиницы. Скрыть')

        self.assertEquals(serp['sn'][49]['d'], 'ekb1.likehostels.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://ekb1.likehostels.ru/')
        self.assertEquals(serp['sn'][49]['t'], u'Like Hostel - гостиница в Екатеринбурге от 350 рублей!')
        self.assertEquals(serp['sn'][49]['s'], u'Like Hostel - недорогая гостиница в центре города. Комфортное размещение от 350 рублей! Забронируйте любой номер на сайте уже сейчас! ... У нас можно снять комнату в Екатеринбурге недорого и с хорошими условиями комфортного проживания в центральных районах города. Для тех, кто впервые планирует посетить Екатеринбург, отели и гостиницы Like Hostel станут самым удобным местом проживания, поскольку их расположение находится в шаговой доступности от основных транспортных магистралей города и важнейших инфраструктурных объектов. Like Hostel Екатеринбург в центре города – это современные и комфортабельные номера со всеми удобствами. Скрыть')

    def test94(self):
        html = self.get_data('captcha_2.html')
        self.assertTrue(YandexParser.is_yandex(html))

    def test95(self):
        html = self.get_data('context-2019-02-15.html')

        parser = YandexParser(html)
        serp = parser.get_context_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 9)

        self.assertEquals(serp['sn'][0]['a'], 't')
        self.assertEquals(serp['sn'][1]['a'], 't')
        self.assertEquals(serp['sn'][2]['a'], 't')
        self.assertEquals(serp['sn'][3]['a'], 't')
        self.assertEquals(serp['sn'][4]['a'], 'b')
        self.assertEquals(serp['sn'][5]['a'], 'b')
        self.assertEquals(serp['sn'][6]['a'], 'b')
        self.assertEquals(serp['sn'][7]['a'], 'b')
        self.assertEquals(serp['sn'][8]['a'], 'b')

    def test96(self):
        self.maxDiff = None
        html = self.get_data('captcha_3.html')
        parser = YandexParser(html)

        captcha_data = parser.get_captcha_data()
        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(captcha_data['url'], u'https://yandex.ru/captchaimg?aHR0cHM6Ly9leHQuY2FwdGNoYS55YW5kZXgubmV0L2ltYWdlP2tleT0wMDI2NUFmTGQwcHZSeGU4cHdnUlB0b3FSSTBWRFI3UA,,_0/1553773996/f2712c3d83b6e2b6231abc5e829cf01b_144b55b97ef8536dc99339901a76280a')
        self.assertEquals(captcha_data['form_action'], u'/checkcaptcha')
        self.assertEquals(captcha_data['form_data']['key'], '00265AfLd0pvRxe8pwgRPtoqRI0VDR7P_0/1553773996/f2712c3d83b6e2b6231abc5e829cf01b_1a86e6e248af6a9a3a32f2198b7af51c')
        self.assertEquals(captcha_data['form_data']['retpath'], 'https://yandex.ru/search/touch?msid=1553773995.145862.3091&lr=213&text=satellite%20c850%20e7k&suggest_reqid=498590402153961121639951454095371_7865790594b24f955ee827816529be73')

    def test97(self):
        html = self.get_data('context-2019-04-10.html')

        parser = YandexParser(html)
        serp = parser.get_context_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 9)

        self.assertEquals(serp['sn'][0]['a'], 't')
        self.assertEquals(serp['sn'][1]['a'], 't')
        self.assertEquals(serp['sn'][2]['a'], 't')
        self.assertEquals(serp['sn'][3]['a'], 't')
        self.assertEquals(serp['sn'][4]['a'], 'b')
        self.assertEquals(serp['sn'][5]['a'], 'b')
        self.assertEquals(serp['sn'][6]['a'], 'b')
        self.assertEquals(serp['sn'][7]['a'], 'b')
        self.assertEquals(serp['sn'][8]['a'], 'b')

    def test98(self):
        html = self.get_data('context-2019-04-10.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 7000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'mebel-v-podolske.ru')
        self.assertEquals(serp['sn'][0]['u'], 'http://Mebel-v-Podolske.ru/divanyi-v-podolske')
        self.assertEquals(serp['sn'][0]['t'], u'Диваны в Подольске недорого можно купить в нашем...')
        self.assertEquals(serp['sn'][0]['s'], u'Цены снижены на все диваны в Подольске. Покупайте диван недорого. ... Именно поэтому купить диван в Подольске недорого в нашем интернет магазине – значит приобрести самый необходимый элемент интерьера. Данный вид мягкой мебели требует тщательного выбора и просто обязан учитывать все требования будущего владельца, а поэтому на нашем сайте вы сможете подробно ознакомиться с внешним видом и описанием товара, узнать цены, а также увидеть действующие акции и скидки нашего магазина, купить диваны в Подольске недорого можно в нашем интернет магазине, а в качестве приятного бонуса мы гарантируем вам отличное качество и износоустойчивость. Скрыть')

        self.assertEquals(serp['sn'][49]['d'], 'podolqwzsk.sravni.com')
        self.assertEquals(serp['sn'][49]['u'], 'https://podolqwzsk.sravni.com/catc4606t18312.html')
        self.assertEquals(serp['sn'][49]['t'], u'Диваны. Цены в Подольске на Диваны. Купить')
        self.assertEquals(serp['sn'][49]['s'], u'Диваны: сравнить цены в Подольске. Купить Диван в интернет-магазинах г. Подольск. Характеристики, фото, отзывы, продажа в каталоге цен Sravni.com. ... Купить Диваны в Подольске. Lareto Диван Rosso 2 - х местный Компактные размеры двухместного дивана " Rosso" позволят ему отлично разместиться даже в маленькой комнате. Внешний вид изделия, напоминающий складки шарпея или выд...авленный тюбик зубной пасты, разработан именитыми д. оценить. 66 030 руб. Купить. Скрыть')

    def test99(self):
        html = self.get_data('2019-04-23.html')

        parser = YandexParser(html, exclude_market_yandex=False)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 9000000)
        self.assertEquals(len(serp['sn']), 11)

        self.assertEquals(serp['sn'][0]['d'], 'mvideo.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://www.mvideo.ru/pylesosy-i-aksessuary/pylesosy-2438')
        self.assertEquals(serp['sn'][0]['t'], u'Купить Пылесосы в интернет-магазине М.Видео, низкие...')
        self.assertEquals(serp['sn'][0]['s'], u'Пылесосы﻿ легко купить онлайн на сайте или по телефону 8 800 600 777 5, заказать доставку по указанному адресу или оформить самовывоз из магазина. В «М.Видео» действует программа «Гарантия лучшей цены». Если у конкурентов выбранный товар оказался дешевле, мы снизим цену. Также в течение 14 дней у вас есть возможность вернуть разницу в случае снижения стоимости на приобретённый товар. Фильтры. без мешка 260. Скрыть')

        self.assertEquals(serp['sn'][2]['d'], 'market.yandex.ru')
        self.assertEquals(serp['sn'][2]['u'], 'https://market.yandex.ru/product--pylesos-samsung-sc5241/7825239?hid=16302535&nid=83796&clid=502')
        self.assertEquals(serp['sn'][2]['t'], u'Пылесос Samsung SC5241 на Маркете')
        self.assertEquals(serp['sn'][2]['s'], u'тип: традиционный, тип пылесборника: мешок, тип уборки: сухая, мощность всасывания: 410 Вт, потребляемая мощность: 1800 Вт, комплектация: фильтр тонкой очистки, труба всасывания: телескопическая, дополнительные функции: индикатор заполнения пылесборника')

        self.assertEquals(serp['sn'][10]['d'], 'holodilnik.ru')
        self.assertEquals(serp['sn'][10]['u'], 'https://www.holodilnik.ru/domestic/vacuum_cleaners/')
        self.assertEquals(serp['sn'][10]['t'], u'Пылесосы, моющие пылесосы, выбор пылесосов...')
        self.assertEquals(serp['sn'][10]['s'], u'предлагает купить в Москве и МО Пылесосы. Найти. Только «белая» бытовая техника. ... Приобретая технику в рассрочку, вы не можете воспользоваться другими видами скидок. Покупка в рассрочку недоступна для юридических лиц. Уведомить о поступлении товара. Скрыть')

    def test100(self):
        html = self.get_data('2019-06-18.html')

        parser = YandexParser(html, exclude_market_yandex=False)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 8000)
        self.assertEquals(len(serp['sn']), 10)

        self.assertEquals(serp['sn'][0]['d'], 'asna.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://www.asna.ru/')
        self.assertEquals(serp['sn'][0]['t'], u'АСНА - Ассоциация Независимых Аптек')
        self.assertEquals(serp['sn'][0]['s'], u'Купить лекарства в аптеках Москва по низкой цене в сети аптек АСНА. Онлайн бронирование препаратов. Аптеки, подключенные к программе, отмечены значком.')

        self.assertEquals(serp['sn'][6]['d'], 'yandex.ru')
        self.assertEquals(serp['sn'][6]['u'], 'https://yandex.ru/maps/?source=wizbiz_new_text_multi&text=%D0%B0%D1%81%D0%BD%D0%B0&ll=37.64083873%2C55.71776114&sll=37.64083873%2C55.71776114&sctx=ZAAAAAgBEAMaKAoSCXsuU5Pg00JAET3vxoLC2ktAEhIJMGqkuwr7tD8RWW%2F%2BZQqkpz8iBQABAgQFKAAwATiX6ZfCoZeZgHlA%2Ba0HSAFVzczMPlgAYiRtaWRkbGVfYXNrX2RpcmVjdF9xdWVyeV90eXBlcz1ydWJyaWNiKG1pZGRsZV9pbmZsYXRlX2RpcmVjdF9maWx0ZXJfd2luZG93PTUwMDBiEnJlbGV2X2RydWdfYm9vc3Q9MWJEbWlkZGxlX2RpcmVjdF9zbmlwcGV0cz1waG90b3MvMi54LGJ1c2luZXNzcmF0aW5nLzIueCxtYXNzdHJhbnNpdC8xLnhiKm1pZGRsZV9pbmZsYXRlX2RpcmVjdF9yZXF1ZXN0X3dpbmRvdz0xMDAwMGIebWlkZGxlX2Fza19kaXJlY3RfcGVybWFsaW5rcz0xYiBtaWRkbGVfZGlyZWN0X2V4cGVyaW1lbnQtaWQ9NzI3OWIdcmVsZXZfZmlsdGVyX2d3a2luZHM9MC4zLDAuNDViKXJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vQWxsb3dUcmF2ZWxCb29zdD0xYjFyZWFycj1zY2hlbWVfTG9jYWwvR2VvdXBwZXIvZmVhdHVyZXNGcm9tT2JqZWN0cz0xYi9yZWFycj1zY2hlbWVfTG9jYWwvR2VvL1Bvc3RmaWx0ZXIvQWJzVGhyZXNoPTAuMmIpcmVhcnI9c2NoZW1lX0xvY2FsL0dlby9DdXRBZmlzaGFTbmlwcGV0PTFiMHJlYXJyPXNjaGVtZV9Mb2NhbC9HZW8vSG90ZWxCb29zdD1wYXJ0bmVyX2NsaWNrc2IpcmVhcnI9c2NoZW1lX0xvY2FsL0dlby9Vc2VHZW9UcmF2ZWxSdWxlPTFqAnJ1cAGVAQAAAACdAc3MTD6gAQGoAQC9AWkw5DfCAR2C8bLCnAPtw%2Ben9AWH%2BImz%2FAHjnLiK9QG7n9jfRQ%3D%3D&sspn=0.047665%2C0.026845')
        self.assertEquals(serp['sn'][6]['t'], u'Асна в Даниловском районе - отзывы, фото, телефоны,…')
        self.assertEquals(serp['sn'][6]['s'], u'Асна в Даниловском районе - отзывы, фото, телефоны, адреса с рейтингом, отзывами и фотографиями. Адреса, телефоны, часы работы, схема проезда.')

        self.assertEquals(serp['sn'][9]['d'], 'zoon.ru')
        self.assertEquals(serp['sn'][9]['u'], 'https://zoon.ru/msk/drugstore/network/asna/')
        self.assertEquals(serp['sn'][9]['t'], u'АСНА, сеть аптек - 187 аптек, фотографии, отзывы...')
        self.assertEquals(serp['sn'][9]['s'], u'АСНА, сеть аптек в Москве - мы нашли для вас 187 аптек. Самый полный каталог заведений с фото, ☎️ и отзывами, удобный поиск мест на карте. ... АСНА, сеть аптек — это 187 заведений в различных районах города. АСНА осуществляет свою деятельность в различных категориях, в том числе и многих других. Скрыть')

    def test101(self):
        html = self.get_data('2019-06-19.html')

        parser = YandexParser(html, exclude_market_yandex=False)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 6000000)
        self.assertEquals(len(serp['sn']), 10)

        self.assertEquals(serp['sn'][0]['d'], 'footboom.com')
        self.assertEquals(serp['sn'][0]['u'], 'https://www.footboom.com/spain/cup/matches')
        self.assertEquals(serp['sn'][0]['t'], u'Кубок Испании по футболу (Кубок Короля) 2018-2019...')
        self.assertEquals(serp['sn'][0]['s'], u'Кубок Испании по футболу (он же – Кубок короля) – отличная возможность для клубов-середняков попасть в еврокубки, вне зависимости от их положения в турнирной таблице чемпионата. Особенности турнира. ... Розыгрыш Кубка Испании по футболу 2018-2019 уже на ранних стадиях оказался богат на сенсации. Коллективы Ла Лиги потеряли сразу четырех своих представителей с первой попытки. Скрыть')

        self.assertEquals(serp['sn'][8]['d'], 'football.kulichki.net')
        self.assertEquals(serp['sn'][8]['u'], 'https://football.kulichki.net/spain/2018/cup.htm')
        self.assertEquals(serp['sn'][8]['t'], u'КУБОК ИСПАНИИ 2017/2018')
        self.assertEquals(serp['sn'][8]['s'], u'5:0 в матче за Кубок страны – это очень мощно. Но от таких игр всё же хотелось бы большей непредсказуемости. Они носят особый статус, их исход определяет судьбу трофея, которая, по идее, должна решаться в равной борьбе. Скрыть')

        self.assertEquals(serp['sn'][9]['d'], 'goal.net.ua')
        self.assertEquals(serp['sn'][9]['u'], 'https://goal.net.ua/news/69262.html')
        self.assertEquals(serp['sn'][9]['t'], u'Все победители Кубка Испании (ТАБЛИЦА)')
        self.assertEquals(serp['sn'][9]['s'], u'За несколько дней до финала «Кубка короля» испанская пресса «взбодрила» наставника «Барселоны» Херардо Мартино новостью о его скорой отставке. Якобы руководство «сине-гранатовых» уже определилось с увольнением аргентинца по итогам сезона. Скрыть')

    def test102(self):
        html = self.get_data('2019-06-21.html')
        parser = YandexParser(html, exclude_market_yandex=False)
        content = parser.get_clean_html()
        self.assertFalse('</title></svg>' in content)

    def test103(self):
        html = self.get_data('context-2019-08-07.html')

        parser = YandexParser(html)
        serp = parser.get_context_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 9)

        self.assertEquals(serp['sn'][0]['a'], 't')
        self.assertEquals(serp['sn'][1]['a'], 't')
        self.assertEquals(serp['sn'][2]['a'], 't')
        self.assertEquals(serp['sn'][3]['a'], 't')
        self.assertEquals(serp['sn'][4]['a'], 'b')
        self.assertEquals(serp['sn'][5]['a'], 'b')
        self.assertEquals(serp['sn'][6]['a'], 'b')
        self.assertEquals(serp['sn'][7]['a'], 'b')
        self.assertEquals(serp['sn'][8]['a'], 'b')

    def test104(self):
        html = self.get_data('mobile-2019-08-23.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], None)
        self.assertEquals(len(serp['sn']), 10)

        self.assertEquals(serp['sn'][0]['d'], 'mrdivanoff.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://mrdivanoff.ru/')
        self.assertEquals(serp['sn'][0]['t'], u'Интернет-магазин мебели в Москве - Купить мебель недорого - Цены от производителя')
        self.assertEquals(serp['sn'][0]['s'], u'В интернет-магазине мебели Мистер Диванофф представлена недорогая мебель. Низкие цены, широкий ассортимент, гарантии, доставка мебели по Москве и области! Звоните +7 (495) 109-05-36.')

        self.assertEquals(serp['sn'][9]['d'], '7divanov.ru')
        self.assertEquals(serp['sn'][9]['u'], 'https://www.7divanov.ru/')
        self.assertEquals(serp['sn'][9]['t'], u'Диваны - купить диван в интернет-магазине мебели в Москве по цене производителя')
        self.assertEquals(serp['sn'][9]['s'], u'Интернет-магазин диванов 7Диванов.ру предлагает купить диван в Москве по лучшим ценам.')

    def test105(self):
        html = self.get_data('2019-08-26.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 7000000)
        self.assertEquals(len(serp['sn']), 15)

        self.assertEquals(serp['sn'][0]['d'], 'gifts.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://gifts.ru/id/53645')
        self.assertEquals(serp['sn'][0]['t'],  u'Декантер Il Lago (артикул Z38177) - Проект 111')
        self.assertEquals(serp['sn'][0]['s'],  u'Итальянский декантер Il Lago бренда IVV украсит любой праздничный стол и превратит ужин с бутылкой вина в красивую церемонию.')

        self.assertEquals(serp['sn'][14]['d'], '40nog.ru')
        self.assertEquals(serp['sn'][14]['u'], 'https://40nog.ru/dekanter-il-lago')
        self.assertEquals(serp['sn'][14]['t'], u'Декантер il lago﻿ в Москве купить недорого в интернет...')
        self.assertEquals(serp['sn'][14]['s'], u'В наличии широкий выбор предложений в категории декантер il lago﻿. Доставка в Москве. Описания и сравнения цен, а также характеристики для товаров из категории - декантер il lago﻿ на сайте 40NOG. ... Декантер Sophienwald Collection Decanter Декантер Sophienwald Collection Decanter, сделанный в ручную мастерами стеклодувами дома Sophienwald, представляет из себя идеальный сосуд для декантации и аэрации красных вин. Скрыть')

    def test106(self):
        html = self.get_data('2019-08-27.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 10000000)
        self.assertEquals(len(serp['sn']), 10)

        self.assertEquals(serp['sn'][0]['d'], 'avtomaty.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://www.avtomaty.ru/terminals')
        self.assertEquals(serp['sn'][0]['t'], u'Платежные терминалы от 32 000 руб., купить терминалы...')
        self.assertEquals(serp['sn'][0]['s'], u'Купить платежный терминал и начать бизнес по приему платежей просто! Мы обучим Вас всем тонкостям этого бизнеса. ... Уважаемые друзья и партнеры из компании Автоматы.ру, Мы высоко оцениваем Ваш профессионализм и оперативность в работе с нами. Выражаем свое удовлетворение от сотрудничества с Вами и во многом благодаря этому мы стали одной из крупнейших в стране. Читать дальше ›. Скрыть')

        self.assertEquals(serp['sn'][9]['d'], 'stampservice.ru')
        self.assertEquals(serp['sn'][9]['u'], 'http://www.StampService.ru/product/terms')
        self.assertEquals(serp['sn'][9]['t'], u'Терминалы оплаты - стоимость и цены, купить терминалы...')
        self.assertEquals(serp['sn'][9]['s'], u'Платежные терминалы, уличные платежные терминалы ОСМП - купить терминал в Москве, ПО для платежных терминалов, производство платежных терминалов - ЗАО Стамп. Решения. Технологии. ... Цена остается доступной, а качество изготовленных автоматов – неизменно высоким. Именно поэтому продукция компании СТАМП прослужит Вам не один год. Терминалы оплаты: стоимость. Скрыть')

    def test107(self):
        html = self.get_data('2019-08-27-1.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 10000000)
        self.assertEquals(len(serp['sn']), 10)

        self.assertEquals(serp['sn'][0]['d'], 'mebelstol.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://mebelstol.ru/rubric/tables/')
        self.assertEquals(serp['sn'][0]['t'], u'Столы недорого купить в магазине MebelStol')
        self.assertEquals(serp['sn'][0]['s'], u'Столы по самой низкой цене. Квалифицированные менеджеры помогут с выбором: 8 (800) 555-39-46 (по России звонок бесплатный). Огромный ассортимент в наличии. Гарантия на все товары! Удобные способы оплаты, наличие чека. Скрыть')

        self.assertEquals(serp['sn'][9]['d'], 'lifemebel.ru')
        self.assertEquals(serp['sn'][9]['u'], 'https://lifemebel.ru/catalog/stoly/dlya_kuhni/')
        self.assertEquals(serp['sn'][9]['t'], u'Кухонные столы в Москве, купить стол для кухни...')
        self.assertEquals(serp['sn'][9]['s'], u'Столы для кухни по доступным ценам от 6 300 руб. в каталоге интернет-магазина ЛайфМебель. Купить кухонный стол недорого можно с доставкой по Москве и всей России. Звоните ☎8 (495) 540-55-17! Скрыть')

    def test108(self):
        html = self.get_data('captcha-2019-10-02.html')

        parser = YandexParser(html)
        captcha = parser.get_captcha_data()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEqual(captcha['url'], u'https://yandex.ru/captchaimg?aHR0cHM6Ly9leHQuY2FwdGNoYS55YW5kZXgubmV0L2ltYWdlP2tleT0wMDJxZlBLMGlreEFyaWtmTWhLUUVRd0N4dnpXQnFmSCZzZXJ2aWNlPXdlYg,,_0/1570003605/5aecbd65d9bd95d889196461e82e3dd9_dfdf1aedb489780274c71d408502e2c8')
        self.assertEqual(captcha['form_action'], '/checkcaptcha')
        self.assertEqual(captcha['form_data']['key'], '002qfPK0ikxArikfMhKQEQwCxvzWBqfH_0/1570003605/5aecbd65d9bd95d889196461e82e3dd9_2f242589f99d31de58088b803cf02b4c')
        self.assertEqual(captcha['form_data']['retpath'], 'https://yandex.ru/search?text=%D0%BF%D1%83%D1%82%D0%B5%D0%B2%D0%BA%D0%B8%20%D0%B2%20%D0%BA%D1%80%D1%8B%D0%BC%20%D0%B8%D0%B7%20%D0%B2%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%B0&lr=213&p=1_8be1020da495c1fb5c7b7f7560a06031')

    def test109(self):
        html = 'bad content'
        parser = YandexParser(html)
        self.assertFalse(YandexParser.is_yandex(html))

        with self.assertRaises(YandexParserContentError) as e:
            parser.get_serp()

    def test110(self):
        html = self.get_data('context-2019-11-19.html')

        parser = YandexParser(html)
        serp = parser.get_context_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 10)

        self.assertEquals(serp['sn'][0]['a'], 't')
        self.assertEquals(serp['sn'][1]['a'], 't')
        self.assertEquals(serp['sn'][2]['a'], 't')
        self.assertEquals(serp['sn'][3]['a'], 't')
        self.assertEquals(serp['sn'][4]['a'], 'b')
        self.assertEquals(serp['sn'][5]['a'], 'b')
        self.assertEquals(serp['sn'][6]['a'], 'b')
        self.assertEquals(serp['sn'][7]['a'], 'b')
        self.assertEquals(serp['sn'][8]['a'], 'b')
        self.assertEquals(serp['sn'][9]['a'], 'b')

    def test111(self):
        html = self.get_data('context-2019-11-20.html')

        parser = YandexParser(html)
        serp = parser.get_context_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 9)

        self.assertEquals(serp['sn'][0]['a'], 't')
        self.assertEquals(serp['sn'][1]['a'], 't')
        self.assertEquals(serp['sn'][2]['a'], 't')
        self.assertEquals(serp['sn'][3]['a'], 't')
        self.assertEquals(serp['sn'][4]['a'], 'b')
        self.assertEquals(serp['sn'][5]['a'], 'b')
        self.assertEquals(serp['sn'][6]['a'], 'b')
        self.assertEquals(serp['sn'][7]['a'], 'b')
        self.assertEquals(serp['sn'][8]['a'], 'b')

    def test112(self):
        html = self.get_data('2020-03-30.html')

        parser = YandexParser(html, exclude_realty_yandex=False)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 5000000)
        self.assertEquals(len(serp['sn']), 11)

        self.assertEquals(serp['sn'][0]['d'], 'novostroy-m.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://www.Novostroy-m.ru/baza/mfk_zilart/otzyvy')
        self.assertEquals(serp['sn'][0]['t'], u'226 реальных отзывов от дольщиков о ЖК «ЗИЛАРТ»...')
        self.assertEquals(serp['sn'][0]['s'], u'Март 2020 — 226 новых отзывов о ЖК «ЗИЛАРТ» от реальных покупателей на сайте Novostroy-M.ru. Читайте мнения на форуме дольщиков о расположении, экологии, планировках, качестве строительства, проблемах застройщика, просрочках по сроку сдачи. ... Ничего критичного, но приятно что все исправили еще до того как мы окончательно приняли квартиру. Ответить. Полезный отзыв? 0. 0. Скрыть')

        self.assertEquals(serp['sn'][9]['d'], 'realty.yandex.ru')
        self.assertEquals(serp['sn'][9]['u'], 'https://realty.yandex.ru/moskva/kupit/novostrojka/zilart-185390/?rgid=193297&nosplash=1&utm_source=wizard&utm_campaign=paid_sites&from=wizard.site-thumb#reviews')
        self.assertEquals(serp['sn'][9]['t'], u'ЖК «ЗИЛАРТ» — отзывы жильцов')
        self.assertEquals(serp['sn'][9]['s'], u'Цены, планировки и наличие квартир. Актуальные предложения в ЖК «ЗИЛАРТ». Москва, ул. Автозаводская, вл. 23')

        self.assertEquals(serp['sn'][10]['d'], 'msk.restate.ru')
        self.assertEquals(serp['sn'][10]['u'], 'https://Msk.Restate.ru/complex/zilart-3543/opinion/')
        self.assertEquals(serp['sn'][10]['t'], u'ЖК ЗИЛАРТ - отзывы дольщиков и покупателей.')
        self.assertEquals(serp['sn'][10]['s'], u'Отзывы дольщиков о жилом комплексе ЗИЛАРТ. Всегда самые новые комментарии покупателей о ЖК. ... ЖК "Зиларт" - знаковый, даже знаменитый объект на рынке недвижимости Москвы. В предыдущих мнениях редакции мы детально описывали достоинства, недостатки и ход строительства ЖК. Список плюсов и минусов остается актуальным, существенных изменений в рыночном статусе объекта не произошло. Скрыть')

    def test113(self):
        html = self.get_data('2020-06-29.html')

        parser = YandexParser(html, exclude_realty_yandex=False)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 14000000)
        self.assertEquals(len(serp['sn']), 9)

        self.assertEquals(serp['sn'][0]['d'], 'pravda-sotrudnikov.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://pravda-sotrudnikov.ru/company/coral-travel')
        self.assertEquals(serp['sn'][0]['t'], u'Туроператор Coral Travel: отзывы сотрудников...')
        self.assertEquals(serp['sn'][0]['s'], u'Нужны отзывы сотрудников о компании Туроператор Coral Travel? На нашем сайте есть информация о данной компании. ... Компания Coral Travel (Россия, Турция, Украина, Польша, Белоруссия, Грузия) входит в крупную международную структуру OTI Holding, основанную в 1992 году. OTI Holding также владеет компаниями Odeon Tours (Турция, Египет, Таиланд, ОАЭ, Испания, Греция), Sunmar Tour (Россия), «Сеть Турагентств Coral Travel» (Россия, Украина), A-Class Travel (Россия, Турция), Wezyr Holydays (Польша), Holiday Market Service (Турция), OGD Security & Consultancy (Турция) и отелями Otium Eco Club Side 5*, Xanadu Resort Hotel 5. Скрыть')

        self.assertEquals(serp['sn'][8]['d'], 'ru.indeed.com')
        self.assertEquals(serp['sn'][8]['u'], 'https://ru.indeed.com/cmp/Coral-Travel/reviews')
        self.assertEquals(serp['sn'][8]['t'], u'Работа в компании Coral Travel: Отзывы сотрудников')
        self.assertEquals(serp['sn'][8]['s'], u'Отзывы от сотрудников компании Coral Travel о корпоративной культуре, заработной плате, соц. пакетах, руководстве и безопасности на работе в компании Coral Travel. ... Работа в Coral travel мне нравится. Да, бывают недовольные клиенты, какие-то претензии с их стороны, которые могут портить нервы и отнимать кучу сил, но я знала, куда шла работать. В подобных компаниях везде так, от этого никуда не денешься. Скрыть')

    def test114(self):
        html = self.get_data('2020-07-03.html')

        parser = YandexParser(html, exclude_realty_yandex=False)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 6000000)
        self.assertEquals(len(serp['sn']), 10)

    def test115(self):
        html = self.get_data('2020-07-03.html')

        parser = YandexParser(html, exclude_realty_yandex=False)
        current_query = parser.get_current_query()
        current_page = parser.get_current_page()
        current_region = parser.get_current_region()
        next_page = parser.get_next_page()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEqual(current_query, u'бонусы мегафон как потратить')
        self.assertEqual(current_page, 1)
        self.assertEqual(current_region, 10658)
        self.assertEqual(next_page, 2)

    def test116(self):
        html = self.get_data('2020-07-06-not-found.html')

        parser = YandexParser(html, exclude_realty_yandex=False)
        current_query = parser.get_current_query()
        current_page = parser.get_current_page()
        current_region = parser.get_current_region()
        next_page = parser.get_next_page()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEqual(current_query, u'фвазйщшгнукзщйрыяфждывфывафывафывафыва')
        self.assertEqual(current_page, 1)
        self.assertEqual(current_region, 41)
        self.assertEqual(next_page, None)

    def test117(self):
        html = self.get_data('2020-07-06-one-page.html')

        parser = YandexParser(html, exclude_realty_yandex=False)
        current_query = parser.get_current_query()
        current_page = parser.get_current_page()
        current_region = parser.get_current_region()
        next_page = parser.get_next_page()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEqual(current_query, u'123123123123234234')
        self.assertEqual(current_page, 1)
        self.assertEqual(current_region, 41)
        self.assertEqual(next_page, None)

    def test118(self):
        html = self.get_data('2020-07-16.html')

        parser = YandexParser(html, exclude_realty_yandex=False)
        self.assertTrue(YandexParser.is_yandex(html))
        self.assertTrue(parser.page_exists(1))
        self.assertTrue(parser.page_exists(2))
        self.assertFalse(parser.page_exists(3))

    def test119(self):
        html = self.get_data('mobile-2020-11-11.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], None)
        self.assertEquals(len(serp['sn']), 10)
        with self.assertRaises(YandexParserError):
            self.assertEquals(parser.get_mobile_current_page(), 5)

        self.assertEquals(serp['sn'][0]['d'], 'zen.yandex.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://zen.yandex.ru/media/technologicus/samyi-bystryi-mobilnyi-internet-2020-5f0c77d924e4507b2677fef7')
        self.assertEquals(serp['sn'][0]['t'], u'Самый быстрый мобильный интернет 2020 | Технологикус | Яндекс Дзен | Яндекс Дзен | Блогерская платформаzen.yandex.ru › media…samyi-bystryi…')
        self.assertEquals(serp['sn'][0]['s'], u'В июле 2020 года компания Ookla, которой принадлежит мобильное приложение Speedtest, основной функцией которого является замер скорости интернета, определила мобильного оператора с самым быстрым мобильным интернетом в России. В четвёртый раз подряд награду получил Мегафон. Скрыть')

        self.assertEquals(serp['sn'][9]['d'], 'itmaster.guru')
        self.assertEquals(serp['sn'][9]['u'], 'https://itmaster.guru/nastrojka-interneta/mobilnyj-internet/kakoy-4g-internet-luchshe.html')
        self.assertEquals(serp['sn'][9]['t'], u'Какой 4g интернет лучше - самый быстрый провайдер через модем (МТС, Билайн, Теле2, Мегафон и др)itmaster.guru › nastrojka-interneta…')
        self.assertEquals(serp['sn'][9]['s'], u'Какие операторы самые популярные в России и какие условия на интернет они предлагают? Какие компании подойдут для города, а какие, к примеру, для дачи? Содержание. ... Он, как и телефон, ловит сигнал от оператора благодаря «симке», вставленной в него. «Симка» должна быть, естественно, от того оператора, которого вы выбрали ранее, следуя нашим советам выше. Можно сразу купить не модем, а мобильный роутер, чтобы раздавать «Вай-Фай» для всех своих устройств. Скрыть')

    def test120(self):
        html = self.get_data('mobile-2020-11-11-pages5.html')

        page2 = YandexParser.extract_mobile_page_content(html, 2)
        self.assertTrue('>2' in page2)

        page3 = YandexParser.extract_mobile_page_content(html, 3)
        self.assertTrue('>3' in page3)

        page4 = YandexParser.extract_mobile_page_content(html, 4)
        self.assertTrue('>4' in page4)

        page5 = YandexParser.extract_mobile_page_content(html, 5)
        self.assertTrue('>5' in page5)

        page5_full = YandexParser.create_mobile_page(page5)
        self.assertTrue(YandexParser.is_yandex(page5_full))
        serp5 = YandexParser(page5_full).get_serp()
        self.assertEquals(serp5['sn'][0]['d'], 'viborprost.ru')
        self.assertEquals(serp5['sn'][0]['u'], 'https://viborprost.ru/texnika/kompyuter/kakogo-operatora-vybrat-dlya-interneta.html')
        self.assertEquals(serp5['sn'][0]['t'], u'Мобильный интернет - какой оператор лучше: какого оператора сотовой связи выбрать для безлимитного интернетаviborprost.ru › …dlya-interneta.html')
        self.assertEquals(serp5['sn'][0]['s'], u'Как выбрать недорогой и быстрый мобильный интернет, желательно безлимитный? На каком операторе сотовой связи остановиться? В этом обзоре мы расскажем об основных тарифах и порекомендуем, на что обращать внимание при выборе тарифа на мобильный интернет. ... Подключить на них самый дешевый интернет и войти в сеть. С телефона или с модема проверить скорость интернета можно на сайте http://www.speedtest.net/. Желательно выполнить проверку несколько раз в течение суток. Это поможет выявить проблемные периоды у каждого оператора. Скрыть')

        self.assertEquals(serp5['sn'][9]['d'], 'tvoysmartphone-ru.turbopages.org')
        self.assertEquals(serp5['sn'][9]['u'], 'https://tvoysmartphone-ru.turbopages.org/tvoysmartphone.ru/s/uroki/142-kak-uskorit-internet-na-android-ustroystvah.html?turbo_uid=AABi4_qXowenH596TJ7De2aSNkIx1hMuXS2JdeLIqZDZr4Gx3Ks7EqXmMeEVwGrOxoBnPs4Cxzd2Pob1E-qrNDYMNFDbXgwBF63Au9LDB07CSblDPg%2C%2C&turbo_ic=AAAhGVsRTeVyQShKy0xfsL9Geqfp6pEbvxNFpMTX81mEl581iUzo1AAcOdACASdOGi_DgaaskuBuzZQsTEigDqRAkecu38WrKgpxRcYae34u07PcdQ%2C%2C&parent-reqid=1605098549896773-1760764814187405568900107-production-app-host-vla-web-yp-223&trbsrc=wb')
        self.assertEquals(serp5['sn'][9]['t'], u'Как ускорить интернет на Андроид устройствахTvoySmartphone.ru › …142…internet-na…')
        self.assertEquals(serp5['sn'][9]['s'], u'Как ускорить мобильный интернет на телефоне или планшете Андроид. Как уменьшить задержки и пинг по Wi-Fi сменой DNS. Интернет плотно обосновался в нашей жизни и большинству уже трудно представить обычный день без доступа к нему, на интернете завязаны как развлечения так и поиск информации или ответов на вопросы. ... Это самый весомый фактор, ибо каким бы навороченным и быстрым не было ваше устройство - если есть ограничение скорости на стороне провайдера то уже мало что сможет помочь. Скрыть')

        with self.assertRaises(YandexParserError):
            YandexParser.extract_mobile_page_content(html, 6)

        self.assertTrue(YandexParser.is_next_mobile_page(html))

        yp = YandexParser(html)
        self.assertEquals(yp.get_current_query(), u'самый быстрый интернет на телефон')
        self.assertEquals(yp.get_current_page(), 1)
        self.assertEquals(yp.get_mobile_current_page(), 5)
        self.assertEquals(yp.get_current_region(), 10946)

    def test121(self):
        html = self.get_data('mobile-2020-11-11-only-one-page.html')
        self.assertFalse(YandexParser.is_next_mobile_page(html))
        
        serp = YandexParser(html).get_serp()
        self.assertEquals(serp['sn'][0]['d'], 'prodomain.info')
        self.assertEquals(serp['sn'][0]['u'], 'https://prodomain.info/whois/skdjha.com')
        self.assertEquals(serp['sn'][0]['t'], u'Whois domain skdjha.com, n/aprodomain.info › whois/skdjha.comвчера')
        self.assertEquals(serp['sn'][0]['s'], u'lksdjha.com. rkkdjha.com. sxkjha.com. Скрыть')

        self.assertEquals(serp['sn'][1]['d'], 'pageglimpse.com')
        self.assertEquals(serp['sn'][1]['u'], 'http://www.pageglimpse.com/brandworks.com')
        self.assertEquals(serp['sn'][1]['t'], u'Site Disclaimerpageglimpse.com › brandworks.com')
        self.assertEquals(serp['sn'][1]['s'], """brandworks
 ajdkjlasdlkjasdkjasdlk jaçlskdjalksjdasdlkasdjalsdjlasjkdçlajksdlajksd 
asdjkasl djasdkj asjkd l akjsdlkja sdlkja dlsk ja asjdlkasdh ha sjha lksdjha
 lskjhd alkdsh ... http://www.brandworks.com.br/. Contact Us | 
Brandworks Address Brandworks International Inc. 366 Adelaide St. West, 
Suite 701 Toronto, Ontario M5V 1R9 Phone Tel: 416-340-8845 Fax: 
416-340-9813 Contact Jim Sproul... Скрыть""")

    def test122(self):
        html = self.get_data('mobile-2021-03-01.html')

        parser = YandexParser(html, exclude_realty_yandex=False)
        current_query = parser.get_current_query()
        current_page = parser.get_current_page()
        current_region = parser.get_current_region()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEqual(current_query, u'владимирская область отдых')
        self.assertEqual(current_page, 1)
        self.assertEqual(current_region, 213)

    def test123(self):
        html = self.get_data('captcha-2021-03-15.html')

        parser = YandexParser(html)
        captcha = parser.get_captcha_data()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEqual(captcha['url'], None)
        self.assertEqual(captcha['captcha_type'], 'i_not_robot')
        self.assertEqual(captcha['form_action'], '/checkcaptcha?key=9404dfba-3180a9b-da0b096f-cba87317_2%2F1615794970%2F492cbdaa470b03c3a7edbe2cb8ff656a_d9424dd3a4eaafecda1b65fd10bdd660&retpath=https%3A%2F%2Fwebmaster.yandex.ru%2Fsite%2Fhttps%3Aspiritfit.ru%3A443%2Fsettings%2Faccess%3F_76c596b6385ad6fb2b6866d172df4e93')
        self.assertEqual(captcha['form_data']['k'], '1_1615794970_6953264976053215454_888e1aba7f9d3b12f82f23633dbb82e1')
        self.assertEqual(captcha['form_data']['d'], 'NdW06Ww5MiEt/w6RqhMUJK04akI9zFhG4whDAOhPnz0=')
        self.assertEqual(captcha['form_data']['key'], '9404dfba-3180a9b-da0b096f-cba87317_2/1615794970/492cbdaa470b03c3a7edbe2cb8ff656a_d9424dd3a4eaafecda1b65fd10bdd660')
        self.assertEqual(captcha['form_method'], 'POST')

    def test124(self):
        html = self.get_data('captcha-2021-03-15-1.html')

        parser = YandexParser(html)
        captcha = parser.get_captcha_data()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEqual(captcha['url'], u'https://webmaster.yandex.ru/captchaimg?aHR0cHM6Ly9leHQuY2FwdGNoYS55YW5kZXgubmV0L2ltYWdlP2tleT0wMEFtb3pBd3dvMTI1Z1hJdmEwR1VOVWttVUZVc1BPOSZzZXJ2aWNlPXdlYm1hc3Rlcg,,_3/1615813434/fac4247fb350c3b7e0fbe63800d4fa2a_a1188901867930f32e276f3953142d25')
        self.assertEqual(captcha['captcha_type'], None)
        self.assertEqual(captcha['form_action'], '/checkcaptcha?key=00AmozAwwo125gXIva0GUNUkmUFUsPO9_3%2F1615813434%2Ffac4247fb350c3b7e0fbe63800d4fa2a_67cc09bd4c7a8f9553478ae6ea40d875&retpath=https%3A%2F%2Fwebmaster.yandex.ru%2Fsite%2Fhttps%3Achinatutor.ru%3A443%2Fsettings%2Faccess%3F_13be31e8f443a1f4b0faba519a5116b9')
        self.assertEqual(captcha['form_data']['k'], '1_1615813476_11062802936027662891_966ab4e777ad46cb024728d0b28aa2bd')
        self.assertEqual(captcha['form_data']['d'], 'i01Wdzt1T4fVsu/LpcZd5YF3snM/de9q3wOSfDVDJwI=')
        self.assertEqual(captcha['form_data']['key'], '00AmozAwwo125gXIva0GUNUkmUFUsPO9_3/1615813434/fac4247fb350c3b7e0fbe63800d4fa2a_67cc09bd4c7a8f9553478ae6ea40d875')
        self.assertEqual(captcha['form_method'], 'POST')

    def test125(self):
        html = self.get_data('mobile-2021-03-29.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], None)
        self.assertEquals(len(serp['sn']), 10)

        self.assertEquals(serp['sn'][0]['d'], 'msk.tele2.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://msk.tele2.ru/mobile/roaming/international/uzbekistan/camel1-unlim')
        self.assertEquals(serp['sn'][0]['t'], u'Тарифы на звонки и интернет Tele2. Прозрачные тарифы без скрытых платежей для поездок за рубеж.')
        self.assertEquals(serp['sn'][0]['s'], u'Роуминг в Узбекистане. Выберите страну, в которую собираетесь поехать. Узбекистан. ... 350 рублей в день. на остальных тарифах. Платите только в те дни, когда пользуетесь интернетом за границей. Подробнее. Стоимость услуг в Узбекистане. ₽ за Мб. интернет. Скрыть')

        self.assertEquals(serp['sn'][9]['d'], 'megasimka.ru')
        self.assertEquals(serp['sn'][9]['u'], 'https://megasimka.ru/product/sim-int-tele2-vig-175/')
        self.assertEquals(serp['sn'][9]['t'], u'Тариф ТЕЛЕ2 Выгодный 175  MEGA SIMKA')
        self.assertEquals(serp['sn'][9]['s'], u'Выгодный тарифный план на связь для абонентов Теле2 по всей России, за исключением Крыма и Севастополя. Абонентская плата и пакет минут может отличаться в зависимости от региона. Посмотреть абонентскую плату для Вашего региона >>>. Предлагаем вашему вниманию, тарифы с официального сайта Теле2 (Мой онлайн, Мой онлайн+), но с абонентской платой В 2 РАЗА НИЖЕ, +20 ГБ к основному пакету гигабайт и возможностью раздачи со смартфона! Скрыть')

    def test126(self):
        html = self.get_data('2021-04-01.html')

        parser = YandexParser(html, exclude_market_yandex=False)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 4000000)
        self.assertEquals(len(serp['sn']), 9)

        self.assertEquals(serp['sn'][0]['d'], 'coral.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://www.coral.ru/')
        self.assertEquals(serp['sn'][0]['t'], u'Coral Travel - туроператор по Турции, России, Греции...')
        self.assertEquals(serp['sn'][0]['s'], u'Coral Travel - ведущий туроператор по Турции, России, Греции, Испании, Тунису! Поиск туров и бронирование туров онлайн прямо на сайте. Полная информация и любом отеле - цены, фото, видео, описание. ... Компания Coral Travel осуществляет мечты людей об идеальном отдыхе с 1995 года – уже 25 лет! Туроператор предлагает путешествия в 39 стран мира с вылетами из более 40 городов России. Скрыть')

        self.assertEquals(serp['sn'][8]['d'], '2gis.ru')
        self.assertEquals(serp['sn'][8]['u'], 'https://2gis.ru/moscow/search/Coral%20travel')
        self.assertEquals(serp['sn'][8]['t'], u'Coral Travel, сеть турагентств в Москве: филиалы — 2ГИС')
        self.assertEquals(serp['sn'][8]['s'], u'Coral Travel, сеть турагентств: все адреса на карте, телефоны, время работы, фото и отзывы. Проложите маршрут до нужного вам филиала.')

    def test127(self):
        html = self.get_data('2021-04-01-1.html')

        parser = YandexParser(html, exclude_market_yandex=False)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 6000000)
        self.assertEquals(len(serp['sn']), 15)

        self.assertEquals(serp['sn'][0]['d'], 'tatler.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://www.tatler.ru/heroes/andrej-molchanov-zhena-liza-soavtor-moej-zhizni')
        self.assertEquals(serp['sn'][0]['t'], u'Андрей Молчанов: «Жена Лиза — соавтор моей жизни»')
        self.assertEquals(serp['sn'][0]['s'], u'Сорокачетырехлетний Андрей Юрьевич так рассказывает про свою мечту, что по ходу интервью мне все больше хочется полезть в кошелек — сколько там сегодня, хватит ли хотя бы на ванную в однушке? Глава «Группы ЛСР» Андрей Молчанов. При этом Молчанов не считает нужным придумывать легенду о том, как со школой ездил на ЗИЛ с экскурсией и остался крайне впечатлен пятитонным грузовиком. Я из вежливости предложила ему эту опцию, он деликатно отказался. Как и от развития мысли о том, что филиал Эрмитажа в Москве был мечтой мальчика из культурной петербуржской семьи. Молчанов мне сказал, что «Даму в голубом» Гейнсборо не навещал, а полюбил и стал собирать искусство много позднее. Скрыть')

        self.assertEquals(serp['sn'][14]['d'], 'zampolit.com')
        self.assertEquals(serp['sn'][14]['u'], 'https://zampolit.com/dossier/molchanov-andrey-yurevich/')
        self.assertEquals(serp['sn'][14]['t'], u'Молчанов Андрей Юрьевич - компромат, биография...')
        self.assertEquals(serp['sn'][14]['s'], u'Молчанов Андрей Юрьевич - председатель Совета директоров ОАО "Группа ЛСР". Компромат и биография. ... Увлекается путешествиями и рыбалкой. СЕМЬЯ. Жена - Елизавета Молчанова. В семье Молчановых шестеро детей. АМБИЦИИ. Голые амбиции, лучше одетых поражений.Народная мудрость. ВЫБОРЫ. Вы выиграли выборы, а я — подсчет голосов.Анастасио Сомоса, президент Никарагуа. СОСТОЯНИЕ. Скрыть')

    def test128(self):
        html = self.get_data('2021-04-01-2.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], None)
        self.assertEquals(len(serp['sn']), 10)

        self.assertEquals(serp['sn'][0]['d'], 'santehmir.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://santehmir.ru/catalog/konvektory/konvektory_vnutripolnye/')
        self.assertEquals(serp['sn'][0]['t'], u'Конвекторы внутрипольные 🔥 купить в Москве по минимальным ценам.')
        self.assertEquals(serp['sn'][0]['s'], u'Купить конвекторы внутрипольные в Москве в интернет магазине Сантехмир. Официальный дилер, Гарантия до 10 лет. Звоните. ... Монтаж Все виды конвекторов нуждаются в обустройстве ниш в полу или стяжке. Скрыть')

        self.assertEquals(serp['sn'][9]['d'], 'pokupki.market.yandex.ru')
        self.assertEquals(serp['sn'][9]['u'], 'https://pokupki.market.yandex.ru/catalog/vstraivaemye-konvektory/73042/list')
        self.assertEquals(serp['sn'][9]['t'], u'Купить Встраиваемые конвекторы по низким ценам в интернет-магазинах на Яндекс.Маркете')
        self.assertEquals(serp['sn'][9]['s'], u'Встраиваемые конвекторы - купить на Яндекс.Маркете. Выбор товаров из категории Встраиваемые конвекторы по характеристикам, описанию и отзывам с удобной доставкой.')

    def test129(self):
        html = self.get_data('mobile-2021-04-05.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], None)
        self.assertEquals(len(serp['sn']), 8)

        self.assertEquals(serp['sn'][0]['d'], 'ru-wikipedia-org.turbopages.org')
        self.assertEquals(serp['sn'][0]['u'], 'https://ru-wikipedia-org.turbopages.org/ru.wikipedia.org/s/wiki/%D0%9F%D0%B8%D0%BB%D0%B0%D1%82%D0%B5%D1%81?turbo_uid=AACk7LWnpfPHVB__nIsNBDX-7w9VAfX0lruYsCLIID1ZS-pmA9qcO0EURs_0y06sKih0BIqD1tjGyu5sG94S7IB4vdsjdr0T07IKBKtFfjtrPix7&turbo_ic=AADH0_XzaZfJpmNXZGm1XW8W0_v3SZxgoKNLWkQqbHBu01tdvQTuQ4-ckcgm6IFcOI0fgodTRd6QHYSk4PCyQ3VQI3AA4WPnjFARopo_Ujtf_f9x&sign=49288c1b80ea83652ef21ae79642d2d70491cd7ca42672580a69b16f8d508919%3A1617575431&parent-reqid=1617575431173151-8257235980975655322-balancer-knoss-search-yp-sas-28-BAL&trbsrc=wb')
        self.assertEquals(serp['sn'][0]['t'], u'Пилатес — Википедия')
        self.assertEquals(serp['sn'][0]['s'], u'Пила́тес — система физических упражнений (фитнеса), разработанная Йозефом Пилатесом в начале XX века для реабилитации после травм.')

        self.assertEquals(serp['sn'][7]['d'], 'goodlooker.ru')
        self.assertEquals(serp['sn'][7]['u'], 'https://GoodLooker.ru/pilates.html')
        self.assertEquals(serp['sn'][7]['t'], u'Пилатес: польза, вред, советы. Пилатес для похудения.')
        self.assertEquals(serp['sn'][7]['s'], u'Пилатес – это серия упражнений для развития мышц всего тела, улучшения осанки и координации. Плюсы и минусы пилатеса, пилатес для похудения. Актуальные советы. ... В 1920-е годы тренер Джозеф Пилатес представил в Америке эффективный комплекс упражнений, который должен был помочь травмированным спортсменам и танцорам восстановиться и вернуться в свою прежнюю физическую форму. С тех самых пор и возникло направление пилатеса, которое обрело колоссальную популярность в последние 10-15 лет. Скрыть')

    def test130(self):
        html = self.get_data('mobile-2021-04-07.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], None)
        self.assertEquals(len(serp['sn']), 10)

        self.assertEquals(serp['sn'][0]['d'], 'ru.investing.com')
        self.assertEquals(serp['sn'][0]['u'], 'https://ru.investing.com/equities/american-intl-group')
        self.assertEquals(serp['sn'][0]['t'], u'AIG | Акции AIG - Investing.com')
        self.assertEquals(serp['sn'][0]['s'], u'Получите подробную информацию о акциях American International Group Inc (AIG) включая Цену, Графики, Теханализ, Исторические данные, Отчеты и др. AIG. ... Ниже вы найдете информацию о акциях American International Group Inc. Вы найдете другие подробности в разделах под этой страницей, такие, как исторические данные, графики, теханализ и другое. Пред. закр. 46,21. Скрыть')

        self.assertEquals(serp['sn'][9]['d'], 'finanz.ru')
        self.assertEquals(serp['sn'][9]['u'], 'https://www.finanz.ru/aktsii/american_international_group')
        self.assertEquals(serp['sn'][9]['t'], u'American International Group (AIG) Inc. - Курс акции - USD - NYSE')
        self.assertEquals(serp['sn'][9]['s'], u'Курс акций American International Group (AIG) [ISIN: US0268747849]. Котировки и графики в реальном времени. Новости. ... American International Group, Inc. (AIG) – одна из крупнейших в мире страховых компаний. Работает в 130 странах. В кризис 2008 года чуть не обанкротилась, и правительству США пришлось выдать ей кредит $85 млрд в обмен на почти 80% акций. Компания провела реструктуризация, подразделение по видам страхования, иным, чем страхование жизни, было выделено в отдельную компанию Chartis. Скрыть')

    def test131(self):
        html = self.get_data('mobile-2021-04-29.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 5000000)
        self.assertEquals(len(serp['sn']), 10)

        self.assertEquals(serp['sn'][0]['d'], 'lsr.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://www.LSR.ru/msk/zhilye-kompleksy/zilart/')
        self.assertEquals(serp['sn'][0]['t'], u'ЖК «Зиларт» | Официальный сайт | Группа ЛСР')
        self.assertEquals(serp['sn'][0]['s'], u'ЖК «ЗИЛАРТ» – уникальный проект бизнес-класса, строящийся в Даниловском районе Москвы. Это первый жилой комплекс, предлагающий жителям широчайший набор нестандартных опций, от просторного парка до собственного музея. Подробнее. ... В ЖК «ЗИЛАРТ» есть варианты с кладовыми и гардеробными комнатами, террасами, несколькими санузлами, просторными кухнями-гостиными. Треть территории комплекса будут занимать зеленые насаждения. Скрыть')

        self.assertEquals(serp['sn'][1]['d'], 'cian.ru')
        self.assertEquals(serp['sn'][1]['u'], 'https://www.cian.ru/kupit-kvartiru-zhiloy-kompleks-zilart-7889/')
        self.assertEquals(serp['sn'][1]['t'], u'1 166 объявлений - Купить квартиру в ЖК ЗИЛАРТ... - ЦИАН')
        self.assertEquals(serp['sn'][1]['s'], u'➜ Купите квартиру в ЖК ЗИЛАРТ на ЦИАН - 1 166 объявлений. Самая маленькая квартира: 25,5 м². Продажа квартир в ЖК ЗИЛАРТ по цене от 12,23 млн. руб. ... Мы нашли для вас 1,1 тыс. квартир в жк ЗИЛАРТ в Москве. Самый большой объект 136,1 м². Средняя стоимость продажи таких квартир - 22,56 млн. руб. Скрыть')

        self.assertEquals(serp['sn'][9]['d'], 'novostroy-m.ru')
        self.assertEquals(serp['sn'][9]['u'], 'https://www.Novostroy-m.ru/baza/mfk_zilart')
        self.assertEquals(serp['sn'][9]['t'], u'ЖК «ЗИЛАРТ»: ИПОТЕКА с господдержкой. 615 квартир...')
        self.assertEquals(serp['sn'][9]['s'], u'❗ЖК «ЗИЛАРТ», Даниловский: ✦цены на квартиры от 13 150 720 руб. ⬆291 отзыв покупателей о ЖК «ЗИЛАРТ». Вид из окон, эксклюзивные фото, съемки с воздуха, панорамы 360. ... Жилой комплекс бизнес-класса «ЗИЛАРТ» возводится застройщиком «Группа ЛСР» в рамках масштабного проекта освоения территории бывшего автомобильного завода им. Лихачева. Занимает более 65 гектар и примыкает к берегу Москвы-реки. Включает в себя 17 корпусов от 3 до 40 этажей. Скрыть')
        
    def test132(self):
        html = self.get_data('2021-05-24.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 11000000)
        self.assertEquals(len(serp['sn']), 10)

        self.assertEquals(serp['sn'][0]['d'], 'medi-salon.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://www.medi-salon.ru/')
        self.assertEquals(serp['sn'][0]['t'], u'ОРТОПЕДИЧЕСКИЕ САЛОНЫ medi официальный...')
        self.assertEquals(serp['sn'][0]['s'], u'Официальный интернет-магазин сети ортопедических салонов medi. Компрессионный трикотаж, бандажи, корсеты, ортезы и другие ортопедические товары из Германии.')

        self.assertEquals(serp['sn'][1]['d'], 'medi-salon.ru')
        self.assertEquals(serp['sn'][1]['u'], 'https://www.medi-salon.ru/salons/')
        self.assertEquals(serp['sn'][1]['t'], u'Ортопедические салоны medi в Москве')
        self.assertEquals(serp['sn'][1]['s'], u'Официальные ортопедические салоны medi в Москве: на карте, как добраться, режим работы, товары и услуги в салонах. ... Ортопедический салон medi (м. Академическая). Москва, ул. Дмитрия Ульянова, дом 16, корпус 1. Академическая. Скрыть')

        self.assertEquals(serp['sn'][9]['d'], 'zoon.ru')
        self.assertEquals(serp['sn'][9]['u'], 'https://zoon.ru/msk/shops/network/medi/')
        self.assertEquals(serp['sn'][9]['t'], u'Medi, салоны ортопедических товаров - 36 магазинов...')
        self.assertEquals(serp['sn'][9]['s'], u'Medi, салоны ортопедических товаров в Москве - мы нашли для вас 36 магазинов. Самый полный каталог заведений с фото, ☎️ и отзывами, удобный поиск мест на карте. ... Medi, салоны ортопедических товаров — это 36 заведений в различных местоположениях города. Medi, салоны ортопедических товаров осуществляет свою деятельность в различных категориях, в том числе магазины протезных и ортопедических товаров и многих других. Скрыть')

    def test133(self):
        html = self.get_data('mobile-2021-05-24.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], None)
        self.assertEquals(len(serp['sn']), 10)

        self.assertEquals(serp['sn'][0]['d'], 'gf-shop.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://gf-shop.ru/kanalizacionnye-nasosy')
        self.assertEquals(serp['sn'][0]['t'], u'Купить Канализационные насосы Grundfos с доставкой по всей России в фирменном магазине Grundfos')
        self.assertEquals(serp['sn'][0]['s'], u'В зависимости от модели канализационные насосы Грундфос применяются для перекачивания стоков в частных домах, коммерческих и промышленных зданиях. На какие параметры обратить внимание при покупке? Тип. Канализационные насосы Грундфос выпускаются нескольких видов, которые различаются по конструкции и выполняемым задачам. Канализационные установки. Модели этого типа отличаются небольшими размерами и простым обслуживанием. Скрыть')

        self.assertEquals(serp['sn'][1]['d'], 'gf-expert.ru')
        self.assertEquals(serp['sn'][1]['u'], 'https://gf-expert.ru/shop/pumps/kanalizacionnye-nasosnye-stancii/')
        self.assertEquals(serp['sn'][1]['t'], u'Купить канализационные насосы Грундфос в официальном магазине')
        self.assertEquals(serp['sn'][1]['s'], u'⭐⭐⭐⭐⭐Купить канализационные установки GRUNDFOS в нашем интернет-магазине✅ ЦЕНА ▶ от 7 400 руб. КАТАЛОГ ▶ 509 насосов Grundfos . ДОСТАВКА по ▶ Москве, России. ГАРАНТИЯ ▶ от 2 года. Звоните ☎ +7(499) 670-08-58. ... Канализационные установки Grundfos предназначены для выкачивания сточных жидкостей из ванной, раковины и унитаза частного дома. Благодаря автоматизированной работе насосов, можно полностью положиться на технику и не контролировать процесс. Скрыть')

        self.assertEquals(serp['sn'][9]['d'], 'topsantex.ru')
        self.assertEquals(serp['sn'][9]['u'], 'https://topsantex.ru/category/nasosnoe-oborudovanie/grundfos/kanalizatsionnye-nasosy/')
        self.assertEquals(serp['sn'][9]['t'], u'Канализационные насосы Grundfos (Грундфос) - купить фекальный насос в Москве')
        self.assertEquals(serp['sn'][9]['s'], u'Предлагаем купить канализационные насосы Grundfos (Грундфос) недорого в интернет-магазине Topsantex в Москве. Большой выбор, быстрая доставка во все регионы России, гарантия от производителя. Звоните! ☎: +7 (495) 664-6055. ... Кабели и адаптеры для скважинных насосов. Тросы и зажимы из нержавеющей стали. Гофры для труб. Скрыть')

    def test134(self):
        html = self.get_data('2021-08-23.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 20000000)
        self.assertEquals(len(serp['sn']), 10)

        self.assertEquals(serp['sn'][0]['d'], 'cian.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://www.cian.ru/kupit-kvartiru/')
        self.assertEquals(serp['sn'][0]['t'], u'Купить квартиру в Москве, продажа квартир недорого...')
        self.assertEquals(serp['sn'][0]['s'], u'➜ Купите квартиру в Москве на ЦИАН - 90 358 объявлений. Самая маленькая квартира: 19,5 м². Продажа квартир в Москве по цене от 5,24 млн. руб. ... Найдено 90,3 тыс. квартир в Москве. Самый просторный объект 249,29 м². Средняя цена продажи таких квартир - 15 млн. руб. Купить. Купить Снять Посуточно. Квартиру в новостройке и вторичке. Квартира в новостройке Квартира во вторичке Комната Доля Дом Часть дома Таунхаус Участок. Комнатность. Скрыть')

        self.assertEquals(serp['sn'][1]['d'], 'realty.yandex.ru')
        self.assertEquals(serp['sn'][1]['u'], 'https://realty.yandex.ru/moskva/kupit/kvartira/')
        self.assertEquals(serp['sn'][1]['t'], u'Купить квартиру в Москве - 96840 объявлений по...')
        self.assertEquals(serp['sn'][1]['s'], u'Более 96840 объявлений по продаже квартир по цене от 4 352 000 ₽. Карты доступности и инфраструктуры в Москве - купить квартиру на Яндекс.Недвижимости. ... Продается трёхкомнатная квартира (№781) в новостройке TopHILLS по адресу Москва, Электролитный пр-д, вл. 7а. Общая площадь квартиры - 67.61 кв.м. Тип проекта, по которому построен дом - монолит. Способы оплаты можно уточнить у продавца. Более. Скрыть')

        self.assertEquals(serp['sn'][9]['d'], 'msk.etagi.com')
        self.assertEquals(serp['sn'][9]['u'], 'https://Msk.Etagi.com/realty/')
        self.assertEquals(serp['sn'][9]['t'], u'Купить квартиру в Москве, 🏢 недвижимость, продажа...')
        self.assertEquals(serp['sn'][9]['s'], u'Купить квартиру в Москве. Звоните Проконсультируем. Сделаем подборку жилья для вас. Цены от 1 200 000 руб., площадь от 7.4 м² Квартиры на карте...')

    def test135(self):
        html = self.get_data('2022-01-31.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 14000000)
        self.assertEquals(len(serp['sn']), 15)

        self.assertEquals(serp['sn'][0]['d'], 'ru.wikipedia.org')
        self.assertEquals(serp['sn'][0]['u'], 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B8%D0%BC,_%D0%98%D0%B3%D0%BE%D1%80%D1%8C_%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B8%D1%87')
        self.assertEquals(serp['sn'][0]['t'], u'Ким, Игорь Владимирович — Википедия')
        self.assertEquals(serp['sn'][0]['s'], u'И́горь Ким — инвестор, банкир, заслуженный экономист Российской Федерации, успешно реализовавший более 30 сделок по приобретению и консолидации активов (M&A)...')

        self.assertEquals(serp['sn'][1]['d'], 'finparty.ru')
        self.assertEquals(serp['sn'][1]['u'], 'https://finparty.ru/personal/igor-kim/')
        self.assertEquals(serp['sn'][1]['t'], u'Игорь Ким биография и карьера в Экспобанк, последние...')
        self.assertEquals(serp['sn'][1]['s'], u'Ким Игорь Владимирович родился 12 января 1966 года в городе Уштобе в Казахстане. Окончил физико-математическую школу при Новосибирском государственном университете, а в 1990 году — НГУ по специальности «экономическая кибернетика». https://finparty.ru/personal/igor-kim/. finparty.ru. Игорь Ким. ... Приобретение Экспобанка. В 2011-м банкир вместе с партнерами выкупил Барклайс Банк, входящий в банковскую группу Barclays. После этого вернул банку первоначальное название — Экспобанк. В 2012-м ранее убыточный банк впервые получил прибыль в $40 млн и рентабельность капитала выше 20%. В 2012-м приобрел «ВестЛБ Восток» — дочерний банк европейского WestLB AG. Скрыть')

        self.assertEquals(serp['sn'][14]['d'], 'fb.ru')
        self.assertEquals(serp['sn'][14]['u'], 'https://FB.ru/article/463959/kim-igor-vladimirovich-bankir-biografiya-bankovskaya-deyatelnost-sostoyanie')
        self.assertEquals(serp['sn'][14]['t'], u'Ким Игорь Владимирович, банкир: биография...')
        self.assertEquals(serp['sn'][14]['s'], u'Ким Игорь Владимирович - уроженец Казахской ССР, города Уштобе. По национальности - кореец, чувствует свою принадлежность к этносу. В детстве это служило и знаком отличия, и поводом закалять характер. ... С декабря 2011 Игорь Владимирович становится председателем совета директоров банка ООО "Экспобанк". Через год (2012), у WestLB AG, одной организации банковского сектора ЕС, Игорь Ким купил дочерний WestLB Eas. Кроме того, у VR - Leasing - компанию FB-Leasing (позже присоединена к "Экспобанку"), а также LBBW Bank CZ (после сменил именование на Expobank CZ). Скрыть')

    def test136(self):
        html = self.get_data('2022-02-01.html')

        parser = YandexParser(html)
        serp = parser.get_serp()

        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(serp['pc'], 9000000)
        self.assertEquals(len(serp['sn']), 50)

        self.assertEquals(serp['sn'][0]['d'], 'cian.ru')
        self.assertEquals(serp['sn'][0]['u'], 'https://www.cian.ru/zhiloy-kompleks-luchi-moskva-8226/otzyvy/')
        self.assertEquals(serp['sn'][0]['t'], u'202 отзыва о ЖК Лучи в Москве')
        self.assertEquals(serp['sn'][0]['s'], u'Отзывы о ЖК «Лучи». 202 отзыва от жильцов и дольщиков. 3,9 - рейтинг на основе отзывов покупателей. Рейтинг от посетителей. 3,9202/5. ... К сожалению, являюсь дольщиком 3 корпуса ЖК Лучи. По ДДУ выдача ключей должна была быть до 30 сентября 2020. Выдача по моей секции не началась до сих пор. Скрыть')

        self.assertEquals(serp['sn'][1]['d'], 'realty.yandex.ru')
        self.assertEquals(serp['sn'][1]['u'], 'https://realty.yandex.ru/moskva_i_moskovskaya_oblast/kupit/novostrojka/luchi-214649/otzyvy/')
        self.assertEquals(serp['sn'][1]['t'], u'2247 отзывов — ЖК «ЛУЧИ». Достоинства, недостатки...')
        self.assertEquals(serp['sn'][1]['s'], u'Отзывы — ЖК «ЛУЧИ». Показать телефон. Застройщик «ЛСР. ... На самом то деле цены тут норм, я смотрел другие жк менее качественные, там цены просто .. Тут планирую приобрести жилую и коммерческую недвижимость. ЛАРИСА. Скрыть')

        self.assertEquals(serp['sn'][49]['d'], 'fb.ru')
        self.assertEquals(serp['sn'][49]['u'], 'https://FB.ru/article/336974/jk-luchi-otzyivyi-pokupateley')
        self.assertEquals(serp['sn'][49]['t'], u'ЖК "Лучи": отзывы покупателей')
        self.assertEquals(serp['sn'][49]['s'], 'ЖК "Лучи" (отзывы покупателей утверждают это!) практически всё нужное будет иметь на собственной территории, здесь найдётся всё, что душа пожелает. На территории располагается многофункциональный комплекс с салонами красоты, аптеками, магазинами, на освобождённых от автомобилей придомовых территориях можно превосходно отдыхать с детьми, заниматься спортом, выгуливать собак на специальной площадке. ... И если две школы на территории жилого комплекса чем-то родителей не устроят, то в шаговой доступности находится десяток других школ и гимназий, бассейны, поликлиники и больницы, сетевые супермаркеты. Ход строительства. Скрыть')

    def test137(self):
        html = self.get_data('2022-04-04.html')

        parser = YandexParser(html)
        captcha = parser.get_captcha_data()

        self.assertEquals(captcha['captcha_type'], 'i_not_robot')
        self.assertEquals(captcha['form_action'], '/checkcaptcha?key=efaadba2-708d9a77-d9f55ec2-aef402d_2%2F1649062316%2F073520a45db9eb1df8ef48d1c118afca_b36e70232e52e9d77f42bfa4058894a9&retpath=https%3A%2F%2Fyandex.kz%2Fsearch%3Ftext%3D%25D0%25B6%25D0%25BA%2B%25D0%25BC%25D0%25BE%25D1%2581%25D0%25BA%25D0%25B2%25D0%25B0%2B%25D0%25B0101%2B%25D0%25BE%25D1%2582%25D0%25B7%25D1%258B%25D0%25B2%25D1%258B%2B%25D0%25B6%25D0%25B8%25D0%25BB%25D1%258C%25D1%2586%25D0%25BE%25D0%25B2%26lr%3D213%26suggest_reqid%3D180497601164420590723001485819544%26numdoc%3D50_cde7119087e85fcca0ad87d77b0dc3e3&u=543bf183-99e0b6f-abcb4f60-1f02f7b6')
        self.assertEquals(captcha['form_data']['k'], '1_1649062316_8393789921230861190_883f13b34055a08f7ac6e3cabbba3f73')
        self.assertEquals(captcha['form_data']['d'], '72aLqyFE2IuvJTjB3FR2AlEkKXOhAO8rw0BbmKD2LaA=')
        self.assertEquals(captcha['form_data']['key'], 'efaadba2-708d9a77-d9f55ec2-aef402d_2/1649062316/073520a45db9eb1df8ef48d1c118afca_b36e70232e52e9d77f42bfa4058894a9')
        self.assertEquals(captcha['form_data']['rdata'], 'lETqmgN++vnaCGqU/nhUY2MGE1GDLM1K8GJhupLGHZPfV7ucA2j66psHAuOuIVtQBApbBo9lgQaWE3X9ztQBgo5TqZEDA73oxEoa7f41QCBrFAVRwDfNEaUhN+vF2g/B10SxzUAoq+6DB1n4/m4QYz1XTF+DYt4J+SY69NOTAYKNVKmRRyW0+MoJGqPvdkxkMEhaFo0ijR/hej35zIVIjM0EvokbIrnn3EAU475iVDg3RUUAxCzNSfRiYf7Bml7Fw0TpkwN+vurDVl3t/jZPIGtCSB/SZcMJoHF5opPFAYKMVKmRA3XhuZ9dCfHuYFQuc0caUZsi2B37OGqoksIPjM0Fv4kbMKr+ygkaoul2THYjUUxfg2PZCflyb7SClRqC1RL53kRo+uiXBwLy8HYSMHMeHV+DZNwJ+SY69NOTAYKLUqmRVTat7oMHXPT+bgJwJEEFUcU3zRHucWOojNRJmM1cqZoPIrnn3EAWp704BWdzCAsXmCLVX7E1PrSCkxyC1QDqx1Ih9KnKFxr7ujUacTQICxaSItVfsTU+tIKTGYLVEvneRGj67poHAqe9OAVnfQZMRYM6m1m2JXe6xcEPmpsU/s4NZr2zjR9Ms6kxWiA0HQtJ1XKaTu9iPamCzEvBgxXuhwMi6qmVUUq0uXhUZGIGExXAbJxO72I9rILMWdKaA6eJR3H6sclEVLK5eFRkZwYTFcBsnE7vYj2vgsxLwYMV7ocDIuCplUNZra8xWiA3HQtJ1XKaTu9iPKmCzEvBgxXuhwMj6qmVQ1mtrzFaIDYXC0nVcppO72I8rILMS8GDFe6HAyPtqZVRSrS5eFRlZwYTB9N1igfhJ2y6moJf1YpKqcwZZuL/3VBd7f4zTyBrUFsGxCzNQ/JiYf7Bml7Fw0TjmQN+vurDVl3t/jxFIGtCSB/SZcMJq3R5osaXQdOKSqnDFGbi/91QXe3+PEAga0JIH9Jlwwmrd3migr9BzIoB6scBLbb9wEZZtbU7GCB9BkFLgzqJSq8zPrSCnhSC1QDqx1Ih9KnGFBr7qCYDZ30GQEGDOptZtiV3usnFD5qJB+fYRGj64psHAqe9OAVnfQZARoM6iUqvMz60goAPms1QpZgPdfr2')
        self.assertEquals(captcha['form_method'], 'POST')


    def _print_context_sn(self, serp):
        for sn in serp['sn']:
            print
            print sn['u']
            print sn['t']
            print sn['vu']
            print sn['a']

    def _print_sn(self, serp):
        for sn in serp['sn']:
            print sn['p'], sn['d'], sn['u'], sn['t'], sn['s']

if __name__ == '__main__':
    unittest.main()
