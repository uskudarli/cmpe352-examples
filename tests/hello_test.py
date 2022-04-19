import unittest
import hello

'''
A simple test for hello.py
'''

def test_hello_world():
    name = 'George'
    result, status = hello.hello_world(name)
    expected_result = 'Hello ' + name + '!'
    assert result == expected_result
    assert status == 200


if __name__ == '__main__':
    unittest.main()
