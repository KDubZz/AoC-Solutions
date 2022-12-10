import aoc_utils


def process(s1, s2, h1, h2, part):
	count = 0
	if part == 1:
		if int(s1) >= int(h1) and int(s2) <= int(h2):
			count += 1
		elif int(s1) <= int(h1) and int(s2) >= int(h2):
			count += 1
	elif part == 2:
		if int(s1) <= int(h2) and int(h1) <= int(s2):
			count += 1
	else:
		return 'Invalid argument for part.'
	return count


def solve(inp):
	count, count2 = 0, 0
	for value in inp:
		s = value.split(',')[0]
		h = value.split(',')[1]
		s1, s2 = s.split('-')
		h1, h2 = h.split('-')
		count += process(s1, s2, h1, h2, 1)
		count2 += process(s1, s2, h1, h2, 2)
	return count, count2


if __name__ == '__main__':
	inp = aoc_utils.input_string_list()
	print('Part 1:', solve(inp)[0])
	print('Part 2:', solve(inp)[1])
