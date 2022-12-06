import aoc_utils

import more_itertools


def part_1():
	inp = aoc_utils.input_string()
	for count, value in enumerate(more_itertools.windowed(inp, 4)):
		if len(set(value)) == 4:
			return count + 4


def part_2():
	inp = aoc_utils.input_string()
	for count, value in enumerate(more_itertools.windowed(inp, 14)):
		if len(set(value)) == 14:
			return count + 14



if __name__ == '__main__':
	print('Part 1:', part_1(), '\nPart 2:', part_2())