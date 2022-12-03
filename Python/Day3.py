import string
import aoc_utils

aoc_utils.SAMPLE = False

d = dict(zip(string.ascii_letters, range(1,53)))

def solutions():
    """
    answers for both parts 1 and 2
    """
    priority = 0
    priority2 = 0

    list_input = aoc_utils.input_string_list()

    for i,value in enumerate(list_input):
        first_half = value[:len(value)//2]
        second_half = value[len(value)//2:]
        for i in first_half:
            if i in second_half:
                priority += (d[i])
                break

    i = 0

    while i < len(list_input):
        first_elf = list_input[i]
        second_elf = list_input[i+1]
        third_elf = list_input[i+2]
        for letter in first_elf:
            if letter in second_elf and letter in third_elf:
                priority2 += (d[letter])
                break
        i += 3
    print('Part 1 =', priority)
    print('Part 2 =', priority2)

if __name__ == '__main__':
    solutions()
