import aoc_utils


def part_1():
	diff = 0
	inp = aoc_utils.input_tab_list()
	for value in inp:
		for i in range(len(value)):
			value[i] = int(value[i])
		value = sorted(value, reverse=True)
		diff += int(value[0]) - int(value[-1])
	return diff


def part_2():
	diff = 0
	inp = aoc_utils.input_tab_list()
	for value in inp:
		for x in value:
			for y in value:
				if int(x) == int(y):
					continue
				elif int(x) % int(y) == 0:
					diff += int(x) // int(y)
	return diff

print(part_1(), part_2())
