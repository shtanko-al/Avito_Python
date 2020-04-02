from typing import Iterable, Union, Optional, List, Tuple, Dict, Iterator
from copy import deepcopy


def ilen(iterable: Iterable):
    # 1) функция получения размера генератора
    n = 0
    for _ in iterable:
        n += 1
    return n


def flatten(iterable: Iterable):
    # 2) функцию flatten, которая из многоуровневого массива сделает одноуровневый
    new_list = list()
    for i in iterable:
        if not isinstance(i, Iterable):
            new_list.append(i)
        else:
            tem_list = flatten(i)
            new_list += tem_list
    return new_list


def distinct(iterable: Iterable):
    # 3) функция, которая удалит дубликаты, сохранив порядок
    temp_list = list()
    for i in iterable:
        if i not in temp_list:
            temp_list.append(i)
    return temp_list


def groupby(key, iterable: Iterable):
    # 4) функция делает из неупорядоченной последовательностей словарей,
    #    словарь сгруппированный по ключу
    result_dict = dict()
    for i in iterable:
        # print('value of i: ', i)
        key_value = i[key]
        # print('value of key: ', key_value)
        if key_value not in result_dict:
            result_dict[key_value] = []
            result_dict[key_value].append(i)
        else:
            result_dict[key_value].append(i)
    return result_dict


def chunks(size: int, iterable: Iterable):
    # 5) функция, которая разобьет последовательность на заданные куски
    temp_list = list()
    result_list = list()
    n = 0
    for i in iterable:
        temp_list.append(i)
        n += 1
        if n == size:
            temp_list_2 = deepcopy(temp_list)
            # возможно использование deepcopy это моветон
            # и надо более алгоритмически сделать
            result_list.append(temp_list_2)
            temp_list.clear()
            n = 0
    if n != 0:
        result_list.append(temp_list)
    return result_list


def first(iterable: Iterable):
    # 6) функция получения первого элемента или None
    try:
        return next(iter(iterable))
    except StopIteration:
        return None


def last(iterable: Iterable):
    #  7) функция получения последнего элемента или None
    #     не работает с генераторами
    if len(iterable) == 0:
        return None
    else:
        return iterable[len(iterable)-1]
    
def last_2(iterable: Iterable):
    #  7) функция получения последнего элемента или None
    # теперь работает с генераторами, но, наверно, можно лучше сделать
    my_iterator = iter(iterable)
    n = 0
    while True:
        try:
            temp = next(my_iterator)
            # print(temp)
            n += 1
        except StopIteration:
            if n == 0:
                return None
            else:
                return temp

def last_3(iterable: Iterable):
    #  7) функция получения последнего элемента или None
    i = None
    for i in iterable:
        pass
    return i


############################################################
# проверки:
test_list_1 = [-1, 0, 7, 8, [1, [2, 3]], 11, 12]
test_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
test_list_3 = ['a', 'b', 'c', 'd', 'e', 'f']
foo = (x for x in range(10))
print(ilen(test_list_1))
print(flatten(test_list_2))
foo = (x for x in range(10))
print('проверка функции chunks: ', chunks(3, test_list_1))
print('проверка функции chunks: ', chunks(3, test_list_3))
print()
print('проверка функции first: ', first(foo))
print('проверка функции first: ', first(test_list_3))
print('проверка функции first: ', first(range(0)))
print()
print('проверка функции last: ', last_3(range(0)))
print('проверка функции last: ', last_3(foo))
print('проверка функции last: ', last_3(test_list_3))

users = [
        {'gender': 'female', 'age': 33},
        {'gender': 'male', 'age': 20},
        {'gender': 'female', 'age': 21},
]
print()
print('функция groupby: ', groupby('gender', users))
print('функция groupby: ', groupby('age', users))
