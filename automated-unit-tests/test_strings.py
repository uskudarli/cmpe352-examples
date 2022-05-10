import unittest
import xmlrunner


class TestStringMethods(unittest.TestCase):
    '''
    Verify that isupper function works correctly
    '''

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    '''
    Verify that string split  function correctly splits tokens 
    and raises type error if not string
    '''

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split raised TypeError if argument is not string
        with self.assertRaises(TypeError):
            s.split(7129)


if __name__ == '__main__':
    runner = xmlrunner.XMLTestRunner(output='./automated-unit-tests/reports')
    unittest.main(testRunner=runner)
