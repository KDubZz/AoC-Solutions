import aoc_utils

def next_number_1():
	inp = aoc_utils.input_string()
	count = 0
	length = len(inp)
	for i in range(len(inp)):
		s = int(inp[i%length])
		h = int(inp[(i+1)%length])
		if s == h:
			count += s
	return count

def next_number_2():
	inp = aoc_utils.input_string()
	count = 0
	length = len(inp)
	for i in range(len(inp)):
		s = int(inp[i % length])
		h = int(inp[(i+(length//2)) % length])
		if s == h:
			count += s
	return count

print('Part 1:', next_number_1(), '\nPart 2:', next_number_2())