import aoc_utils

prev_visited = set()

def move_tail(head_coords, tail_coords):
	if head_coords == tail_coords:
		return tail_coords
	elif head_coords[0] == tail_coords[0]:
		if head_coords[1] - tail_coords[1] > 1:
			return [tail_coords[0], tail_coords[1] + 1]
		elif head_coords[1] - tail_coords[1] < -1:
			return [tail_coords[0], tail_coords[1] - 1]
		else:
			return tail_coords
	elif head_coords[1] == tail_coords[1]:
		if head_coords[0] - tail_coords[0] > 1:
			return [tail_coords[0] + 1, tail_coords[1]]
		elif head_coords[0] - tail_coords[0] < -1:
			return [tail_coords[0] - 1, tail_coords[1]]
		else:
			return tail_coords
	elif abs(head_coords[0] - tail_coords[0]) == 1 and abs(head_coords[1] - tail_coords[1]) == 1:
		return tail_coords
	else:
		if head_coords[0] > tail_coords[0]:
			return [tail_coords[0] + 1, tail_coords[1] + 1] if head_coords[1] > tail_coords[1] else [tail_coords[0] + 1, tail_coords[1] - 1]

		if head_coords[1] > tail_coords[1]:
			return [tail_coords[0] - 1, tail_coords[1] + 1]
		else:
			return [tail_coords[0] - 1, tail_coords[1] - 1]

def solution(inp, tail_length: int):
	position = [[0, 0] for _ in range(10)]
	prev_visited = {(0, 0)}
	for line in inp:
		direction, amount = line.split()
		amount = int(amount)
		if direction == 'D':
			position[0][1] -= amount
		elif direction == 'L':
			position[0][0] -= amount
		elif direction == 'R':
			position[0][0] += amount
		elif direction == 'U':
			position[0][1] += amount
		for _ in range(amount):
			for x in range(1, tail_length + 1):
				position[x] = move_tail(position[x-1], position[x])
			prev_visited.add((position[tail_length][0], position[tail_length][1]))
	print(position)
	return(len(prev_visited))


if __name__ == '__main__':
	inp = aoc_utils.input_string_list()
	print(solution(inp, 1))
	print(solution(inp, 9))