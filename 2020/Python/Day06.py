import aoc_utils
import textwrap

x = aoc_utils.input_block_list()

def part_1(inp):
	num = 0
	string  = ''
	for i in inp:
		s = i.split('\n')
		for i in s:
			string += i
		num += len(set(string))
		string = ''
	return num

def part_2(inp):
	num = 0
	string = ''
	lst = []
	for i in inp:
		s = i.split('\n')
		num_of_people = len(s)
		for i in range(num_of_people):
			l = textwrap.wrap(s[i], 1)
			print(l)
			lst += l
		if num_of_people == 1:
			print(s)
			print(len(set(lst)))
			num += len(set(lst))
		else:
			ans = set(lst).intersection(iter(lst))
			print(lst)
			print(set(lst).intersection())
			num += len(ans)
		lst = []
	return num
print(part_1(x))
print(part_2(x))