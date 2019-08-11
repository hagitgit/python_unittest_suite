# run all tests in module:
# my_projects/sample_unittest » python -m unittest test.test_the_guide -v
# run all tests in class:
# my_projects/sample_unittest » python -m unittest test.test_the_guide.TestTheGuide -v
# run a specific test:
# my_projects/sample_unittest » python -m unittest test.test_the_guide.TestTheGuide.test_test -v
# run all tests under test folder:
# my_projects/sample_unittest » python -m unittest discover -v

import unittest

from sample_unittest.the_guide import TheGuide
 
class TestTheGuide(unittest.TestCase):
	
	def test_test(self):
		self.assertTrue(True)

	def test_the_guide(self):
		answer = TheGuide().the_most_important_item()
		self.assertEqual(answer,'towel',"Don't Panic!")

if __name__ == '__main__':
	unittest.main()
