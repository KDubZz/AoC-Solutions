import aocd

puzzle = aocd.models.Puzzle(year=2023, day=1)
inp = puzzle.input_data.splitlines()

def part1(inp):
	nums_only = []
	total = 0
	for value in inp:
		temp = ''
		for char in value:
			if char.isdigit():
				temp += char
		nums_only.append(temp)
	for line in nums_only:
		total += int(f"{line[0]}{line[-1]}")
	return total

def part2(inp):
	str_nums = ['one','two','three','four','five','six','seven','eight','nine']
	replacement_str_nums = ['o1e', 't2o', 't3e', 'f4r', 'f5e', 's6x', 's7n', 'e8t', 'n9e']
	counter = 0
	reset_nums_only = []
	for value in inp:
		temp = value
		for number in str_nums:
			if number in temp:
				temp = temp.replace(number, replacement_str_nums[str_nums.index(number)])
		reset_nums_only.append(temp)
	counter = part1(reset_nums_only)
	return counter

if __name__ == '__main__':
	print(f"Part 1: {part1(inp)}")
	print(f"Part 2: {part2(inp)}")