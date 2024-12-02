import aocd
import itertools

puzzle = aocd.models.Puzzle(year=2024, day=2)
inp = puzzle.input_data.splitlines()

def check_if_valid(row):
    diffs = [(item[0]-item[1]) for item in list(itertools.pairwise(row))]
    if max(diffs) > 3 or min(diffs) < -3 or diffs.count(0) > 0:
        return False
    n, p = 0, 0
    for item in diffs:
        if item < 0:
            n += 1
        else:
            p += 1
    if p > 0 and n > 0:
        return False
    return True

def part_1(inp):
    safe_total = 0
    for line in inp:
        row = [int(i) for i in line.split(' ')]
        safe_total += 1 if check_if_valid(row) == True else 0
    return safe_total

def part_2(inp):
    safe_total = 0
    for line in inp:
        row = [int(i) for i in line.split(' ')]
        if check_if_valid(row) == True:
            safe_total += 1
        else:
            for i, item in enumerate(row):
                new_row = list(row)
                new_row.pop(i)
                if check_if_valid(new_row) == True:
                    safe_total += 1
                    break
    return safe_total

if __name__ == '__main__':
    print(part_1(inp))
    print(part_2(inp))