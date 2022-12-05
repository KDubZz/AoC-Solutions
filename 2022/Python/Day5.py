import aoc_utils


def part_1():
	"""
	inp = aoc_utils.input_string_list()
	crates = [[' ', 'C', ' ', ' ', ' ', 'L', ' ', ' ', 'T'], [' ', 'V', 'R', 'M', ' ', 'T', ' ', ' ', 'B'], [' ', 'F', 'G', 'H', 'Q', 'Q', ' ', ' ', 'H'], [' ', 'W', 'L', 'P', 'V', 'M', 'V', ' ', 'F'], [' ', 'P', 'C', 'W', 'S', 'Z', 'B', 'S', 'P'], ['G', 'R', 'M', 'B', 'F', 'J', 'S', 'Z', 'D'], ['Z', 'Q', 'F', 'L', 'G', 'W', 'H', 'F', 'M']]
	for i in range(len(inp)):
		inp[i] = inp[i].replace('move ', '')
		inp[i] = inp[i].replace(' from ', '-')
		inp[i] = inp[i].replace(' to ', '-')
		l = inp[i].split('-')
		a = int(l[0])
		b = int(l[1])
		c = int(l[2])
		x = 0
		y = 0
		for _ in range(a):
			value = crates[x][b-1]
			if value == ' ':
				x += 1
			else:
				col = value
				colVal = crates[x].index(col)
				crates[colVal] = ' '
				while crates[y][c-1] == ' ' and y < len(crates) - 1:
					y += 1
					print(col)
					print(y)
					if crates[y][c-1] != ' ':
						crates[y-1][c-1] += col
						crates[y-1][c-1].strip()
					if c-1 == len(crates[x]) and crates[y][c-1] == ' ':
						crates[y][c-1] += col
						crates[y][c-1].strip()
						
			x = 0
			y = 0



	return crates
	"""
	inp = aoc_utils.input_string_list()
	crates = [['Z', 'J', 'G'], ['Q', 'L', 'R', 'P', 'W', 'F', 'V', 'C'], ['F', 'P', 'M', 'C', 'L', 'G', 'R'], ['L', 'F', 'B', 'W', 'P', 'H', 'M'], ['G', 'C', 'F', 'S', 'V', 'Q'], ['W', 'H', 'J', 'Z', 'M', 'Q', 'T', 'L'], ['H', 'F', 'S', 'B', 'V'], ['F', 'J', 'Z', 'S'], ['M', 'C', 'D', 'P', 'F', 'H', 'B', 'T']]
	for i in range(len(inp)):
		inp[i] = inp[i].replace('move ', '')
		inp[i] = inp[i].replace(' from ', '-')
		inp[i] = inp[i].replace(' to ', '-')
	for i in range(len(inp)):
		splitter = inp[i].split('-')
		quant = int(splitter[0])
		start = int(splitter[1]) - 1
		end = int(splitter[2]) - 1
		for _ in range(quant):
			transit = crates[start].pop()
			crates[end].append(transit)
	return ''.join(crate[-1] for crate in crates)

		
def part_2():
	inp = aoc_utils.input_string_list()
	crates = [['Z', 'J', 'G'], ['Q', 'L', 'R', 'P', 'W', 'F', 'V', 'C'], ['F', 'P', 'M', 'C', 'L', 'G', 'R'], ['L', 'F', 'B', 'W', 'P', 'H', 'M'], [
		'G', 'C', 'F', 'S', 'V', 'Q'], ['W', 'H', 'J', 'Z', 'M', 'Q', 'T', 'L'], ['H', 'F', 'S', 'B', 'V'], ['F', 'J', 'Z', 'S'], ['M', 'C', 'D', 'P', 'F', 'H', 'B', 'T']]
	for i in range(len(inp)):
		inp[i] = inp[i].replace('move ', '')
		inp[i] = inp[i].replace(' from ', '-')
		inp[i] = inp[i].replace(' to ', '-')
	for i in range(len(inp)):
		splitter = inp[i].split('-')
		quant = int(splitter[0])
		start = int(splitter[1]) - 1
		end = int(splitter[2]) - 1
		for _ in range(quant):
			if quant > 1:
				transit = crates[start][len(crates[start])-quant:]
				crates[start] = crates[start][:len(crates[start])-quant]
				crates[end] += transit
				break
			if crates[start] == []:
				continue
			else:
				transit = crates[start].pop()
				crates[end] += transit
	return ''.join(crate[-1] for crate in crates)


print('Part 1:', part_1(), '\nPart 2:', part_2())
