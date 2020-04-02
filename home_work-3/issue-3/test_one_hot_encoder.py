import unittest
from one_hot_encoder import fit_transform


class TestOneHotEncoder(unittest.TestCase):
    def test_many_str(self):
        result = fit_transform('pies', 'work', 'may')
        self.assertEqual(result, [('pies', [0, 0, 1]), ('work', [0, 1, 0]), ('may', [1, 0, 0])])

    def test_list(self):
        result = fit_transform([1, '2', 3])
        self.assertEqual(result, [(1, [0, 0, 1]), ('2', [0, 1, 0]), (3, [1, 0, 0])])

    def test_str_with_double(self):
        result = fit_transform('Paris', 'Ney-York', 'Paris')
        self.assertNotEqual(result, [('Paris', [0, 0, 1]), ('Ney-York', [0, 1, 0]), ('Paris', [1, 0, 0])])

    def test_4(self):
        result = fit_transform('1', 'stone', '2', '1', 'stone')
        expect = [('1', [0, 0, 1]), ('stone', [0, 1, 0]), ('2', [1, 0, 0]), ('1', [0, 0, 1]), ('stone', [0, 1, 0])]
        self.assertIn(result[0], expect)

    def test_5(self):
        with self.assertRaises(TypeError):
            fit_transform()


if __name__ == '__main__':
    unittest.main()
