import aocd
from more_itertools import chunked

puzzle = aocd.models.Puzzle(year=2023, day=5)
inp = puzzle.input_data.splitlines()
example = [i for i in puzzle.examples[0][0].splitlines() if i != '']

def main(lines):
	seeds = [int(s) for s in lines[0][len('seeds: '):].split(' ')]
	chunked_seeds = list(chunked(seeds, 2))
	nlist = []
	for seed_pair in chunked_seeds:
		nlist += list(range(seed_pair[0], seed_pair[0]+seed_pair[1]))
	map_order = []
	ranges = {}
	current_ranges = []
	map_name = 'seed-to-soil'
	for idx in range(3, len(lines)):
		l = lines[idx]
		if len(l) <= 0:
			continue
		if "-to-" in l:
			ranges[map_name] = current_ranges
			map_order.append(map_name)
			map_name = l.split(' ')[0]
			current_ranges = []
		else:
			nums = l.split(' ')
			current_ranges.append([int(num) for num in nums])
	ranges[map_name] = current_ranges
	map_order.append(map_name)
	return (find_lowest(seeds, map_order, ranges), find_lowest(nlist, map_order, ranges))

def find_lowest(arg0, map_order, ranges):
	nbest = float('inf')
	for seed in arg0:
		curr = seed
		for m in map_order:
			for r in ranges[m]:
				if curr >= r[1] and curr <= (r[1] + r[2] - 1):
					curr += (r[0] - r[1])
					break
		nbest = min(nbest, curr)
	return nbest

if __name__ == '__main__':
	sols = main(inp)
	for i, sol in enumerate(list(sols)):
		print(f"Part {i+1}: {sol}")