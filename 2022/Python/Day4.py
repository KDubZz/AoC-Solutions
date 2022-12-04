import aoc_utils

inp = aoc_utils.input_string_list()

def part_1():
	count = 0
	for value in inp:
		s = value.split(',')[0]
		h = value.split(',')[1]
		s1, s2 = s.split('-')
		h1, h2 = h.split('-')
		"""
		if int(s1) >= int(h1) and int(s2) <= int(h2):
			count += 1
		elif int(s1) <= int(h1) and int(s2) >= int(h2):
			count += 1
		"""
		if int(s1) <= int(h2):
			if int(h1) <= int(s2):
				count += 1
	return count

if __name__ == '__main__':
	print('Part 1:', part_1())
