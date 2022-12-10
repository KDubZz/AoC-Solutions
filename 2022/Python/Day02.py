import aoc_utils


def part_1(games):
    score = 0
    for i in range(2500):
        first = games[i].split(' ')[0]
        second = games[i].split(' ')[1]
        if first == 'A':
            if second == 'X':
                score += 4
            elif second == 'Y':
                score += 8
            else:
                score += 3
        elif first == 'B':
            if second == 'X':
                score += 1
            elif second == 'Y':
                score += 5
            else:
                score += 9
        elif second == 'X':
            score += 7
        elif second == 'Y':
            score += 2
        else:
            score += 6
    return score


def part_2(games):
    score = 0
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
        elif second == 'X':
            score += 2
        elif second == 'Y':
            score += 6
        else:
            score += 7
    return score


if __name__ == '__main__':
    games = aoc_utils.input_string_list()
    print('Part 1:', part_1(games))
    print('Part 2:', part_2(games))
