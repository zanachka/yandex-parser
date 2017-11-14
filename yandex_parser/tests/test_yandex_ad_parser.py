# -*- coding:utf-8 -*-
import unittest

from yandex_parser.yandex_ad_parser import YandexAdParser
from yandex_parser.tests import YandexParserTests


class YandexAdParserTestCase(YandexParserTests):

    def test1(self):
        html = self.get_data('ad-2017-11-14.html')
        parser = YandexAdParser(html)
        pc = parser.get_pagecount()
        self.assertEquals(pc, 74)

    def test2(self):
        html = self.get_data('ad-2017-11-14-empty.html')
        parser = YandexAdParser(html)
        pc = parser.is_not_found()
        self.assertEquals(pc, True)

    def test3(self):
        html = self.get_data('ad-2017-11-14-one.html')
        parser = YandexAdParser(html)
        pc = parser.get_pagecount()
        self.assertEquals(pc, 1)

    def test4(self):
        html = self.get_data('ad-2017-11-14-empty.html')
        parser = YandexAdParser(html)
        serp = parser.get_serp()
        self.assertEquals(serp['pc'], 0)
        self.assertEquals(serp['sn'], [])

    def test5(self):
        html = self.get_data('ad-2017-11-14-one.html')
        parser = YandexAdParser(html)
        serp = parser.get_serp()
        self.assertEquals(serp['pc'], 1)
        self.assertEquals(len(serp['sn']), 1)

        self.assertEquals(serp['sn'][0]['t'], u'Швейные машины Husqvarna. / damadoma.ru')
        self.assertEquals(serp['sn'][0]['s'], u'Все модели Husqvarna с бесплатной доставкой в любой город России. Гарантия!')
        self.assertEquals(serp['sn'][0]['u'], 'http://yabs.yandex.ru/count/2OA5WlL-Hwm40000gO10ZhUphA05MXoL0Pi1RaEt0Ye1YB5fBJ41YPNe0fW7dQNrkm6c4egj1pcstAdynlozfx3gxAekfQkza0AygVx30eq1tG7Ua2JqzBGNKSy6aR-q3JWAamAYXGsP1KACcE42jeJTjOYxe9ZX0g-OuGApYBkqYBlPcE42seYxfugzgAkPdREkyt82eCgbzzm5iG6on1000a08-VDo0g3AfVVS1Vm6kQNrkm6xxG2VILfOekB1__________yFmlqSwKtzY7s90iME3zC2xW7RxO1HC6bOekBV0l2W061evP3oA-s3AFNIEukmDN82zjcN7ZNptbNxcE42UHy0?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E')

    def test6(self):
        html = self.get_data('ad-2017-11-14.html')
        parser = YandexAdParser(html)
        serp = parser.get_serp()
        self.assertEquals(serp['pc'], 74)
        self.assertEquals(len(serp['sn']), 10)

        self.assertEquals(serp['sn'][0]['t'], u'Купите стол AERO − Большой выбор - 500+ моделей столов!')
        self.assertEquals(serp['sn'][0]['s'], u'В наличии − От 6900р. Онлайн-магазин столов и стульев!')
        self.assertEquals(serp['sn'][0]['u'], 'http://yabs.yandex.ru/count/Bt863Bkef8440000gO10ZhePhA05MXoL0Pi1RaEt0Ye1YB8SBm04YRkhDuO1dPiT4AO_YhIz87OFtBC6h0OGlR8ERo4AgYwbeFdL3hoebJiEZG7T0TwG9FIHkZy03GMJ0gA53Pa5GeoPGzEsaM4_jP6sDQ2hIQm1hvb3qxEGusoqaROrsPqarjgOSJQKbXuAfvRS2AYmG5bp1wxth42CBFhIt0Mn0RB44002G0Zvzwn0Z2pwqjm5_0QvcnqGk-q0dqbQMABYmV__________3yBnJUVJ5lC3Y0Z5Zm_J0ku1s-s0KJ1fMABYtmBme01WQEMGyYljWoZro07qNdMizjKIDmhgtbNxcKFJVny0?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB')

        self.assertEquals(serp['sn'][1]['t'], u'Купить столы по суперцене! - Купить столы в кухню.')
        self.assertEquals(serp['sn'][1]['s'], u'Высокое качество. Низкие цены. Скидки! Закажите!')
        self.assertEquals(serp['sn'][1]['u'], 'http://yabs.yandex.ru/count/Bt8632X1Aau40000gO10ZhePhA05MXoL0Pi1RaEt0Ye1CeYr3SBG0ucok8ml0vsiXIuMfZoAkMWwYmpSkWxDW0szjsyCsGYgBgMjuOmClA_qNmsD0Tq1tf0azFIyVnsnA96wFm0D1PC2eeKDcGL2Z9L3qxQGOJ-raBOre9L3qw-LGzEpaBOrj92sDTcLGzFQaBOrb9RW2QUNr0wee_mE6wxth42CBFhIt0Mn0RB4400200Zvzwn0Z2pwqjm5_0Qvh8Kk5hlj09z9MbYYui7__________m_2yKtdqnRp0uW8nOyFp0NJ0ku1s-s0KJ1fMABYtmBme01WQEMGyYljWoZro07qNdMizjKIDmhgtbNxbKFJU240?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB')

        self.assertEquals(serp['sn'][9]['t'], u'Купить кухонные столы, обеденные, раздвижные: фото...')
        self.assertEquals(serp['sn'][9]['s'], u'Доступные цены! Огромный ассортимент мебели в интернет-магазине СТОЛПЛИТ.')
        self.assertEquals(serp['sn'][9]['u'], 'http://yabs.yandex.ru/count/Bt8636ojg2a40000gO10ZhePhA05MXoL0Pi1RaEt0Ye1EW68jEzAm0Q9yo6woOD5qoKAdPM25vgODc6cWGYAjdm1PHEzkUdCKGkgBgMWbXWGlAmsoWgD0Tq1tf0azFIODc6HkZy03GMJ0gA53Pa5GeoGdZcsa4aHjP2c3g2GdZcla9uviv2c3hIGfWxPa9uvsf2c3fIJy0Idc989gBh0ew02hlUiG8mi-jBS1R47iiGGG0902Fdth42CBFhIt0Ny1hcLWXUxxG2VILfOekB1__________yFml5DvzCMymE82CMF3ys-8cXa4ywrTDEr4jC2xW7RxO1HC6bOekBV0l2W061eyfBfgkMGyYljWoZro07qNdMizjKIDmhgtbNxa9uvVo80?q=%D0%BA%D1%83%D0%BF%D0%BB%D1%8E+%D1%81%D1%82%D0%BE%D0%BB')

    def _print_sn(self, serp):
        for sn in serp['sn']:
            print sn['p']
            print sn['t']
            print sn['s']
            print sn['u']
            print

if __name__ == '__main__':
    unittest.main()
