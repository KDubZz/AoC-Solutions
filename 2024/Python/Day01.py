import aocd

puzzle = aocd.models.Puzzle(year=2024, day=1)
inp = puzzle.input_data.splitlines()

def process_data(inp):
    left_list = []
    right_list = []
    for row in inp:
        left, right = row.split('   ')
        left_list.append(int(left))
        right_list.append(int(right))

    left_list.sort()
    right_list.sort()

    return (left_list, right_list)

def part_1(inp):
    difference_total = 0

    left_list, right_list = process_data(inp)

    for i, item in enumerate(left_list):
        difference_total += abs(item - right_list[i])

    return difference_total

def part_2(inp):
    similarity_total = 0
    left_list, right_list = process_data(inp)

    for item in left_list:
        similarity_total += item * right_list.count(item)

    return similarity_total

if __name__ == '__main__': 
    print(f"Part 1: {part_1(inp)}\nPart 2: {part_2(inp)}")