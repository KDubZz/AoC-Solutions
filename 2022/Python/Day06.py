import aoc_utils
import more_itertools

def solve(window, inp):
	for count, value in enumerate(more_itertools.windowed(inp, window)):
		if len(set(value)) == window:
			return count + window

if __name__ == '__main__':
	part_1_window = 4
	part_2_window = 14
	inp = aoc_utils.input_string()
	print('Part 1:', solve(part_1_window, inp))
	print('Part 2:', solve(part_2_window, inp))
