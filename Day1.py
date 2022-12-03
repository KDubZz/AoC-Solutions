import aoc_utils

aoc_utils.SAMPLE = False

def sorted_num(calories: str) -> int:
    return sum(map(int, calories.splitlines()))

calories_sum = list(map(sorted_num, aoc_utils.input_block_list()))
print(max(calories_sum))
print(sorted(calories_sum[:-1]))
