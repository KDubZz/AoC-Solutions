import functools
import aoc_utils

inp = aoc_utils.input_block_list()


def compare_values(a, b):
	if type(a) == type(b) == type(1):
		if a < b:
			return -1
		elif a > b:
			return 1
		else:
			return 0
	if type(a) != type(b):
		if type(a) == type(1):
			a = [a]
		if type(b) == type(1):
			b = [b]
	if len(a) == 0 and len(b) == 0:
		return 0
	if len(b) == 0:
		return 1
	if len(a) == 0:
		return -1
	if type(a) == type(b) == type([]):
		compare = compare_values(a[0], b[0])
		return compare_values(a[1:], b[1:]) if compare == 0 else compare

def solve(num):
	count = 0
	increment = 1
	lists = []
	for line in inp:
		a, b = line.split()
		if compare_values(eval(a), eval(b)) == -1:
			count += increment
		lists.extend((eval(a), eval(b)))
		increment += 1
	lists.extend(([[2]], [[6]]))
	lists.sort(key=functools.cmp_to_key(compare_values)) #props to Max Bowman like wtf even is this
	for i in range(len(lists)):
		if str(lists[i]) == "[[2]]":
			x = i + 1
		if str(lists[i]) == "[[6]]":
			y = i + 1
	return count if num == 1 else x * y


if __name__ == '__main__':
	print('Part 1:', solve(1))
	print('Part 2:', solve(2))