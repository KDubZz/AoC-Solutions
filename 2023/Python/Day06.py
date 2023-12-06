import aocd

puzzle = aocd.models.Puzzle(year=2023, day=6)
inp = puzzle.input_data.splitlines()

def part_1(inp):
	times = [int(i) for i in inp[0].split(' ') if i.isdigit()]
	dist = [int(i) for i in inp[1].split(' ') if i.isdigit()]
	total = 1
	for i, time in enumerate(times):
		total *= sum((time-x) * x > dist[i] for x in range(time))
	return total

def part_2(inp):
	time = int(''.join([i for i in inp[0].split(' ') if i.isdigit()]))
	dist = int(''.join([i for i in inp[1].split(' ') if i.isdigit()]))
	return sum((time-x) * x > dist for x in range(time))

if __name__ == '__main__':
	print(part_1(inp))
	print(part_2(inp))