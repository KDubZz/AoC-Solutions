import aoc_utils

with open('/workspaces/AoC-Solutions/2022/Python/inputs/Day4.txt', "r", encoding='UTF-8') as file:
    inp = [line.rstrip() for line in file]

def part_1():

	acc = 0
	jmp = 0
	count = 0

	while count < len(inp):
		value = inp[count]
		if '+' in value:
			value = value.replace('+', '')
		if 'z' in value:
			return acc
		if 'jmp' in value:
			jmp = int(value[4:])
			count += jmp
		elif 'acc' in value:
			if abs(int(value[4:])) < acc:
				acc += int(value[4:])
				count += 1
			else:
				count += 1
		else:
			count += 1
		value += 'z'

if __name__ == '__main__':
	print('Part 1:', part_1())
