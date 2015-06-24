# -*- coding:utf-8 -*-
import unittest
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
            'form_data': {
                'key': 'd3R7H8CDiSOteW3obOspZ8nMesCNR8WC_0/1435077202/853e18711cde74266e45da1315dacee2_ff263da232b103004f79fe4c4e139913', 
                'retpath': 'http://yandex.ru/yandsearch?p=0&text=%D0%BA%D0%BE%D0%BC%D0%BC%D0%B5%D1%80%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B5+%D0%B1%D0%B0%D0%BD%D0%BA%D0%B8&site=&numdoc=50&lr=213_cefc8bbe530fbaf69685556720f14a26'
            }
        }
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
        self.assertEquals(parser.get_region_code(), 213)

    def test_pagination_exists_1(self):
        html = self.get_data('serp_1.html')
        parser = YandexParser(html)
        self.assertTrue(parser.pagination_exists())

    def test_pagination_exists_2(self):
        html = self.get_data('serp_3.html')
        parser = YandexParser(html)
        self.assertFalse(parser.pagination_exists())

    def test_pagecount_1(self):
        html = self.get_data('serp_1.html')
        parser = YandexParser(html)
        self.assertEquals(parser.get_pagecount(), 124000000)

    def test_pagecount_2(self):
        html = self.get_data('serp_2.html')
        parser = YandexParser(html)
        self.assertEquals(parser.get_pagecount(), 354000)

    def test_pagecount_3(self):
        html = self.get_data('serp_3.html')
        parser = YandexParser(html)
        self.assertEquals(parser.get_pagecount(), 22)

    def test_not_found(self):
        html = self.get_data('not_found_1.html')
        parser = YandexParser(html)
        self.assertTrue(parser.is_not_found())
    
    def test_serp_1(self):
        html = self.get_data('serp_1.html')
          
        parser = YandexParser(html)
        serp = parser.get_serp()
          
        self.assertFalse(parser.is_not_found())
          
        self.assertEquals(serp['pc'], 124000000)
        self.assertEquals(len(serp['sn']), 51)
         
        for i, sn in enumerate(serp['sn']):
            exp_sn = serp_1_snippets[i]
#             print '({}, "{}", u"{}", u"{}", {}, {}),'.format(sn['p'], sn['u'], sn['t'].replace('"', '\\"'), sn['s'].replace('"', '\\"'), sn['m'], sn['i'])
            
            self.assertEquals(sn['p'], exp_sn[0])
            self.assertEquals(sn['u'], exp_sn[1])
            self.assertEquals(sn['t'], exp_sn[2])
            self.assertEquals(sn['s'], exp_sn[3])
            self.assertEquals(sn['m'], exp_sn[4])
            self.assertEquals(sn['i'], exp_sn[5])

    def test_serp_2(self):
        html = self.get_data('serp_2.html')
          
        parser = YandexParser(html)
        serp = parser.get_serp()
          
        self.assertFalse(parser.is_not_found())
          
        self.assertEquals(serp['pc'], 354000)
        self.assertEquals(len(serp['sn']), 50)
         
        for i, sn in enumerate(serp['sn']):
            exp_sn = serp_2_snippets[i]
#             print '({}, "{}", u"{}", u"{}", {}, {}),'.format(sn['p'], sn['u'], sn['t'].replace('"', '\\"'), sn['s'].replace('"', '\\"'), sn['m'], sn['i'])
            
            self.assertEquals(sn['p'], exp_sn[0])
            self.assertEquals(sn['u'], exp_sn[1])
            self.assertEquals(sn['t'], exp_sn[2])
            self.assertEquals(sn['s'], exp_sn[3])
            self.assertEquals(sn['m'], exp_sn[4])
            self.assertEquals(sn['i'], exp_sn[5])

    def test_serp_3(self):
        html = self.get_data('serp_3.html')
          
        parser = YandexParser(html)
        serp = parser.get_serp()
          
        self.assertFalse(parser.is_not_found())
          
        self.assertEquals(serp['pc'], 22)
        self.assertEquals(len(serp['sn']), 15)
         
        for i, sn in enumerate(serp['sn']):
            exp_sn = serp_3_snippets[i]
#             print '({}, "{}", u"{}", u"{}", {}, {}),'.format(sn['p'], sn['u'], sn['t'].replace('"', '\\"'), sn['s'].replace('"', '\\"'), sn['m'], sn['i'])
            
            self.assertEquals(sn['p'], exp_sn[0])
            self.assertEquals(sn['u'], exp_sn[1])
            self.assertEquals(sn['t'], exp_sn[2])
            self.assertEquals(sn['s'], exp_sn[3])
            self.assertEquals(sn['m'], exp_sn[4])
            self.assertEquals(sn['i'], exp_sn[5])

#     def test_captcha_found(self):
#         html = self.get_data('not_found_1.html')
#         self.assertTrue(YandexParser(html).is_not_found())
# 
#     def test_blocked(self):
#         pass
# 
serp_1_snippets = [
    (1, "http://www.okna.ru/", u"\"Kaleva\" - продажа и установка пластиковых окон", u"Информация о фирме и услугах: продажа и установка пластиковых окон и дверей, остекление балконов и лоджий. Фотографии и описания типов окон. Оконный калькулятор on-line. Цены. Адреса магазинов.", False, False),
    (2, "http://www.FabrikaOkon.ru/", u"\"Фабрика окон\" - изготовление пластиковых окон", u"Производство и установка плаcтиковых окон, остекление балконов и лоджий. Цены, калькулятор стоимости. Онлайн-заказ. Возможность покупки в рассрочку. Текущие акции и скидки.", False, False),
    (3, "http://oknabm.ru/", u"\"Бизнес-М\" - продажа пластиковых окон и дверей", u"Изготовление и установка окон из ПВХ Veka, алюминиевых окон, остекление балконов. Консультация специалиста по выбору пластиковых окон. Калькулятор для расчета стоимости. Адреса офисов.", False, False),
    (4, "http://www.plastika-okon.ru/", u"Пластиковые окна ПВХ купить недорого в Москве со...", u"Хотите заказать недорогие пластиковые окна в Москве? ... Компания «Пластика окон» уже 13 лет специализируется на изготовлении, продаже и установке дешевых...", False, False),
    (5, "http://www.ZavodskieOkna.ru/", u"\"Заводские Окна\" - пластиковые окна", u"Производство и установка окон ПВХ из профилей KBE, Rehau, Trocal; остекление балконов и лоджий системами Slidors и Provedal. Цены. Калькулятор расчета стоимости заказа. Онлайн-запись на замер.", False, False),
    (7, "http://www.EuroOkna.ru/", u"Пластиковые окна ПВХ: ...от производителя № 1 в Москве....", u"Готовые пластиковые окна полностью соответствуют международным стандартам и отлично подходят под местные климатические условия.", False, False),
    (8, "http://www.ecookna.ru/", u"\"Экоокна\" - пластиковые окна и двери", u"Производство пластиковых окон и дверей, остекление балконов и лоджий, изготовление зимних садов и др. Онлайн-расчет стоимости окна. Информация о скидках. Адреса офисов продаж.", False, False),
    (9, "http://sobesednik.ru/proisshestviya/20150623-malchik-vypal-iz-okna-v-voskresenske-iz-za-moskitnoy-setki", u"Мальчик выпал из окна в Воскресенске из-за москитной...", u"3 часа назадsobesednik.ru›proisshestviya/20150623…vypal…okna…Сохранённая копияПожаловатьсяШестилетний мальчик выпал из окна третьего этажа жилого дома в подмосковном Воскресенске. Ребёнок лежит в реанимации.", False, False),
    (10, "http://maps.yandex.ru/?source=wizbiz-new&text=%D0%BE%D0%BA%D0%BD%D0%B0&sll=37.7818%2C55.6694&maxspn=0.833332%2C0.530138&sspn=0.833332%2C0.530138&sctx=BgAAAAEDowG8BRLkQkCh%2BDHmrtVLQIy61t6nquo%2FOL2L9%2BP24D8CAAAAAQIBAAAAAAAAAAEM6%2BZDiEbZ59UAAAABAACAPw%3D%3D", u"Окна в Москве и области", u"123456789На большую картуКарта загружается   Точное местоположение определить не удалось.", True, False),
    (11, "http://www.OknaRosta.ru/", u"\"Окна Роста\" - продажа пластиковых окон", u"Пластиковые окна, алюминиевые конструкции, деревянные окна. Описание продукции. Конструктор окон и расчет стоимости онлайн. Список дилеров. Контакты.", False, False),
    (12, "http://www.Okna-Lider.com/", u"\"Окна лидер\" - пластиковые окна и двери", u"Производство пластиковых окон, входных дверей, металлических решеток на окна, остекление балконов, устройство натяжных потолков. Цены. Условия доставки, оплаты и сроки изготовления. Контакты.", False, False),
    (13, "http://www.Plastok.ru/", u"\"Пласток\" - пластиковые окна и двери", u"Производство и продажа окон, балконных дверей, комплектующих к ним, а также поставки жалюзей и штор, кондиционеров и др. Цены. Адреса мест продаж.", False, False),
    (14, "http://www.okna-plastek.ru/", u"Окна пвх из Германии, купить окна пвх в москве, немецкие...", u"Мы рекомендуем обратить внимание на немецкие окна Саламандра, в Москве их продажей занимаются несколько компаний, но большинство из них, в отличие от нас...", False, False),
    (15, "http://www.oknaprosvet.ru/", u"\"Просвет\" - пластиковые окна", u"Производство, продажа и монтаж окон из профилей Rehau и Provedal, остекление балконов и лоджий. Цены. Информация для дилеров. Контакты.", False, False),
    (16, "http://www.OknaMaster.ru/", u"\"Окна Мастер\" - продажа пластиковых окон", u"Изготовление и установка окон из ПВХ, полный комплекс услуг по монтажу; остекление фасадов, лоджий и балконов. Адреса офисов.", False, False),
    (17, "http://oknovam.ru/", u"Галерея окон - ...окна по дешевым ценам в Москве...", u"Заказать пластиковые окна в Москве по выгодной цене и превосходному качеству вам поможет компания «Галерея окон».", False, False),
    (18, "http://www.OknaKomforta.ru/", u"\"Окна Комфорта\" - пластиковые окна", u"Производство пластиковых окон из профилей Veka, остекление балконов и лоджий. Онлайн-калькулятор стоимости окон. Условия продажи в кредит.", False, False),
    (19, "http://Okna-Magnit.ru/", u"\"Окна-Магнит\" - изготовление пластиковых окон", u"Оптовая поставка ПВХ-профиля и комплектующих для производства пластиковых окон, собственное производство окон, остекление балконов и лоджий. Форма для вызова замерщика. Контакты.", False, False),
    (20, "http://www.MosOkna.ru/", u"Пластиковые окна - ...пластиковые окна на заказ в Москве", u"Московские окна — крупнейший производитель пластиковых окон в России. Современное автоматизированное производство по запатентованным технологиям...", False, False),
    (21, "http://www.sm-okna.ru/", u"\"Строй Мастер\" - пластиковые окна", u"Изготовление и установка окон из немецкого профиля Rehau, остекление лоджий и балконов. Каталог продукции. Калькулятор стоимости окон. Контакты.", False, False),
    (22, "http://www.veka.ru/", u"\"Veka\" - производитель окон и дверей", u"Описание продукции: оконные профильные системы, двери, рольставни, декоративные перекладины и пр. Адреса представительств.", False, False),
    (23, "http://torg.mail.ru/okna/", u"Окна - где купить по выгодным ценам. Характеристики...", u"Самый большой выбор где купить окна - 357 предложений. Информация по отзывам и магазинам на Товары@Mail.ru.", False, False),
    (24, "http://www.hobbit.ru/", u"Пластиковые окна в Москве от производителя заказать...", u"качественные пластиковые окна производятся на заводе с 1992 года ... офисы продаж и выставочные стенды пластиковых окон от производителя в крупных ТЦ Москвы и...", False, False),
    (25, "http://www.OknaLux.ru/", u"Пластиковые окна пвх Thyssen, KBE в Москве недорого...", u"Пластиковые окна с витражным стеклом. Витражи на окнах украсят вашу квартиру или дом. Пластиковые окна для ресторана. Установлены окна пвх в ресторане.", False, False),
    (26, "http://www.Okna5.ru/", u"\"Отличные окна\" - изготовление пластиковых окон", u"Изготовление, монтаж и обслуживание окон и дверей из ПВХ. Система расчета стоимости и онлайн-заказа. Сведения о компании. Контакты.", False, False),
    (27, "http://www.ramokna.ru/", u"\"РАМокна\" - пластиковые окна", u"Продажа, ламинация и установка пластиковых окон, остекление балконов и лоджий. Цены. Контакты.", False, False),
    (28, "http://www.oknasok.ru/", u"\"Самарские оконные конструкции\" - окна из ПВХ", u"Производство и установка пластиковых окон, подоконников и дверей, оптовая продажа профиля SOK и конструкций из него. Калькулятор для расчета стоимости окон. Контакты.", False, False),
    (29, "http://okna-kurs.ru/", u"Продажа деревянных окон для квартиры на заказ в Москве", u"Купить деревянные окна в Москве вовсе не составит труда, если воспользоваться услугами компании «Курс».", False, False),
    (30, "http://Avrora-Okna.ru/", u"\"Аврора-Окна\" - пластиковые и деревянные окна", u"Продажа, установка и ремонт окон, остекление балконов, строительство зимних садов и др. услуги. Цены, онлайн-расчёт стоимости окон. Информация об акциях и спецпредложениях. Фотографии объектов.", False, False),
    (31, "http://www.OknaSite.ru/", u"\"Ваши теплые окна\" - производство деревянных окон", u"Производство, продажа и монтаж деревянных, дерево-алюминиевых окон со стеклопакетами, евроокон, арочных окон из древесины дуба и др. Стоимость. Фотогалерея готовых работ.", False, False),
    (32, "http://okna-virtual.ru/", u"Заказать пластиковые окна / Купить окна ПВХ в Москве...", u"Самые выгодные цены на пластиковые окна в Москве и области. Если Вы решили купить пластиковые окна ПВХ в Москве...", False, False),
    (33, "http://nww.ru/", u"Новые окна - производитель пластиковых окон.", u"Производство и продажа пластиковых окон из ПВХ и алюминия, кованых изделий; оборудования для производства окон и для деревообработки. Цены. Галерея работ. Онлайн-калькулятор.", False, False),
    (34, "http://www.oknamedia.ru/", u"\"Окна медиа\" - портал о пластиковых окнах", u"Каталог производителей окон, отзывы о компаниях-установщиках. Новости, обзоры и аналитика рынка. Динамика цен, оконный калькулятор. Форум, фото- и видеоматериалы.", False, False),
    (35, "http://www.formulaokna.ru/", u"\"Формула окна\" - пластиковые окна", u"Производство, монтаж и сервисное обслуживание пластиковых окон и дверей, стеклопакетов, витражей и др. Цены, калькулятор стоимости. Фотогалерея готовых работ. Отзывы клиентов. Адреса мест продаж.", False, False),
    (36, "http://www.okna-best.ru/", u"ООО Компания ОКНА", u"АКЦИЯ!!!Купив окна в нашей компании Вы можете стать обладателем автомобиля VOLGSWAGEN JETTA или стеклочистителя KARHER.", False, False),
    (37, "http://www.oknamir.ru/", u"Главная страница - Окна Мир", u"Изготовление, доставка и установка различных видов пластиковых окон, витражей, вентилируемых фасадов, зимних садов, дверей и др. Статьи. Контакты.", False, False),
    (38, "http://www.premium-okna.ru/pvc.html", u"Пластиковые окна ПВХ используемые в Москве...", u"Пластиковые окна идеально гармонируют с любым архитектурным стилем зданий: от нестареющей классики до авангардных дизайнерских проектов.", False, False),
    (39, "http://www.oknalina.ru/", u"Окна Лина: Пластиковые окна в Москве и Московской...", u"Компания «Окна Лина» - тепло и уют вашего дома! 10 лет вместе в Вами! Качественные оконные и дверные конструкции, офисные перегородки, жалюзи.", False, False),
    (40, "http://oknalegion.ru/", u"Пластиковые окна ПВХ в Москве", u"Установка пластиковых, деревянных и алюминиевых окон, отделка балконов. Онлайн-расчёт стоимости окна. Онлайн-заявка на вызов замерщика. Галерея работ.", False, False),
    (41, "http://www.glavokna.ru/", u"\"Главокна\" - пластиковые окна", u"Изготовление и установка окон, остекление балконов и лоджий. Цены на продукцию. Информация о скидках. Технические описания профилей. Советы по эксплуатации. Контакты.", False, False),
    (42, "http://www.okna-yes.ru/", u"\"Okna-yes\" - монтаж окон и остекление балконов", u"Изготовление и монтаж пластиковых окон и алюминиевых конструкций, остекление, утепление и отделка балконов. Описание продукции. Цены. Фотогалерея.", False, False),
    (43, "http://msk.localmart.ru/okna/", u"Окна б/у Московская область : продать, купить окно...", u"Продам окна ПВХ. Новые, готовые, в наличии. Двухкамерный стеклопакет, поворотно-откидная створка: (В)100*(Ш)100-стоим... избранное Москва.", False, False),
    (44, "http://www.format-okna.ru/", u"Пластиковые окна и двери - \"Формат-Окна\", отзывы", u"Качественные пластиковые окна от компании «Формат-Окна». Наша компания «Формат-Окна» работает с 1998 года и за это время зарекомендовала себя...", False, False),
    (45, "http://forum-okna.ru/", u"Оконный форум, форум-окна forum-okna.ru", u"Форум про окна, монтаж, ремонт, оконные конструкции, программное обеспечение.Свободное общение 2.0Форум, для любителей обсуждать отвлеченные темы, никак не связанные с оконной …Ремонт и техническое обслуживание окон — 18 мая 2015Все вопросы по этой узкой, но важной теме Всего 26 форумов ", False, False),
    (46, "http://www.oknadoz.ru/", u"Купить пластиковые окна: цены в Москве. Производство...", u"Пластиковые окна в Москве могут быть изготовлены не только белого цвета, но и любого другого подходящего для Ваших целей.", False, False),
    (47, "http://www.oknacm2.ru/", u"Пластиковые окна в Москве, производство, монтаж...", u"Изготовление и монтаж ПВХ-окон и дверей, офисных перегородок, систем остекление балконов, зимних садов и пр. Калькулятор расчета стоимости заказа. Онлайн-вызов замерщика. Адреса мест продаж.", False, False),
    (48, "http://www.okna-super.ru/calculator/", u"...окна калькулятор. Стоимость пластиковых окон в Москве", u"«Делали ремонт и решили обновить окна. Обратились в «Окна Супер» и попросили сделать двустороннюю ламинацию окон.", False, False),
    (49, "http://market.yandex.ru/catalog/91726/list?page=3&clid=703", u"Окна — Результаты поиска — Яндекс.Маркет", u"Мансардные окна Velux обеспечивает на 30-40% больше света, чем слуховое окно с такой же площадью остекления.", False, False),
    (50, "http://www.oknamoskvy.ru/", u"Пластиковые окна (окна ПВХ) в Москве: установка...", u"Пластиковые окна от фирмы «Окна Москвы». Компания «Окна Москвы» высоко зарекомендовала себя в области производства и установки пластиковых окон и ПВХ...", False, False),
    (51, "http://www.FabOkon.ru/", u"\"Фабокон\" - пластиковые окна и двери", u"Производство, продажа и установка пластиковых окон и дверей, остекление балконов и лоджий, отделка откосов и др. Калькулятор стоимости окон. Акции, программы скидок. Фотогалерея. Контакты.", False, False),
    (52, "http://veramo.ru/", u"\"Верамо\" - пластиковые окна Veka и Rehau", u"Замер, изготовление и монтаж окон. Описание профильных систем, цветовая гамма, цены. Контакты.", False, False),
]

serp_2_snippets = [
    (1, "http://MosMobi.ru/hummer-h5", u"Hummer H5 Ударопрочный и стильный смартфон... - Москва", u"9 000 руб.MosMobi.ru›Hummer H5Сохранённая копияПоказать ещё с сайтаПожаловатьсяHummer H5 как раз из такой серии. Это новый смартфон, который отлично защищен от повреждений, различных воздействий и излишней влаги.Доставка: Москва от 300 руб.", False, False),
    (2, "http://mtk-telefon.ru/kommunikatory-i-smartfony/zashchishchennye-smartfony/hummer-h5-ip67.html", u"Hummer H5 mtk 6572 - Москва", u"7425 руб. Представляем Вам новинку - защищенный смартфон Hummer H5 со степенью защиты IP68. Кроме его наглядных качеств, телефон имеет неплохую начинку: двух ядерный процессор, хороший экран с размером 4 дюйма...", False, False),
    (3, "http://chinese-cafe.ru/shop/509/desc/hummer-h5", u"Купить Hummer H5, Hummer H5 отзывы, обзор Hummer...", u"Технические характеристики Hummer H5: Новый функциональный пыле-влага-защищённый Android смартфон Hummer H5.", False, False),
    (4, "http://defmob.com/katalog/phones/hummer-h5.html", u"Защищенный водонепроницаемый телефон Hummer...", u"Cмартфон Hummer H5 - это полноценно защищённый телефон, построенный на двухъядерной базе с достаточным объёмом оперативной памяти.", False, False),
    (5, "http://www.gps-mio.ru/catalog/t3971.html", u"Телефоны Hummer Защищенный смартфон HUMMER H5", u"Защищенный смартфон HUMMER H5. Главная Телефоны Hummer. 9500 руб. шт.", False, False),
    (7, "http://magazilla.ru/desc/hummer-h5/", u"Мобильный телефон Hummer H5. Описание... - Москва", u"Характеристики и описание Hummer H5. ... Мобильный телефон Защищенный телефон Hummer H5+ black-green Video-shoper.ru (Москва).", False, False),
    (9, "http://rezervacija.com.ua/products/hummer-h5", u"Защищенные телефоны Hummer H5 купить со скидкой...", u"Hummer H5 - защищенный, противоударный, водонепроницаемый смартфон.", False, False),
    (10, "http://www.e-katalog.ru/HUMMER-H5.htm", u"Hummer H5 – купить мобильный телефон, сравнение цен...", u"Мобильный телефон Защищенный телефон Hummer H5+ black-green. Защищенный смартфон Hummer H5 со степенью защиты IP68.", False, False),
    (11, "http://runbo-extreme.ru/product/hummer-h5", u"Купить Hummer H5, продажа защищенного смартфона...", u"Благодаря низкой цене защищённого смартфона Hummer H5, его обладателем может стать любой желающий.", False, False),
    (12, "http://china-techcom.com/hummer-h5-mt6572.html", u"Hummer H5 противоударный водонепроницаемый купить...", u"7400 руб. Китайские защитные смартфоны вроде Hummer H5 ориентированы на людей, которые привыкли веcти очень активный образ жизни. Данная модель прекрасно подходит спортсменам, путешественникам, туристам.", False, False),
    (13, "http://hummer-h5.ru/", u"Купить Hummer H5", u"Защищенный смартфон HUMMER H5. Защищен по стандарту IP68. Имеет влагостойкий корпус и способен работать под водой до двух метров.", False, False),
    (14, "http://sotavsem.ru/protectedsmartphone/hummer/hummer-h5.eur.black", u"Защищенный смартфон Hummer H5 купить по цене 6900 руб", u"Купить защищенный телефон Hummer H5 с доставкой по Москве и все России. Закажите смартфон Hummer H5 не боящийся пыли и влаги в интернет магазине...", False, False),
    (15, "http://forum.china-iphone.ru/hummer-h5-4g-512-480-800-t33656.html", u"HUMMER H5 4G/512 480*800 • 1 • Forum.China-iPhone.Ru", u"15 апреля 2014 в порядке, я имел полное восстановление HUMMER H5, спасибо специалистов. Posted after 26 minutes 28 seconds: Пожалуйста, поддержите CWM HUMMER H5, СПАСИБО эксперты.Всего 548 сообщений ", False, False),
    (16, "http://www.kit-iphone.ru/shop/shop.product_details/19/flypage.tpl/317.html", u"Hummer H5", u"Hummer H5 – старший брат популярного «неубиваемого» Hummer H11+. ... Сейчас – лучше бы купил два Хаммера, чем Хаммер и ЛендРовер.", False, False),
    (17, "http://kpkmag.ru/goods/Hummer-H5-IP67-MTK6572-2", u"Купить смартфон Hummer H5 IP67 MTK6572 /Цена. Отзывы....", u"Описание Hummer H5 IP67 MTK6572: Hummer H5 - продолжение известной линии пыле-влага-защитных бюджетных смартфонов от Hummer.", False, False),
    (18, "http://catphone.ru/products/11144635", u"Защищенный смартфон Hummer H5", u"8 999 руб.catphone.ru›Защищенные телефоны›Hummer H5Сохранённая копияПоказать ещё с сайтаПожаловатьсяЗащищенный смартфон Hummer H5. ... Подскажите пожалуйста: Хаммер Н5, и Хаммер Н55 - это разные аппараты, или, всё же это один и тот же??Доставка: Москва от 200 руб.", False, False),
    (19, "http://rugged.com.ua/review/hummer-h5", u"Обзор защищенного смартфона Hummer H5 – RUGGED.", u"Обзор защищенного смартфона Hummer H5. Информация от компании RUGGED. Цены, описание, характеристики, тесты товаров.", False, False),
    (20, "http://moskva.aport.ru/hummer_h5/mod752869", u"Hummer H5: цены в Москве. Купить Хаммер H5 в Москве", u"Hummer H5: цены от 9 390руб. до 9 390руб. В наличии у 1 магазина. Купить Хаммер H5 в Москве. Характеристики, описание, фото.", False, False),
    (21, "http://ru.aliexpress.com/popular/phones-hummer.html", u"телефоны hummer – Купить телефоны hummer недорого...", u"Оригинал Hummer H5 водонепроницаемый телефон смартфон андроид 4.4 IP68 телефон 3 г GPS емкостный экран WCDMA водонепроницаемый а...", False, False),
    (22, "http://tankofon.ru/index.php?route=product/product&product_id=74", u"купить Hummer H5 | Танкофон", u"Производитель: Hummer Модель: Hummer H5 Наличие: Есть в наличии Отзывов написано: 3 Написать.", False, False),
    (23, "http://sonim-tech.ru/goods.php?id=342", u"Защищенный телефон Защищенный телефон Hummer H5", u"9 900 руб.sonim-tech.ru›goods.php?id=342Сохранённая копияПоказать ещё с сайтаПожаловатьсяПри том, что стоимость нового Hummer H5 осталась практически на уровне предыдущих моделей, разработчики усилили параметры защищенности нового смартфона.Доставка: Москва от 380 руб.", False, False),
    (24, "http://magmid.ru/tabletpc/waterproof-dustproof-antishock/Uphone-s930.html", u"Противоударный телефон Hummer H5 на Android; купить...", u"Защищенный противударный, пыленепроницаемый, водонепроницаемый смартфон-телефон Hummer H5 цена на неубиваемый телефон купить в интернет магазине в...", False, False),
    (25, "http://dostavkada.ru/product_10906.html", u"...Hummer h5 (Хамер H5, H55) с доставкой по москве.", u"Hummer H55 (H5) - телефон, который зарекомендовал себя с лучшей стороны. ... Многие родители, купив телефон Хаммер H55 (H5), для своего ребенка, через...", False, False),
    (26, "http://phonempire.ru/goods/%D0%9C%D0%BE%D0%B1%D0%B8%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D1%82%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD-Hummer-H5", u"Мобильный телефон Hummer H5, купить Мобильный...", u"Hummer H5 как раз из такой серии. Это новый смартфон, который отлично защищен от повреждений, различных воздействий и излишней влаги.", False, False),
    (27, "http://otzovik.com/reviews/smartphone_hummer_h5/", u"Отзывы о Смартфон Hummer H5", u"Смартфон Hummer H5 - отзывы. ... прикупил себе Hummer H5 до этого были (Discovery V5 пустая трата денег НЕ вздумайте покупать) остался очень доволен все...", False, False),
    (28, "http://www.cars.ru/catalog/Hummer/", u"Новый Hummer 2015 - Автомобили марки Hummer: цены...", u"Автомобили Hummer, снятые с производства и не продающиеся официально в России. Hummer H3.", False, False),
    (29, "http://4pda.ru/forum/index.php?showtopic=564309", u"Hummer H5 - Обсуждение, Смартфон 4\" | Форум", u"15 апреля 2014 Обсуждение Hummer H5 Hummer H5 Обсуждение ». Перед тем как задать вопрос, посмотрите FAQ по Android OS и Глоссарий.Всего более 11 сообщений ", False, False),
    (30, "http://ekonomimdengi.ru/", u"Телефон хаммер H5 (H55) купить - Доставка телефонов...", u"оставка телефонов хаммер H5 (H55) по Москве. ... Купить Hummer H5 с доставкой по Москве. Есть в наличии Hummer H5 черного цвета.", False, False),
    (31, "http://www.mobipukka.ru/2014/03/20/zashhishhennyj-gps-smartfon-ip68-hummer-h5/", u"Защищенный GPS-смартфон IP68 Hummer H5", u"Защищенный смартфон Hummer H5 является усовершенствованным вариантом Hummer H1.20 марта 2014", False, False),
    (32, "http://Nado-Telefon.ru/zashchishchennye-telefony/hummer-h5-ip67.html", u"Hummer H5", u"Защищенный смартфон Hummer H5 MTK6572 оснащен двухъядерным процессором MTK6572, Dual Core, с тактовой частотой 1,3 ГГц каждого ядра...", False, False),
    (33, "http://tiu.ru/Hummer-h5-1.html", u"HUMMER H5 в России. Сравнить цены, купить... - Москва", u"Широкий выбор поставщиков, у которых можно купить HUMMER H5 в России по лучшей цене. Заказать HUMMER H5 на Tiu.ru.", False, False),
    (34, "http://RusHummer.ru/forum/viewtopic.php?p=312847", u"Очень интересный концепт HUMMER H5 • HUMMER & AUTO...", u"Новости о Хаммер и других авто. ... Re: Очень интересный концепт HUMMER H5. А почему Н 5, разве Н 4 уже есть..", False, False),
    (35, "http://kitaiskii-planshet.ru/hummer-h5-mt6572.html", u"Hummer H5 противоударный водонепроницаемый Интернет...", u"7400 руб. В модели Hummer H5 подобного недостатка не имеется. Поддерживается стандарт защиты IP68, пагубные воздействия со стороны окружающей среды больше не страшны.", False, False),
    (36, "http://ShopoTam.ru/brand/hummer-h5/", u"Бренд HUMMER H5 — купить с доставкой в Москву...", u"Доставка качественных товаров известного бренда HUMMER H5 в Москву и регионы России от 6-и дней.", False, False),
    (37, "http://ChiMarket.ru/shop/show-product/452/13/hummer-h5-mtk6572-ip-67/", u"Купить китайский защищенный телефон Hummer H5 IP-67...", u"Hummer H5 - новый защищенный китайский телефон в пыле-влаго-защищённом корпусе под управлением операционной системы Android.", False, False),
    (38, "http://kitomart.ru/shop/320/desc/hummer-h5-ip67-mtk6572", u"Купить Hummer H5 IP67 MTK6572. Отзывы. Низкая цена", u"Имеет класс защиты стандарта IP67, Hummer H5 работает на базе процессора MTK6572 под управлением ОС Android 4.2.2.", False, False),
    (39, "http://www.needrom.com/download/hummer-h5/", u"Hummer H5", u"Rom for hummer h5 only MT6572 100% workLanguage: Multilanguage100% CZECHVersion for flash toolbuild.version=TLSJ_S930_HYS_A06_S152AWK_HUMMER_CN_GCS_2G_4P_W3G_2P...", False, False),
    (40, "http://activizm.ru/goods/539232/zascshiscshennyj_smartfon_hummer_h5/", u"Защищенный смартфон Hummer H5 - купить в Москве...", u"Ищете Защищенный смартфон Hummer H5? Проверенные интернет-магазины, конкурентные цены, доставка по Москве и РФ.", False, False),
    (41, "http://www.drive.ru/hummer", u"Hummer: цены, тест-драйвы, отзывы, форум, фото, видео", u"Кроме модели H4 Hummer может выпустить маленький внедорожник H5. ... Число звёзд над головой Хаммера уменьшилось в десять раз.", False, False),
    (42, "http://www.minmin.ru/index/good/1473", u"Hummer H5 - Защищённый смартфон", u"Hummer H5– старший брат популярного «неубиваемого» Hummer H11+. Тот же ударопрочный, водонепроницаемый корпус, та же мощная батарея…", False, False),
    (43, "http://www.pleer.ru/_180022_hummer_h5.html", u"Hummer H5 - купить сотовый телефон Хаммер по лучшей...", u"Hummer H5 - это уникальный по общим составляющим смартфон. С одной стороны - это классический бюджетный смартфон на операционной системе Android, однако, снабженный очень неплохими для своей цены характеристиками и, к тому же...", False, False),
    (44, "http://russian.alibaba.com/goods/hummer-h5-phone.html", u"Hummer H5 Телефон, Поиск лучших товаров Hummer...", u"Посик Высшего качества Hummer H5 Телефон, Hummer H5 Телефон Компаний, Hummer H5 Телефон Производителей на Alibaba.com.", False, False),
    (45, "http://mobilhits.ru/products/hummer-h5-", u"Hummer H5", u"9 500 руб.mobilhits.ru›products/hummer-h5-Сохранённая копияПоказать ещё с сайтаПожаловатьсяЗащищенный телефон Hummer H5 - устройство из будущего. ... Он очень похож на своего теску - внедорожник Хаммер, поэтому имеет фото авто на задней...Доставка: Москва, бесплатно", False, False),
    (46, "http://irecommend.ru/content/smartfon-bronenosets", u"Мобильный телефон Hummer H5 - «Смартфон броненосец»...", u"Сегодня делюсь с вами своим новым приобретением - смартфоном Хаммер Н5. ... написать модератору. CrockXP рекомендует Мобильный телефон Hummer H5.", False, False),
    (47, "http://hummerclubrus.ru/forums/showthread.php?p=916109", u"Hummer H5 тестил кто? | Форум", u"23 декабря 2014 xenon4ek надеюсь выдержит, хотя у меня ни квадрика, ни снегохода нет, покупал Н5 для Хомяка)))Всего более 50 сообщений ", False, False),
    (48, "http://electronics.wikimart.ru/communication/cell/model/64702598/mobilnyjj_telefon_hummer_h5_plus/", u"Мобильный телефон Hummer Hummer H5 Plus | Викимарт", u"Мобильный телефон Hummer Hummer H5 Plus. Характеристики Описание. 9489 Р. ... Описание. Защищенный смартфон Hummer H5 со степенью защиты IP68.", False, False),
    (49, "http://www.hummer-h5.de/", u"hummer-h5.de", u"Ссылки на страницу содержат: Hummer H5....", False, False),
    (50, "http://dialogdv.ru/product/hummer-h55/", u"Hummer H55 - купить неубиваемый Android-смартфон...", u"Поэтому выгоднее прямо сейчас купить телефон хаммер на нашем сайте dialogdv.ru. ... Hummer H55 отзывы. отзыв о телефоне Хаммере.", False, False),
    (51, "http://my.mail.ru/mail/hummer_h5/", u"Николай Елагин - на Мой Мир@Mail.ru", u"Николай Елагин - . Страница пользователя hummer_h5@mail.ru социальной сети Мой Мир.", False, False),
    (52, "http://luxury-info.ru/catalog/auto/Hummer/Hummer-H5.html", u"Hummer H5 - Автомобили - Luxury-info.ru Портал о мире...", u"Hummer » H5. Модельный ряд. ... Может и дорог-то не останется для настоящего «Хаммера». Вернее их отсутствия.", False, False),
]

serp_3_snippets = [
    (1, "http://www.dvor.chita.ru/files/prays_pechatniy_dvor_na_6.02.2015.xls", u"dvor.chita.ru/files/prays_pechatniy_dvor_na_6.02.2015.xls", u"Посмотреть", False, False),
    (2, "http://www.misuraemme.it/upload/files/001/scheda_tecnica/en_sistemacrossing.pdf", u"CROSSING", u"Посмотреть", False, False),
    (3, "http://www.cs.rochester.edu/u/myros/classes/cs247/class-project/6318-most-frequent-lexemes.lisp", u"cs.rochester.edu/u/myros/classes/cs247/class-project/6318...", u"...Adv) (4839 1245 brigade n) (1552 6190 bright a) (2432 3498 brilliant a) ... Pron) (4382 1450 thereafter adv) (2917 2660 thereby adv) (435 23218 therefore adv)...", False, False),
    (4, "http://www.bidsync.com/DPXViewer/Contract_Letter.Attach_Catalog_rev_2009-0407.pdf?ac=view&contid=3708&docid=1028421", u"California Office Supplies Catalog, dated 04/07/2009", u"Посмотреть", False, False),
    (5, "http://greaterworcestermagazine.com/?page_id=383", u"F Yellow Pages » Worcester County Massachusetts - Greater...", u"Financial Planning Consultants American Express Financial Adv 42 Brook St Whitinsville ... Funeral Directors Tancrell-Jackman Funeral Home 35 Snowling Rd Uxbridge 01569-2432...", False, False),
    (6, "http://www.trpdd.com/countyspending/pontotoc/2012ledger.pdf", u"CPONTOTOC - ID: 000022 - Form: GREENBAR", u"Посмотреть", False, False),
    (7, "http://cve.mitre.org/data/refs/refmap/source-BUGTRAQ.html", u"CVE - CVE Reference Map for Source BUGTRAQ", u"Common Vulnerabilities and Exposures (CVE®) is a dictionary of common names (i.e., CVE Identifiers) for publicly known information security vulnerabilities. CVE's common identifiers...", False, False),
    (8, "http://www.autismnet.ru/puremedix.com/pricelist/", u"Price list ― PUREMEDIX | US $42,25", u"Metagenics, ADVACLEAR® 126 CAPS. US $80,75. ADV42. Metagenics, ADVACLEAR® 42 VCAPS.", False, False),
    (9, "http://www.ecr.indianrailways.gov.in/ecr/billstatus/1415014605359_getjobid24.pdf", u"Installation for : hjp/dnr/see/spj section : 160...", u"Посмотреть", False, False),
    (10, "http://www.docstoc.com/docs/120692255/gsl_senses_dickins", u"gsl_senses_dickins by fanzhongqing", u"...[X] decided adj 637 637 2% 12 2426 decide [X] decidedly adv 56 56 100% 56 2427 decide ... will/won't/would willingly adv 42e 42 100% 42 11653 [X]. will/won't/would unwilling adj 68e 68...", False, False),
    (11, "http://www.decoracabinets.com/cabinet-resources/~/media/Decora/Documents/Decora_Spec_March2013.ashx", u"What’s New", u"Посмотреть", False, False),
    (12, "http://str-sintez.ru/data/str-sintez/files/str-sintez.xls", u"str-sintez.ru/data/str-sintez/files/str-sintez.xls", u"Посмотреть", False, False),
    (13, "http://files.baumanec.net/botva/8%20semestr/Dinamika/2%20%E4%E7.xmcd", u"files.baumanec.net/botva/8 semestr/Dinamika/2 дз.xmcd", u"7788uKhtx9aDv42X3n38WK1WR4bePL97787o0ItyZTIIy8RAMF9MVl7WiWffgFH5UR0S6mwm...", False, False),
    (14, "http://www.downanddirtyobstaclerace.com/wp-content/uploads/MIA-5K_AgeGroup.pdf", u"Cobra Kai Cobra Kai", u"Посмотреть", False, False),
    (15, "http://www.attachmentnewengland.com/FamilyAdventureCamp.mht", u"attachmentnewengland.com/FamilyAdventureCamp.mht", u"...KG0AdV42j+etWEGw3WZPugOt0FuFCpE6RCSqovLVIlstpz8KOYEqA9k9BpuOTJS5aUu3bfqNSm8h.", False, False),
]

if __name__ == '__main__':
    unittest.main()
