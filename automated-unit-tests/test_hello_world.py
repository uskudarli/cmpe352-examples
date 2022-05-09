#!/usr/bin/env python
import os
import unittest
import xmlrunner
import hello_world


class TestHello(unittest.TestCase):

    def setUp(self):
        hello_world.app.testing = True
        self.app = hello_world.app.test_client()
        self.mock_data = ['alice', 'ümit', 'oğuz', 'steve', 'Bjørn']

    def test_hello(self):
        return_value = self.app.get('/')
        self.assertEqual(return_value.status, '200 OK')
        self.assertEqual(return_value.data, b'Hello World!\n')

    def test_hello_hello(self):
        return_value = self.app.get('/hello/')
        self.assertEqual(return_value.status, '200 OK')
        self.assertEqual(return_value.data, b'Hello World!\n')

    def test_hello_name(self):
        for name in self.mock_data:
            return_value = self.app.get(f'/hello/{name}')
            self.assertEqual(return_value.status, '200 OK')
            self.assertIn(bytearray(f"{name}", 'utf-8'), return_value.data)

    def tearDown(self):
        self.mock_data = []

if __name__ == '__main__':
    # create a runner to see the output test reports
    root_dir = os.path.dirname(__file__)
    test_loader = unittest.TestLoader()
    package_tests = test_loader.discover(start_dir=root_dir)

    runner = xmlrunner.XMLTestRunner(output='./reports/xml/')
    unittest.main(testRunner=runner)