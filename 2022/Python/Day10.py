import aoc_utils


def spec_sum(values):
	return sum(x * y for x, y in zip(range(20, 221, 40), values[19::40]))


def write_lines(lst):
	for i in range(len(lst) // 40):
		for x in range(40):
			current = lst[i * 40 + x]
			if abs(current-x) <= 1:
				print('█', end='')
			else:
				print(' ', end='')
		print()


def part_1(inp_list):
	x = 1
	prev_values = []
	for value in inp_list:
		try:
			action, num = value.split(' ')
		except ValueError:
			action = value
		prev_values.append(x)
		if action == 'addx':
			prev_values.append(x)
			x += int(num)
	return spec_sum(prev_values), prev_values


if __name__ == '__main__':
	inp = aoc_utils.input_string_list()
	first_ans = part_1(inp)[0]
	prev_values = part_1(inp)[1]
	print('Part 1:', first_ans)
	print('\n\n')
	write_lines(prev_values)
	print('\n\n')		