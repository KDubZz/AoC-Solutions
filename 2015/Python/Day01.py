import aocd

puzzle = aocd.models.Puzzle(year=2015, day=3)
inp = puzzle.input_data
example = puzzle.examples

print(example)

visited = []
cur = (0, 0)

for i in inp:
	visited.append(cur)
	if i == '>':
		cur = (cur[0]+1, cur[1])
	elif i == '^':
		cur = (cur[0], cur[1]+1)
	elif i == 'v':
		cur = (cur[0], cur[1]-1)
	else:
		cur = (cur[0]-1, cur[1])
	visited.append(cur)

visited = set(visited)

puzzle.answer_a = len(list(visited))

visited = []

cur = (0, 0)
r_cur = (0, 0)

r = False

for i in inp:
	if r == False:
		visited.append(cur)
		if i == '>':
			cur = (cur[0]+1, cur[1])
		elif i == '^':
			cur = (cur[0], cur[1]+1)
		elif i == 'v':
			cur = (cur[0], cur[1]-1)
		else:
			cur = (cur[0]-1, cur[1])
		visited.append(cur)
		r = True
	else:
		visited.append(r_cur)
		if i == '>':
			r_cur = (r_cur[0]+1, r_cur[1])
		elif i == '^':
			r_cur = (r_cur[0], r_cur[1]+1)
		elif i == 'v':
			r_cur = (r_cur[0], r_cur[1]-1)
		else:
			r_cur = (r_cur[0]-1, r_cur[1])
		visited.append(r_cur)
		r = False

visited = set(visited)

puzzle.answer_b = len(list(visited))