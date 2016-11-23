# -*- coding:utf-8 -*-
import unittest

from yandex_parser.exceptions import YandexParserError
from yandex_parser.tests import YandexParserTests
from yandex_parser.yandex import YandexParser
from yandex_parser.yandex_bar import YandexBarParser
from yandex_parser.yandex_suggest import YandexSuggestParser


class YandexParserTestCase(YandexParserTests):

    def test_captcha_1(self):
        html = self.get_data('captcha_1.html')
        parser = YandexParser(html)

        captcha_data = parser.get_captcha_data()
        exp = {
            'url': u'http://yandex.ru/captchaimg?aHR0cDovL3MuY2FwdGNoYS55YW5kZXgubmV0L2ltYWdlP2tleT1kM1I3SDhDRGlTT3RlVzNvYk9zcFo4bk1lc0NOUjhXQw,,_0/1435077202/853e18711cde74266e45da1315dacee2_2bf39001bd241d1c6539b7db6a0464ad', 
            'form_action': '/checkcaptcha',
            'form_data': {
                'key': 'd3R7H8CDiSOteW3obOspZ8nMesCNR8WC_0/1435077202/853e18711cde74266e45da1315dacee2_ff263da232b103004f79fe4c4e139913', 
                'retpath': 'http://yandex.ru/yandsearch?p=0&text=%D0%BA%D0%BE%D0%BC%D0%BC%D0%B5%D1%80%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5+%D0%B1%D0%B0%D0%BD%D0%BA%D0%B8&site=&numdoc=50&lr=213_cefc8bbe530fbaf69685556720f14a26'
            }
        }
        self.assertTrue(YandexParser.is_yandex(html))
        self.assertEquals(captcha_data, exp)
   
       
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

    def _print_context_sn(self, serp):
        for sn in serp['sn']:
            print
            print sn['u']
            print sn['t']
            print sn['vu']

    def _print_sn(self, serp):
        for sn in serp['sn']:
            print sn['p'], sn['d'], sn['u'], sn['t'], sn['s']

if __name__ == '__main__':
    unittest.main()
