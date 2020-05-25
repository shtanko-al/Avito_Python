from typing import Iterable
from copy import deepcopy


def ilen(iterable: Iterable):
    """1) функция возвращает размер итерируемого объекта
    или генератора, если объект пустой, то None
    не понятно как обработать строку, вернуть ошибку или длину строки?

    """
    n = 0
    for _ in iterable:
        n += 1
    return n


def flatten(iterable: list or tuple):
    """
    2) функция flatten, которая из многоуровневого массива сделает одноуровневый
    не понятно как обработать строку, вернуть ошибку или строку обратно?
    """
    if not isinstance(iterable, str):
        new_list = list()
        for i in iterable:
            if (not isinstance(i, Iterable)) or isinstance(i, str):
                new_list.append(i)
            else:
                tem_list = flatten(i)
                new_list += tem_list
        return new_list
    else:
        raise TypeError('функция не принимает строку')


def distinct_2(iterable: Iterable):
    """
    3) функция, которая удалит дубликаты, сохранив порядок
    """
    temp_list = list()
    for i in iterable:
        if i not in temp_list:
            temp_list.append(i)
    return temp_list


def distinct(iterable: Iterable):
    """
    3) функция, которая удалит дубликаты, сохранив порядок
    работатет со соловорями и множествами
    """
    temp_list = list()
    temp_set = set()
    temp_list_for_not_iter = list()
    for i in iterable:
        if not (isinstance(i, dict) or isinstance(i, set)):
            if i not in temp_set:
                temp_list.append(i)
                temp_set.add(i)
        else:
            if i not in temp_list_for_not_iter:
                temp_list.append(i)
                temp_list_for_not_iter.append(i)
    return temp_list


def groupby(key, iterable: Iterable):
    """
    4) функция делает из неупорядоченной последовательностей словарей,
    словарь сгруппированный по ключу
    """
    result_dict = dict()
    for i in iterable:
        if isinstance(i, dict):
            key_value = i[key]
            if key_value not in result_dict:
                result_dict[key_value] = []
                result_dict[key_value].append(i)
            else:
                result_dict[key_value].append(i)
        else:
            raise TypeError
    return result_dict


def chunks(size: int, iterable: Iterable):
    """5) функция, которая разобьет последовательность на заданные куски"""
    temp_list = list()
    result_list = list()
    n = 0
    for i in iterable:
        temp_list.append(i)
        n += 1
        if n == size:
            temp_list_2 = deepcopy(temp_list)
            result_list.append(temp_list_2)
            temp_list.clear()
            n = 0
    if n != 0:
        result_list.append(temp_list)
    return result_list


def first(iterable: Iterable):
    """6) функция получения первого элемента или None"""
    if isinstance(iterable, set):
        raise TypeError('в множествах нет очередности')
    elif isinstance(iterable, dict):
        for i in iterable.items():
            return {i[0]: i[1]}
    else:
        for i in iterable:
            return i


def last(iterable: Iterable):
    """7) функция возвращает последний элемент
    из итерируемого объекта или генератора
    или None, если объект пустой"""
    if isinstance(iterable, set):
        raise TypeError('в множествах нет очередности')
    elif isinstance(iterable, dict):
        i = None
        for i in iterable.items():
            pass
        return {i[0]: i[1]}
    else:
        i = None
        for i in iterable:
            pass
        return i


if __name__ == '__main__':
    # проверки:
    test_list_1 = [-1, 0, 7, ['asdasd', 3, 'stgsth'], 8, [1, [2, 3]], 11, 12]
    test_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    test_list_3 = ['a1', 'bbb', 'casd', 'dasd', 'e', 'f', 12]
    test_list_4 = [1, 7, 1, 5, 5, 1, 9, 8, 9, 15, 11]
    test_list_5 = ['a', 'b', {1: 'a', 'abc': 1}, 'cde', 'd', {12, 'abra', 'asdf', 17}, 'e', 'f']
    test_list_6 = {'wer': 11, 'a': 234, 2: 123}
    test_list_7 = {5, 6, 'asd', 7, 9, 8, 5, 'adf'}
    foo = (x for x in range(10))
    print('проверка функции ilen: ', ilen(test_list_1))
    print('проверка функции ilen от строки: ', ilen('test_list_1'))
    print('проверка функции ilen от генератора: ', ilen((x for x in range(10))))
    print(flatten(test_list_1))
    print('проверка функции chunks: ', chunks(3, test_list_1))
    print('проверка функции chunks: ', chunks(3, test_list_2))
    print('проверка функции chunks: ', chunks(3, test_list_3))
    print('проверка функции chunks: ', chunks(3, test_list_4))
    print('проверка функции chunks: ', chunks(3, test_list_5))
    print('проверка функции chunks: ', chunks(3, test_list_6))
    print()
    print('проверка функции first: ', first((x for x in range(10))))
    print('проверка функции first: ', first(test_list_6))
    print('проверка функции first: ', first(range(0)))
    # print('проверка функции first: ', first(test_list_7))

    print()
    print('проверка функции last: ', last(test_list_1))
    print('проверка функции last: ', last((x for x in range(10))))
    print('проверка функции last: ', last(test_list_6))

    users = [
        {'gender': 'female', 'age': 33},
        {'gender': 'male', 'age': 20},
        {'gender': 'female', 'age': 21},
    ]
    print()
    print('функция groupby: ', groupby('gender', users))
    print('функция groupby: ', groupby('age', users))
    print('функция distinct: ', distinct(test_list_4))
    print('функция distinct_2: ', distinct((x for x in range(10))))
