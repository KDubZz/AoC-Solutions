import aoc_utils
import itertools


def rock_block(start, end):
	global grid, bottom
	from_x, from_y = list(map(int, start.split(',')))
	to_x, to_y = list(map(int, end.split(',')))
	bottom = max(bottom, max(from_y, to_y))
	x_diff = to_x - from_x
	y_diff = to_y - from_y
	diff_x = 0 if x_diff == 0 else x_diff // abs(x_diff)
	diff_y = 0 if y_diff == 0 else y_diff // abs(y_diff)
	while from_x != to_x or from_y != to_y:
		grid.add((from_x, from_y))
		from_x += diff_x
		from_y += diff_y
		grid.add((from_x, from_y))


def sand_drop():
	start_x, start_y = 500, 0
	if (start_x, start_y) in grid:
		return False
	for _ in range(100000):
		if (start_x, start_y + 1) not in grid:
			start_y += 1
		elif (start_x - 1, start_y + 1) not in grid:
			start_x -= 1
			start_y += 1
		elif (start_x + 1, start_y + 1) not in grid:
			start_x += 1
			start_y += 1
		else:
			grid.add((start_x, start_y))
			return True


def part_1():
	count = 0
	for i in inp:
		splitted = i.split('->')
		for start, end in itertools.pairwise(splitted):
			rock_block(start, end)

	while sand_drop():
		count += 1
	return count


def part_2():
	count = 0
	for i in inp:
		splitted = i.split('->')
		for start, end in itertools.pairwise(splitted):
			rock_block(start, end)
	rock_block(f"-10000,{str(bottom + 2)}", f"10000,{str(bottom + 2)}")
	
	while sand_drop():
		count += 1
	return count


if __name__ == '__main__':
	inp = aoc_utils.input_string_list()
	start_x, start_y = 1000, 1000
	bottom = 0
	grid = set()
	print('Part 1:', part_1())
	grid = set()
	print('Part 2:', part_2())