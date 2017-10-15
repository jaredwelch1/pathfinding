import sys
import unittest

sys.path.insert(0, '../classes')
from graph import graph



class graphTests(unittest.TestCase):

	def test_length(self):
		self.assertEqual(5, len(graph([1,2,3,4,5])))

if __name__ == '__main__':
	unittest.main()
