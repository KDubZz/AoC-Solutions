import aoc_utils
from collections import defaultdict


def part_1(inp, store, x):
	for i in range(len(inp)):
		line = inp[i].split()
		if line[0].isnumeric():
			for i, value in enumerate(x):
				store['/'.join(x[:i+1])] += int(line[0])
		if line[1] == 'cd':
			if line[2] == '..':
				x.pop()
			else:
				x.append(line[2])
	return sum(val for val in store.values() if val<=100000)
			

def part_2(inp, store, x):
	for i in range(len(inp)):
		line = inp[i].split()
		if line[0].isnumeric():
			for i, value in enumerate(x):
				store['/'.join(x[:i+1])] += int(line[0])
		if line[1] == 'cd':
			if line[2] == '..':
				x.pop()
			else:
				x.append(line[2])
	prev_val = 1000000000
	for val in store.values():
		if val >= store['/'] - 40000000 and val < prev_val:
			prev_val = val
	return prev_val
	
	
if __name__ == '__main__':
	inp = aoc_utils.input_string_list()
	store = defaultdict(int)
	empty = []
	print('Part 1:', part_1(inp, store, empty))
	store = defaultdict(int)
	empty = []
	print('Part 2:', part_2(inp, store, empty))