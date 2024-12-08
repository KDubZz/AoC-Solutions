import aocd
import itertools

puzzle = aocd.models.Puzzle(year=2024, day=7)
inp = puzzle.input_data.splitlines()

def get_operator_combinations(part, num_operators):
    return ["".join(comb) for comb in itertools.product(["*", "+", "|"], repeat=num_operators)] if part == 2 else ["".join(comb) for comb in itertools.product(["*", "+"], repeat=num_operators)]

def process(part, inp):
    ans_sum = 0
    for line in inp:
        ans = int(line.split(':')[0])
        vals = [int(i) for i in line[line.index(':')+2:].split(' ')]
        num_operators = len(vals)-1
        combinations = get_operator_combinations(part, num_operators)
        for comb in combinations:
            l = list(comb)
            result = vals[0]
            for i in range(len(vals)):
                if i+1 == len(vals):
                    continue
                if l[i] == '+':
                    result += vals[i+1]
                elif l[i] == '*':
                    result *= vals[i+1]
                elif part == 2 and l[i] == '|':
                    result = int(str(result) + str(vals[i+1]))
            if result == ans:
                ans_sum += ans
                break
    return ans_sum

if __name__ == '__main__':
    print(process(1, inp))
    print(process(2, inp))