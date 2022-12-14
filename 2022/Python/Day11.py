import aoc_utils
import math
import itertools

def create_sum(x, y, operand):
	if operand == '*':
		return x * y
	elif operand == '+':
		return x + y

inp = aoc_utils.input_block_list()
l = []
for i in inp:
	s = i.split('\n')
	for x in s:
		x = x.strip()
		l.append(x)

m_count = 0
operations = []
true_m = []
false_m = []
sumup = []
tests = []

for item in l:
	if 'Monkey ' in item:
		m_count = int(item[7])
	elif 'Test: ' in item:
		divisor = item.split(' ')[-1]
		divisor = int(divisor)
		tests.append(divisor)
	elif 'If true: ' in item:
		true_m.append(int(item.split(' ')[-1]))
	elif 'If false: ' in item:
		false_m.append(int(item.split(' ')[-1]))
	elif 'Operation: ' in item:
		sumup.append(item.split('=')[1])

def solve(a):
	amount = [0 for _ in range(len(l))]
	nums = [list(map(int, item.split(':')[1].split(','))) for item in l if 'Starting items:' in item]
	n = 20 if a == 1 else 10000
	for _, i in itertools.product(range(n), range(8)):
		while len(nums[i]) != 0:
			amount[i] += 1
			old = nums[i].pop()
			if a == 2:
				lcm = math.lcm(*tests)
				new = eval(sumup[i]) % lcm
			else:
				new = eval(sumup[i]) // 3
			if new%tests[i] == 0:
				nums[true_m[i]].append(new)
			else:
				nums[false_m[i]].append(new)
	amount.sort()
	return amount[-1] * amount[-2]

if __name__ == '__main__':
	print('Part 1:', solve(1))
	print('Part 2:', solve(2))