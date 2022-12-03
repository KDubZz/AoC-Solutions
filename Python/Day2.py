import aoc_utils

aoc_utils.SAMPLE = False

games = aoc_utils.input_string_list()


def part_1():
    """
    solution for part 1
    """
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

def part_2():
    """
    solution for part 2
    """
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
    print('Part 1:', part_1())
    print('Part 2:', part_2())
