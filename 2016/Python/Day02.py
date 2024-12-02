import aocd

puzzle = aocd.models.Puzzle(year=2016, day=2)
inp = puzzle.input_data.splitlines()
sample = """ULL
RRDDD
LURDL
UUUUD"""

nums = [[1,2,3],[4,5,6],[7,8,9]]
ind = [1, 1]
code = []

def traverse(nums, code, ind):
    for button in sample.splitlines():
        for instruction in button:
            if instruction == 'U':
                ind[0] -= 1 if ind[0] > 0 else 0
            elif instruction == 'D':
                ind[0] += 1 if ind[0] < 2 else 0
            elif instruction == 'L':
                ind[1] -= 1 if ind[1] > 0 else 0
            else:
                ind[1] += 1 if ind[1] < 2 else 0
        code.append(nums[ind[0]][ind[1]])
    return code

def traverse_2(nums, code, ind):
    for button in inp:
        for instruction in button:
            if instruction == 'U':
                ind[0] -= 1 if nums[ind[0]-1][ind[1]] != "" else 0
            elif instruction == 'D':
                ind[0] += 1 if nums[ind[0]+1][ind[1]] != "" else 0
            elif instruction == 'L':
                ind[1] -= 1 if nums[ind[0]][ind[1]-1] != "" else 0
            else:
                ind[1] += 1 if nums[ind[0]][ind[1]+1] != "" else 0
            print(ind)
        code.append(nums[ind[0]][ind[1]])
    return code

print(traverse(nums, code, ind))

nums = [["","","","","","",""],["","","","1","","",""], ["","", "2", "3", "4", "",""], ["","5", "6", "7", "8", "9",""], ["","", "A", "B", "C", "",""], ["","", "", "D", "", "",""],["","","","","","",""]]
ind = [3, 1]
code = []

print(traverse_2(nums, code, ind))