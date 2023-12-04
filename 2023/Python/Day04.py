import aocd

puzzle = aocd.models.Puzzle(year=2023, day=4)
inp = puzzle.input_data.splitlines()

def process(inp):
	total = 0
	cards = [1 for _ in range(len(inp))]
	for x, card in enumerate(inp):
		winning = [int(i) for i in card.split(':')[1].split('|')[0].strip().split(' ') if i!= '']
		pos = [int(i) for i in card.split(':')[1].split('|')[1].strip().split(' ') if i!= '']
		card_tot = 0
		match_tot = 0
		for val in winning:
			if val in pos:
				match_tot += 1
				if card_tot == 0:
					card_tot += 1
				else:
					card_tot *= 2
		for match in range(match_tot):
			cards[x + match + 1] += cards[x]
		total += card_tot
	return total, sum(cards)

if __name__ == '__main__':
	print(f"Part 1: {process(inp)[0]}")
	print(f"Part 2: {process(inp)[1]}")