import aocd

puzzle = aocd.models.Puzzle(year=2023, day=1)
inp = puzzle.input_data.splitlines()

def part1(inp):
	nums_only = []
	for value in inp:
		temp = ''.join(char for char in value if char.isdigit())
		nums_only.append(temp)
	return sum(int(f"{line[0]}{line[-1]}") for line in nums_only)

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
	return part1(reset_nums_only)

if __name__ == '__main__':
	print(f"Part 1: {part1(inp)}")
	print(f"Part 2: {part2(inp)}")
	puzzle.answer_a = part1(inp)
	puzzle.answer_b = part2(inp)