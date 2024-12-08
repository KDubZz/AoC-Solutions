import aocd

puzzle = aocd.models.Puzzle(year=2024, day=5)
inp = puzzle.input_data

rules, examples = inp.split('\n\n')

rules = [[int(i) for i in rule.split('|')] for rule in rules.splitlines()]
examples = [[int(i) for i in example.split(',')] for example in examples.splitlines()]

total = 0
wrong_examples = []

def check_example(rules, example):
    length = len(example)
    for i in range(length):
        for x in range(i+1, length):
            first, second = example[i], example[x]
            for rule in rules:
                if rule[0] == second and rule[1] == first:
                    return False
    return True

def part_1(rules, examples):
    total = 0
    wrong_examples = []
    for example in examples:
        if check_example(rules, example) == False:
            wrong_examples.append(example)
        else:
            total += example[len(example)//2]

    return total, wrong_examples

def part_2(rules, wrong_examples):
    new_total = 0
    for example in wrong_examples:
        t_rules = []
        for rule in rules:
            if rule[0] in example and rule[1] in example:
                t_rules.append(rule)
        for _ in range(len(t_rules)):
            for rule in t_rules:
                if example.index(rule[0]) > example.index(rule[1]):
                    example.append(example.pop(example.index(rule[1])))
        new_total += example[len(example)//2] if len(example) % 2 == 1 else 0
    return new_total

if __name__ == '__main__':
    total, wrong_examples = part_1(rules, examples)
    print(total)
    print(part_2(rules, wrong_examples))