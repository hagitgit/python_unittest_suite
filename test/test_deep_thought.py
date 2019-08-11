# run all tests in module:
# my_projects/sample_unittest » python -m unittest test.test_deep_thought -v
# run all tests in class:
# my_projects/sample_unittest » python -m unittest test.test_deep_thought.TestDeepThought -v
# run a specific test:
# my_projects/sample_unittest » python -m unittest test.test_deep_thought.TestDeepThought.test_test -v
# run all tests under test folder:
# my_projects/sample_unittest » python -m unittest discover -v

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
