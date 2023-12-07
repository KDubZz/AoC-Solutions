import aocd

puzzle = aocd.models.Puzzle(year=2023, day=7)
inp = puzzle.input_data.splitlines()
example = puzzle.examples[0][0].splitlines()

def kind(card):
	card_values = {}
	for i in card:
		if i in card_values:
			card_values[i] += 1
		else:
			card_values[i] = 1
	tot_cards = set()
	highest = 0
	for i in card_values.items():
		if i[1] > 0:
			tot_cards.add(i[0])
			if i[1] > highest:
				highest = i[1]
	if len(list(tot_cards)) == 5:
		return 6
	elif len(list(tot_cards)) == 4:
		return 5
	elif len(list(tot_cards)) == 3:
		return 3 if highest == 3 else 4
	elif len(list(tot_cards)) == 2:
		return 2 if highest == 3 else 1
	elif len(list(tot_cards)) == 1:
		return 0

def count_and_adjust(cards, card, card_values):
        return cards.count(card) + (card_values['J'] if card != 'J' else 0)

def evaluate_hand(cards, tot_cards, card_values):
    if any(count_and_adjust(cards, card, card_values) == 5 for card in cards):
        return 0
    elif any(count_and_adjust(cards, card, card_values) == 4 for card in cards):
        return 1
    elif (card_values[tot_cards[0]] == 2 and card_values[tot_cards[1]] == 3) or \
         (card_values[tot_cards[0]] == 3 and card_values[tot_cards[1]] == 2) or \
         (len(tot_cards) == 3 and card_values['J'] == 1 and
          (card_values[tot_cards[0]] == 2 or card_values[tot_cards[1]] == 2)):
        return 2
    elif any(count_and_adjust(cards, card, card_values) == 3 for card in cards):
        return 3
    elif len(tot_cards) == 3:
        return 4
    elif any(count_and_adjust(cards, card, card_values) == 2 for card in cards):
        return 5
    else:
        return 6
def j_kind(cards):
	card_values = {'J': 0}
	tot_cards = []
	if 'J' in cards:
		tot_cards.append('J')
	for i in cards:
		if i in card_values:
			card_values[i] += 1
		else:
			card_values[i] = 1
			tot_cards.append(i)
	return evaluate_hand(cards, tot_cards, card_values)

def part_1(inp):
	total = []
	card_order = "23456789TJQKA"
	for line in inp:
		cards = line.split(' ')[0]
		bid = int(line.split(' ')[1])
		rank = kind(cards)
		process = False
		for i, val in enumerate(total):
			if process:
				break
			if val[0] == rank:
				for n in range(5):
					if card_order.find(val[1][n]) < card_order.find(cards[n]):
						total.insert(i, (rank, cards, bid))
						process = True
						break
					elif card_order.find(val[1][n]) > card_order.find(cards[n]):
						break
			if val[0] > rank:
				total.insert(i, (rank, cards, bid))
				process = True
				break
		if process == False:
			total.append((rank, cards, bid))
	return sum((len(total) - i) * val[2] for i, val in enumerate(total))

def part_2(inp):
	total = []
	j_card_order = "J23456789TQKA"
	for line in inp:
		cards = line.split(' ')[0]
		bid = int(line.split(' ')[1])
		rank = j_kind(cards)
		process = False
		for i, val in enumerate(total):
			if process:
				break
			if val[0] == rank:
				for n in range(5):
					if j_card_order.find(val[1][n]) < j_card_order.find(cards[n]):
						total.insert(i, (rank, cards, bid))
						process = True
						break
					elif j_card_order.find(val[1][n]) > j_card_order.find(cards[n]):
						break
			if val[0] > rank:
				total.insert(i, (rank, cards, bid))
				process = True
				break
		if process == False:
			total.append((rank, cards, bid))
	return sum((len(total) - i) * val[2] for i, val in enumerate(total))

if __name__ == '__main__':
	print(f"Part 1: {part_1(inp)}")
	print(f"Part 2: {part_2(inp)}")