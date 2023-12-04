import aocd
from collections import *

puzzle = aocd.models.Puzzle(year=2023, day=3)
inp = puzzle.input_data.splitlines()

def process(inp, symbol):
	displacement = [-1, 0, 1]
	sym_to_num = defaultdict(set)
	for y in range(len(inp)):
		symbol_locations = []
		curr_num = "" 
		number_found = False
		for x in range(len(inp[y])):
			if inp[y][x].isdigit():
				curr_num += inp[y][x]
				for x_displacement in displacement:
					for y_displacement in displacement:
						if (x+x_displacement) >= 0 and (x+x_displacement) < len(inp[y]) and (y+y_displacement) >= 0 and (y+y_displacement) < len(inp) and inp[y+y_displacement][x+x_displacement] in symbol:
							number_found = True
      						symbol_locations.append((y+y_displacement, x+x_displacement))
			else:
				if number_found == True:
					for symbol_location in symbol_locations:
						sym_to_num[symbol_location].add(int(curr_num))
					number_found = False
					curr_num = ""
				symbol_locations = []
				curr_num = ""
		if number_found == True:
			for symbol_location in symbol_locations:
				sym_to_num[symbol_location].add(int(curr_num))
			curr_num = ""
			number_found = False
			symbol_locations = []
	return sym_to_num

if __name__ == '__main__':
	total = 0
	ntotal = 0
	sym_to_num = process(inp, "!£$%&*^_+@#/=-")
	for val in sym_to_num:
		total += sum(list(sym_to_num[val]))
	print(f"Part 1: {total}")
	ast_only = process(inp, "*")
	for val in ast_only:
		if len(sym_to_num[val]) == 2:
			num_1, num_2 = list(sym_to_num[val])
			ntotal += num_1 * num_2
	print(f"Part 2: {ntotal}")
