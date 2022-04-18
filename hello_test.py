import unittest
import hello

'''
A simple class to test the Hello Class defined in hello.py
'''

class HelloTestCase(unittest.TestCase):
    def test_hello_world(self):
        app = hello.Hello()
        name = 'George'
        result, status = app.hello_world(name)
        expected_result = 'Hello ' + name + '!'
        self.assertEqual(result, expected_result)
        self.assertEqual(status, 200)


if __name__ == '__main__':
    unittest.main()
