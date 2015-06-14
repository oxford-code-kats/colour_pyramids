from enum import Enum


class Colour(Enum):
	red = 1
	blue = 2
	green = 3

top_blocks = {
	frozenset([Colour.red]): Colour.red,
	frozenset([Colour.blue]): Colour.blue,
	frozenset([Colour.green]): Colour.green,
	frozenset([Colour.red, Colour.green]): Colour.blue,
	frozenset([Colour.red, Colour.blue]): Colour.green,
	frozenset([Colour.green, Colour.blue]): Colour.red,
}

def top_block(colours):
	return top_blocks[frozenset(colours)]

def next_row(row):
	for block_pair in zip(row, row[1:]):
		yield top_block(block_pair)

def pyramid_peak(row):
	while len(row) > 1:
		row = list(next_row(row))
	return row[0]



