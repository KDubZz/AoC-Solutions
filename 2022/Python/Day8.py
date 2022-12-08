import aoc_utils
from functools import reduce

lines = aoc_utils.input_string_list()
lst = [[] for _ in range(99)]
for i, line in enumerate(lines):
	for b in line:
		lst[i].append(b)

def done(lst, x, y):
	current = lst[y][x]
	count = [True for _ in range(4)]
	for i in range(x):
		if lst[y][i] >= current:
			count[0] = False
			break
	for i in range(1, len(lines)-x):
		if lst[y][x+i] >= current:
			count[1] = False
			break
	for i in range(y):
		if lst[i][x] >= current:
			count[2] = False
			break
	for i in range(1, len(lines)-y):
		if lst[y+i][x] >= current:
			count[3] = False
			break
	return True in count


def score(lst, x, y):
	current = lst[y][x]
	count = [0 for _ in range(4)]
	for i in range(x):
		count[0] += 1
		if lst[y][x-i-1] >= current:
			break
	for i in range(1, len(lines)-x):
		count[1] += 1
		if lst[y][x+i] >= current:
			break
	for i in range(y):
		count[2] += 1
		if lst[y-i-1][x] >= current:
			break
	for i in range(1, len(lines)-y):
		count[3] += 1
		if lst[y+i][x] >= current:
			break
	return reduce((lambda m, n: m*n), count)

def part_1():
	ans = 0
	for y, line in enumerate(lines):
		for x, char in enumerate(line):
			if done(lst, x, y):
				ans += 1
	return ans
def part_2():
	ans = 0
	for y, line in enumerate(lines):
		for x, char in enumerate(line):
			if score(lst, x, y) > ans:
				ans = score(lst, x, y)
	return ans

if __name__ == '__main__':
	print('Part 1:', part_1())
	print('Part 2:', part_2())