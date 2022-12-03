import aoc_utils

aoc_utils.SAMPLE = False

with open('Day2.txt') as f:
    games = f.read().splitlines()

print(games)

score = 0

print(games)

for i in range(2500):
    first = games[i].split(' ')[0]
    second = games[i].split(' ')[1]
    if first == 'A':
        if second == 'X':
            score += 3
        elif second == 'Y':
            score += 4
        else:
            score += 8
    elif first == 'B':
        if second == 'X':
            score += 1
        elif second == 'Y':
            score += 5
        else:
            score += 9
    else:
        if second == 'X':
            score += 2
        elif second == 'Y':
            score += 6
        else:
            score += 7

print(score)