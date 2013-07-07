import unittest
from sample import quicksort

class TestQuicksort(unittest.TestCase):
	def runBasicTest(self, input, expected):
		quicksort.sort(input)
		self.assertEquals(input, expected)

	def test_sortEmptyList(self):
		self.runBasicTest([], [])

	def test_sortListWithOneItem(self):
		self.runBasicTest([5], [5])

	def test_basicsort(self):
		self.runBasicTest([6,3,0,-5,60,4,3,1], [-5, 0, 1, 3, 3, 4, 6, 60])

	def test_sortMap(self):
		try:
			quicksort.sort({'apple': 1, 'orange': 2})
		except TypeError:
			pass
		except:
			self.fail("quicksort should throw an exception for non-list input")

if __name__ == '__main__':
	unittest.main()
