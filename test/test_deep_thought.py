# run all tests in module:
# PY_VENV_unittest_suite/my_projects/python_unittest_suite » python -m unittest test.test_deep_thought -v
# run all tests in class:
# PY_VENV_unittest_suite/my_projects/python_unittest_suite » python -m unittest test.test_deep_thought.TestDeepThought -v
# run a specific test:
# PY_VENV_unittest_suite/my_projects/python_unittest_suite » python -m unittest test.test_deep_thought.TestDeepThought.test_test -v
# run all tests under test folder:
# PY_VENV_unittest_suite/my_projects/python_unittest_suite » python -m unittest discover -v

import unittest

from sample_unittest.deep_thought import DeepThought
 
class TestDeepThought(unittest.TestCase):
	
	def test_test(self):
		self.assertTrue(True)

	def test_deep_thought(self):
		answer = DeepThought().the_answer_to_life_universe_and_everything()
		self.assertEqual(answer,42,"Don't Panic!")

if __name__ == '__main__':
	unittest.main()
