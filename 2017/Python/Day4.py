import aoc_utils
import operator as op
from itertools import permutations

def part_1():
	inp = aoc_utils.input_string_space_list()
	val_count = 0
	true_count = 0
	bad_count = 0
	for elem in inp:
		for val in elem:
			if op.countOf(elem, val) == 1:
				val_count += 1
			else:
				bad_count += 1
				break
		if bad_count == 0:
			true_count += 1
		bad_count = 0
	return true_count


def part_2():
	inp = aoc_utils.input_string_space_list()
	true_count = 0
	worse_count = 0
	for elem in inp:
		possibilities = []
		for val in elem:
			possibilities += [''.join(p) for p in permutations(val)]
			possibilities = list(filter(lambda a: a != val, possibilities))
		for val in elem:
			if val in possibilities:
				worse_count += 1
		break
	if worse_count == 0:
		true_count += 1
	worse_count = 0

	return true_count


print(part_1(), part_2())