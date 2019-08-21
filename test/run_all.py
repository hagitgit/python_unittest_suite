# run the suite:
# PY_VENV_unittest_suite/my_projects/python_unittest_suite » python -m unittest test.run_all -v
# run all tests under test folder including suite:
# PY_VENV_unittest_suite/my_projects/python_unittest_suite » python -m unittest discover -v


import unittest

from test.test_deep_thought import TestDeepThought
from test.test_the_guide import TestTheGuide

def simple_suite():
	suite = unittest.TestSuite()
	suite.addTest(TestDeepThought('test_test'))
	suite.addTest(TestDeepThought('test_deep_thought'))
	suite.addTest(TestTheGuide('test_test'))
	suite.addTest(TestTheGuide('test_the_guide'))
	return suite

def loader_suite(loader, tests, pattern):
	test_cases = (TestDeepThought, TestTheGuide)
	suite = TestSuite()
	for test_class in test_cases:
		tests = loader.loadTestsFromTestCase(test_class)
		suite.addTests(tests)
	return suite

if __name__ == '__main__':
	runner = unittest.TextTestRunner()
	# runner.run(simple_suite())
	runner.run(loader_suite())
