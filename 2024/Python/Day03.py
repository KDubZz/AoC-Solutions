import aocd
import re

puzzle = aocd.models.Puzzle(year=2024, day=3)
inp = puzzle.input_data.splitlines() 

def part1(inp):
    reg_str = r"mul\(\d+,\d+\)"
    total = 0
    for line in inp:
        pattern = re.findall(reg_str, line)
        for item in pattern:
            first, second = item.split(',')
            total += int(first[4:])*int(second[:-1])
    return total

def part2(inp):
    reg_str = r"mul\(\d+,\d+\)|don\'t\(\)|do\(\)"
    total = 0
    do_state = True
    for line in inp:
        pattern = re.findall(reg_str, line)
        for item in pattern:
            if item == "don't()":
                do_state = False
            elif item == "do()":
                do_state = True
            else:
                first, second = item.split(',')
                total += int(first[4:])*int(second[:-1]) if do_state == True else 0
    return total

if __name__ == '__main__':
    print(part1(inp))
    print(part2(inp))