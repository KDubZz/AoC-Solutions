import aocd

puzzle = aocd.models.Puzzle(year=2016, day=1)
inp = puzzle.input_data.split(', ')
sample = "R8, R4, R4, R8".split(', ')

n, e = 0, 0

direction = 0

visited = set()

found = False

for item in inp:
    turn = item[0]
    steps = int(item[1:])
    direction += 90 if turn == 'R' else -90
    if direction == 360:
        direction = 0
    elif direction == -90:
        direction = 270
    if direction == 0:
        for i in range(steps):
            n += 1
            if ((e, n)) in visited:
                print(abs(n) + abs(e))
                found = True
                break
            visited.add((e, n))
    elif direction == 90:
        for i in range(steps):
            e += 1
            if ((e, n)) in visited:
                print(abs(n) + abs(e))
                found = True
                break
            visited.add((e, n))
    elif direction == 180:
        for i in range(steps):
            n -= 1
            if ((e, n)) in visited:
                print(abs(n) + abs(e))
                found = True
                break
            visited.add((e, n))
    else:
        for i in range(steps):
            e -= 1
            if ((e, n)) in visited:
                print(abs(n) + abs(e))
                found = True
                break
            visited.add((e, n))
    if found == True:
        break

print(abs(n) + abs(e))
