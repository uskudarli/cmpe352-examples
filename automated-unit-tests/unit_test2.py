import unittest


class FooTest(unittest.TestCase):
    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        print
        "FooTest:setUp_:begin"
        ## do something...
        print
        "FooTest:setUp_:end"

    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        print
        "FooTest:tearDown_:begin"
        ## do something...
        print
        "FooTest:tearDown_:end"