import json


class AdvertRec:
    """
    Класс принимает json или словарь и генерирует объекты класса
    с атрибутами взятыми из json'на или словаря
    глубина вложенности бесконечная, вложенные типы класса AdvertRec
    """

    def __init__(self, json_str: json or str):
        # self.title = None
        # self.price = 0
        if type(json_str) == str:
            atr_data = json.loads(json_str)
        else:
            atr_data = json_str
        for key, value in atr_data.items():
            if type(value) == dict:
                self.__dict__[key] = Advert(value)
            else:
                self.__dict__[key] = value
        # p = self.__dict__.setdefault('price', 0)
        if self.__dict__.setdefault('price', 0) < 0:
            raise ValueError('Ошибка: цена меньше 0')

    # def __repr__(self):
    #     t = self.__dict__['title']
    #     p = self.__dict__['price']
    #     return f'{t} | {p} ₽'

    def get_atr(self, t=None):  # надо допилить
        if t is None:
            temp_dict = self.__dict__
        else:
            temp_dict = t
        for key, value in temp_dict.items():
            if type(value) == dict:
                self.get_atr(t=value)
            else:
                yield key
        # return self.__dict__.keys()

    # def zap_pole(self, key, value):
    #     if type(value) != dict:
    #         self.__dict__[key] = value
    #     else:
    #         if type(value) == dict:
    #             self.zap_pole(self, value.items())
    #         else:
    #             self.__dict__[key] = Pole(value)


class Advert:
    """
    Класс принимает json или словарь и генерирует объекты класса
    с атрибутами взятыми из json'на или словаря
    (атрибуты 'title' и 'price' есть есть всегда)
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
                self.__dict__[key] = self.Pole(value)
            else:
                self.__dict__[key] = value
        if self.title is None:
            raise ValueError("Ошибка: нет поля 'title'")
        if self.__dict__.setdefault('price', 0) < 0:
            raise ValueError('Ошибка: цена меньше 0')

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'

    def get_atr(self):  # надо допилить
        for key, value in self.__dict__.items():
            print(type(value))
            if isinstance(value, self.Pole):
                self.zap_pole(value)
            else:
                yield key

    def zap_pole(self, t_d):
        for key, value in t_d.__dict__.items():
            if isinstance(value, self.Pole):
                self.zap_pole(value)
            else:
                yield key

    class Pole:
        """
        Вспомогательный класс для класса Advert
        """
        def __init__(self, d: dict):
            for k, v in d.items():
                self.__dict__[k] = v


if __name__ == '__main__':
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

    # print(type(lesson_str))
    my_advert_1 = Advert(lesson_str)
    # print(type(my_advert_1))
    print(my_advert_1.__dict__)
    print(my_advert_1.location.metro_stations)
    # print(my_advert_1.title)
    # print(f'цена: {my_advert_1.price}')
    print(my_advert_1.__repr__())

    print('\nатрибуты:')
    for a in my_advert_1.get_atr():
        print('\t', a)
