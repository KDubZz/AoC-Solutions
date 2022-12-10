import aoc_utils

def fin_list(inp):
	row = list(range(128))
	col = list(range(8))
	final_list = []
	for value in inp:
		for i in range(len(value)):
			if value[i] == 'F':
				row = row[:len(row) // 2]
			elif value[i] == 'B':
				row = row[len(row) // 2:]
			elif value[i] == 'L':
				col = col[:len(col) // 2]
			elif value[i] == 'R':
				col = col[len(col) // 2:]
		fin_row = row[0]
		fin_col = col[0]
		row = list(range(128))
		col = list(range(8))
		seat_id = (fin_row * 8) + fin_col
		final_list.append(seat_id)
	return(sorted(final_list))

if __name__ == '__main__':
	inp = aoc_utils.input_string_list()
	lst = fin_list(inp)
	part_1 = max(lst)
	count = lst[0]
	for i in lst:
		if i != count + 1:
			part_2 = i-1
		count = i
	print('Part 1:', part_1)
	print('Part 2:', part_2)