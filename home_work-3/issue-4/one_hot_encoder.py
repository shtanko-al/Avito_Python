from typing import List, Tuple


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    # print(categories)
    uniq_categories = set(categories)
    # print(type(uniq_categories))
    bin_format = f'{{0:0{len(uniq_categories)}b}}'
    # print(bin_format)

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        # print(seen_categories)
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


if __name__ == '__main__':
    from pprint import pprint

    # cities = ['Moscow', 'New York', 'Moscow', 'London']
    # exp_transformed_cities = [
    #     ('Moscow', [0, 0, 1]),
    #     ('New York', [0, 1, 0]),
    #     ('Moscow', [0, 0, 1]),
    #     ('London', [1, 0, 0]),
    # ]
    # transformed_cities = fit_transform(cities)
    # pprint(transformed_cities)
    # print()
    # # assert transformed_cities == exp_transformed_cities
    #
    # pprint(fit_transform('Paris', 'Ney-York', 'Himki', 'Omsk', 'samara', 'saturn', 'origami', 'Paris'))
    # pprint(fit_transform([1, 2, 3]))
    # my_words = ['pies', 'work', 'may']
    # print(fit_transform(my_words))
    # print(fit_transform('Paris', 'Ney-York', 'Paris', 'Omsk', 'Ney-York', 'Himki'))
    # print(fit_transform([1, 2, 3, 4]))
    print(fit_transform('1', 'stone', '2', '1', 'stone'))
    print(fit_transform())
