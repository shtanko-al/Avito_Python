import json


class AdvertRecurs:
    """
    Класс принимает json или словарь и генерирует объекты класса
    с атрибутами взятыми из json'на или словаря
    глубина вложенности бесконечная, вложенные типы - объекты класса AdvertRec
    (нет проверок, но интересно получилось)
    """

    def __init__(self, data_adv: str or dict):
        if type(data_adv) == str:
            atr_data = json.loads(data_adv)
        else:
            atr_data = data_adv

        for key, value in atr_data.items():
            if type(value) == dict:
                self.__dict__[key] = AdvertRecurs(value)
            else:
                self.__dict__[key] = value

    def __repr__(self):
        return " | ".join(self.__dict__)


class Advert:
    """
    Класс принимает json-строку или словарь и генерирует объекты класса
    с необходимыми атрибутами (атрибуты 'title' и 'price' есть есть всегда)
    бесконечная глубина вложенности
    """

    def __init__(self, json_str: json or str):
        self.title = None
        self.price = 0

        if type(json_str) == str:
            atr_data = json.loads(json_str)
        else:
            atr_data = json_str

        for key, value in atr_data.items():
            if type(value) == dict:
                self.__dict__[key] = Pole(value)
            else:
                self.__dict__[key] = value

        if self.title is None:
            raise ValueError("Ошибка: нет поля 'title'")
        if self.__dict__.setdefault('price', 0) < 0:
            raise ValueError('Ошибка: цена меньше 0')

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


class Pole:
    """Вспомогательный класс для класса Advert"""

    def __init__(self, d: dict):
        for key, value in d.items():
            if type(value) == dict:
                self.__dict__[key] = Pole(value)
            else:
                self.__dict__[key] = value

    def __repr__(self):
        return " | ".join(self.__dict__)


class ColorizeMixin(Advert):
    # color_code = {
    #     'red': 31,
    #     'green': 32,
    #     'yellow': 33,
    # }

    # def __init__(self, color: str):
    #     self.repr_color_code = self.color_code[color]

    def __repr__(self):
        super(Advert, self).__repr__()
        return f'\033[1;33;40m{self.title} | {self.price} ₽\033[1;00;00m'


class ColorAdvert(ColorizeMixin, Advert):
    pass


if __name__ == '__main__':
    adv_dict_1 = {
        "title": "iPhone X",
        "price": 100,
        "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"]
        }
    }
    adv_dict_2 = {
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }
    }
    adv_str_1 = """{
        "title": "course python",
        "price": 50,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская",
            "Пушкинская"]
            }
        }"""
    adv_str_2 = """{
        "title": "car",
        "price": 100500,
        "text": "едет с трудом",
        "location": {
            "address": "город Cходня, Лесная, 7",
            "metro_stations": ["Речной Вокзал"]
            }
        }"""
    adv_str_3 = """{
        "title": "Very interesting thing",
        "price": 999999,
        "specification": {
            "type": {
                "a1": "11",
                "a2": "22"
            },
            "weight": {
                "b1": "33",
                "b2": "44"
            },
            "power": {
                "b3": {"qe": "55", "qqw": 23},
                "b4": {"as": "66", "erth": "sdf"}
            }
        },
        "location": {
            "address": "город Cходня, Лесная, 7",
            "metro_stations": ["Речной Вокзал"]
            }
        }"""

    my_advert_1 = ColorAdvert(adv_dict_1)
    print(my_advert_1)

    # my_advert_2 = AdvertRec(adv_str_1)
    # print(my_advert_2.location)

    my_advert_3 = AdvertRecurs(adv_str_3)
    print(my_advert_3)
    print(my_advert_3.__dict__)
    print(f'обращение к полю b3: {my_advert_3.specification.power.b3}')
    print(my_advert_3.specification)

    # print(my_advert_1.title)
    # print(f'цена: {my_advert_1.price}')
    # print(my_advert_1)

    # print('\nатрибуты:')
    # for a in my_advert_1.get_atr():
    #     print('\t', a)
