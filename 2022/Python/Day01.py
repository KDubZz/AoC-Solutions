import aoc_utils

def sorted_num(calories: str) -> int:
    return sum(map(int, calories.splitlines()))

if __name__ == '__main__':
    calories_sum = list(map(sorted_num, aoc_utils.input_block_list()))
    print('Part 1:', max(calories_sum))
    print('Part 2:', sum(sorted(calories_sum, reverse=True)[:3]))
