import string
import aoc_utils

d = dict(zip(string.ascii_letters, range(1,53)))

def part_1(list_input):
    priority = 0
    for i,value in enumerate(list_input):
        first_half = value[:len(value)//2]
        second_half = value[len(value)//2:]
        for i in first_half:
            if i in second_half:
                priority += (d[i])
                break
    return priority


def part_2(list_input):
    priority = 0
    for i in range(0, len(list_input), 3):
        first_elf = list_input[i]
        second_elf = list_input[i+1]
        third_elf = list_input[i+2]
        for letter in first_elf:
            if letter in second_elf and letter in third_elf:
                priority += (d[letter])
                break
    return priority

if __name__ == '__main__':
    inp = aoc_utils.input_string_list()
    print('Part 1:', part_1(inp))
    print('Part 2:', part_2(inp))
