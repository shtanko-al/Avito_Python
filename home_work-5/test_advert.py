import unittest
from issue_01 import Advert, ColorAdvert

j1 = {
    "title": "iPhone X",
    "price": 100,
    "location": {
        "address": "город Самара, улица Мориса Тореза, 50",
        "metro_stations": ["Спортивная", "Гагаринская"]
    }
}
j2 = {
    "title": "Вельш-корги",
    "price": 1000,
    "class": "dogs",
    "location": {
        "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
    }
}
lesson_str = """{
    "title": "course python",
    "price": 50,
    "location": {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская",
        "Пушкинская"]
        }
    }"""
adv_1 = """{
    "title": "car",
    "price": 100500,
    "text": "едет с трудом",
    "location": {
        "address": "город Cходня, Лесная, 7",
        "metro_stations": ["Речной Вокзал"]
        }
    }"""


class TestAdvert(unittest.TestCase):
    def setUp(self) -> None:
        self.adv_1 = Advert(j1)
        self.adv_2 = Advert(lesson_str)
        # self.adv_3 = Advert(j3)
        # self.adv_4 = Advert(j4)
        # self.adv_5 = Advert(j5)
        # self.adv_6 = Advert(j6)

    def test_repr_1(self):
        self.assertEqual(self.adv_1, 'iPhone X | 100 ₽')

    def test_repr_2(self):
        self.assertEqual(self.adv_2, 'course python | 50 ₽')


if __name__ == '__main__':
    unittest.main()
