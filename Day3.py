import aoc_utils

aoc_utils.SAMPLE = False

import string

d = dict(zip(string.ascii_letters, range(1,53)))

priority = 0
priority2 = 0

list_input = aoc_utils.input_string_list()
print(list_input)


for i in range(len(list_input)):
    s = list_input[i][:len(list_input[i])//2]
    f = list_input[i][len(list_input[i])//2:]
    for i in s:
        if i in f:
            priority += (d[i])
            break

i = 0

while i < len(list_input):
    a = list_input[i]
    b = list_input[i+1]
    c = list_input[i+2]
    for x in a:
        if x in b and x in c:
                priority2 += (d[x])
                break
    i += 3
    
print('Part 1 =', priority)
print('Part 2 =', priority2)