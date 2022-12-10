import aoc_utils


def part_1():
	
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
			transit = crates[start].pop()
			crates[end] += transit
	return ''.join(crate[-1] for crate in crates)

if __name__ == '__main__':
	print('Part 1:', part_1(), '\nPart 2:', part_2())
