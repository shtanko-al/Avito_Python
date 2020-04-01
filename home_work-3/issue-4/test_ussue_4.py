import pytest
from one_hot_encoder import fit_transform


def test_fit_transform_empty():
    with pytest.raises(TypeError):
        fit_transform()
    with pytest.raises(TypeError):
        fit_transform(1)


def test_fit_transform_str():
    expect = [('pies', [0, 0, 1]), ('work', [0, 1, 0]), ('may', [1, 0, 0])]
    assert fit_transform('pies', 'work', 'may') == expect


def test_fit_transform_list():
    my_in = [1, '2', 3]
    expect = [(1, [0, 0, 1]), ('2', [0, 1, 0]), (3, [1, 0, 0])]
    assert fit_transform(my_in) == expect


def test_str_with_double():
    my_in = fit_transform('Paris', 'Ney-York', 'Paris')
    assert my_in == [('Paris', [0, 1]), ('Ney-York', [1, 0]), ('Paris', [0, 1])]


def test_str_only_double():
    my_in = fit_transform('apple', 'apple', 'apple', 'apple')
    assert my_in == [('apple', [1]), ('apple', [1]), ('apple', [1]), ('apple', [1])]


if __name__ == '__main__':
    pytest.main()
