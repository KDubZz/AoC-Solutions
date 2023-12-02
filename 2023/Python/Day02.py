import aocd

puzzle = aocd.models.Puzzle(year=2023, day=2)
inp = puzzle.input_data.splitlines()

def process(inp):
	id_sum, power_sum = 0, 0
	for line in inp:
		game_id = line.split(':')[0]
		games = line.split(':')[1].split(';')
		num_id = int(''.join([char for char in game_id if char.isdigit()]))
		red_high, green_high, blue_high = 0, 0, 0
		for game in games:
			game = game.replace(',', '')
			colours = game.split(' ')[1:]
			temp = 0
			for i in colours:
				if i.isdigit():
					temp = int(i)
				else:
					if i == 'red':
						if temp > red_high:
							red_high = temp
					elif i == 'blue':
						if temp > blue_high:
							blue_high = temp
					elif i == 'green':
						if temp > green_high:
							green_high = temp
		if red_high <= 12 and green_high <= 13 and blue_high <= 14:
			id_sum += num_id
		power_sum += red_high*green_high*blue_high
	return (id_sum, power_sum)

if __name__ == '__main__':
	print(f"Part 1: {process(inp)[0]}\nPart 2: {process(inp)[1]}")