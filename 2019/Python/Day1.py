"""
import aoc_utils
import math

def parse(n: int):
	return math.floor(n/3) - 2


def infinite(n: int):
	fuel = parse(n)
	if fuel <= 0:
		return 0
	else:
		return fuel + infinite(fuel)


def part_1():
	return sum(parse(i) for i in aoc_utils.input_int_list())


def part_2():
	kount = 0
	for i in aoc_utils.input_int_list():
		kount += infinite(i)
	return(kount)


if __name__ == '__main__':
	print('Part 1:', part_1())
	print('Part 2:', part_2())

"""



def p(n):return n//3-2
def k(n):f=p(n);return 0if f<=0else f+k(f)
b = __import__('aoc_utils').input_int_list();print(sum(p(i)for i in b),sum(k(i)for i in b))

p=lambda n:n//3-2;k=lambda n:0if p(n)<=0else(p(n)+k(p(n)));b = __import__('aoc_utils').input_int_list();print(sum(p(i)for i in b),sum(k(i)for i in b))