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
        self.assertEquals(serp['sn'][0]['s'], u'Дром Спецтехника и грузовики: объявления о продаже и покупке Купить автобус б/у или новый. ... Автобус Higer KLQ 6928 Q 35 мест 2013 год Москва, 6 700 куб. см., 35 мест. Читать еще')

        self.assertEquals(serp['sn'][1]['d'], 'm.irr.ru')
        self.assertEquals(serp['sn'][1]['u'], 'http://m.irr.ru/cars/commercial/buses/')
        self.assertEquals(serp['sn'][1]['t'], u'Автобусы в Москве и области продажа, цены | купить автобус...')
        self.assertEquals(serp['sn'][1]['s'], u'ИЗ РУК В РУКИ - Коммерческий транспорт в Москве и области. Купить автобус б/у или новый - частные объявления и предложения дилеров. Читать еще')

        self.assertEquals(serp['sn'][2]['d'], 'farpost.ru')
        self.assertEquals(serp['sn'][2]['u'], 'http://www.farpost.ru/moskva/auto/spectech/bus/')
        self.assertEquals(serp['sn'][2]['t'], u'Купить АВТОБУС в Москве. Новый или БУ автобус. Цены. Фото.')
        self.assertEquals(serp['sn'][2]['s'], u'Купить автобус в Москве. Продажа автобусов в Москве с фото. Аукционные, новые и б.у. Производство: Корея, Япония, Китай, Россия и др. Читать еще')

        self.assertEquals(serp['sn'][49]['d'], 'moskva.regmarkets.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://moskva.regmarkets.ru/igrushechnye-avtobusy-11419/')
        self.assertEquals(serp['sn'][49]['t'], u'Игрушечные автобусы модели, паз, лиаз купить в Москве.')
        self.assertEquals(serp['sn'][49]['s'], u'Чтобы узнать, как купить модель игрушечного автобуса паз, с открывающимися дверями в Москве по доступной цене, воспользуйтесь нашим сервисом. Читать еще')

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
        self.assertEquals(serp['sn'][0]['s'], u'Ноутбуки для бизнесаМаксимальные возможности и свобода передвижений для вас и вашего бизнеса. Вам не обязательно все время находиться на рабочем месте. Читать еще')

        self.assertEquals(serp['sn'][49]['d'], 'chel.blizko.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://chel.blizko.ru/predl/computer/computer/notebook/noutbuki')
        self.assertEquals(serp['sn'][49]['t'], u'Ноутбуки Acer в Челябинске - Портал выгодных покупок BLIZKO.ru')
        self.assertEquals(serp['sn'][49]['s'], u'Вам нужно купить в Челябинске ноутбук марки Acer? Данную задачу будет легко решить с помощью раздела «Ноутбуки». ... Каталог актуальных акций и распродаж. Читать еще')

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
        self.assertEquals(serp['sn'][0]['s'], u'Интернет магазин Связной предлагает ознакомиться с каталогом мобильных телефонов, в котором представлены модели с ценами от 1 390 до 76 890 рублей. Читать еще')

        self.assertEquals(serp['sn'][49]['d'], 'lorena-kuhni.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://lorena-kuhni.ru/catalog/')
        self.assertEquals(serp['sn'][49]['t'], u'Каталог')
        self.assertEquals(serp['sn'][49]['s'], u'Каталог. «Современная коллекция/Модерн» (17) «Городская классика» (18) «Классика» (20). Если классика – вне моды, то модерн всегда на самом ее пике. ... Отправить отзыв директору. Ваше имя*. Телефон*. Читать еще')

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
        self.assertEquals(serp['sn'][0]['s'], u'Бесплатные объявления о продаже мобильных телефонов iPhone 7, Айфон 6, iPhone 6S, 5SE, iPhone 5S, 5C, Айфон 5, 4S 4 в Самарской области. ... Самара. Вчера, 21:59. Айфон 4s 8Гб. Читать еще')

        self.assertEquals(serp['sn'][49]['d'], 'electronics.wikimart.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://electronics.wikimart.ru/communication/cell/tag/iphone4/')
        self.assertEquals(serp['sn'][49]['t'], u'Купить iPhone 4 в Москве в интернет магазине. Айфон 4: цены...')
        self.assertEquals(serp['sn'][49]['s'], u'7 моделей Apple iPhone 4 от 5335 руб. в наличии! Покупайте Apple iPhone 4 ✈✈✈ с доставкой на Викимарт. ... Apple iPhone 4 отличаются дорогими высококачественными материалами, большим количеством приложений и функций. Читать еще')

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
        self.assertEquals(serp['sn'][0]['s'], u'Продажа MP3-плееров SONY (Сони). ... В интернет-магазине ЭЛЬДОРАДО можно купить MP3-плеер Сони с гарантией и доставкой. Читать еще')

        # Тут внимание - пустой заголовок сниппета
        self.assertEquals(serp['sn'][40]['d'], 'sportlifeabout.ru')
        self.assertEquals(serp['sn'][40]['u'], 'http://sportlifeabout.ru/1/useful-articles/74-obzor-pleera-sony-nw-w273')
        self.assertEquals(serp['sn'][40]['t'], None)
        self.assertEquals(serp['sn'][40]['s'], u'В отличие от большинства других плееров Сони, изобилующих различными опциями — одни из которых делают звук «кристально чистым»... Читать еще')

        self.assertEquals(serp['sn'][49]['d'], 'vk.com')
        self.assertEquals(serp['sn'][49]['u'], 'https://vk.com/topic-35092860_28777272')
        self.assertEquals(serp['sn'][49]['t'], u'компьютер не "видит" плеер |  Sony NWZ-E463 / NWZ-E464...')
        self.assertEquals(serp['sn'][49]['s'], u'Последнее время массово компьютеры перестают видеть плееры от сони, вся проблемА в прошивке у плеера... Читать еще')

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
        self.assertEquals(serp['sn'][0]['s'], u'Закрыть. Шапка. Samsung Galaxy S2. Диагональ дисплея:4.3. ... Быстро привык к оболочке Самсунга. Хорошая цена. Беспокоит Андроид - вопросы постоянных прошивок и прочий геммор, при поддержке Самса - это реализовано не совсем идеально. Читать еще')

        self.assertEquals(serp['sn'][49]['d'], '1galaxy.ru')
        self.assertEquals(serp['sn'][49]['u'], 'http://www.1galaxy.ru/mobilnye-ustrojstva/')
        self.assertEquals(serp['sn'][49]['t'], u'Мобильные устройства Samsung Galaxy')
        self.assertEquals(serp['sn'][49]['s'], u'Новый флагман Samsung - Galaxy S7 Edge. Высокотехнологичный дизайн, покрытие 2,5 D Очень стильный и удобный смартфон с невероятно тонким корпусом. Samsung предлагает несколько цветов для вашего корпуса. Читать еще')

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
