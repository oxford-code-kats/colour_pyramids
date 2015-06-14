import unittest
from itertools import permutations

from pyramid import Colour, top_block, next_row, pyramid_peak

class PyramidTests(unittest.TestCase):

	def test_top_block_same_colour(self):
		for colour in Colour:
			blocks = [colour, colour]
			with self.subTest(colour=colour):
				self.assertEqual(top_block(blocks), colour)

	def test_top_block_different_colours(self):
		for *blocks, expected in permutations(Colour, 3):
			with self.subTest(blocks=blocks):
				self.assertEqual(top_block(blocks), expected)

	def test_next_row_same_colour(self):
		row = [Colour.blue, Colour.blue, Colour.blue]
		expected = [Colour.blue, Colour.blue]
		self.assertEqual(list(next_row(row)), expected)

	def test_next_row_different_colours(self):
		row = [Colour.red, Colour.green, Colour.blue]
		expected = [Colour.blue, Colour.red]
		self.assertEqual(list(next_row(row)), expected)

	def test_pyramid_peak_one(self):
		row = [Colour.red, Colour.blue, Colour.green, Colour.blue]
		self.assertEqual(pyramid_peak(row), Colour.green)

	def test_pyramid_peak_two(self):
		row = [Colour.red, Colour.red, Colour.green, Colour.blue]
		self.assertEqual(pyramid_peak(row), Colour.green)

if __name__ == "__main__":
	unittest.main()