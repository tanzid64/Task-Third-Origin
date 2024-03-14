from dict2 import Dict2, DictError
import unittest

class TestDict2(unittest.TestCase):
    def test_set_get_item(self):
        myDict = Dict2()
        myDict['a'] = 1
        myDict['b'] = 2
        self.assertEqual(myDict['a'], 1)
        self.assertEqual(myDict['b'], 2)

    def test_missing_key(self):
        myDict = Dict2()
        with self.assertRaises(DictError) as context:
            myDict['c']
        self.assertEqual(str(context.exception), "Key c does not exist in dict2")

    def test_iteration(self):
        myDict = Dict2()
        myDict['a'] = 1
        myDict['b'] = 2
        keys = list(iter(myDict))
        self.assertCountEqual(keys, ['a', 'b'])

if __name__ == '__main__':
    unittest.main()
