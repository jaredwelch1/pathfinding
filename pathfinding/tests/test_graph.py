import sys
import unittest
from pathfinding import Graph


class GraphTests(unittest.TestCase):

	def test_length(self):
		self.assertEqual(5, len(Graph([1,2,3,4,5])))

if __name__ == '__main__':
	unittest.main()
