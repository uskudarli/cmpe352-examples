import unittest
import os
import HtmlTestRunner  # Import the HTMLTestRunner Module
import test_hello_world
import test_strings

# Get the Present Working Directory to store the report

current_directory = os.getcwd()

# Create a class to test the runner to produce nice HTML reports

class HTML_TestRunner_TestSuite(unittest.TestCase):
    def test_demo_suite(self):
        # create a test suite
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        # add two tests to the suite -- in principle they should be related, here they are demo
        suite.addTest(loader.loadTestsFromModule(test_hello_world))
        suite.addTest(loader.loadTestsFromModule(test_strings))

        # create output for running suite result

        output_file = open(current_directory + "/automated_unit_tests/reports/HTML_Test_Runner_ReportTest.html", "w")

        html_runner = HtmlTestRunner.HTMLTestRunner(
            stream=output_file,
            report_title='HTML Report for Unit Tests',
            descriptions='HTML Reporting using HTMLTestRunner')

        html_runner.run(suite)


# main function to call unittests

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports/html/'))

