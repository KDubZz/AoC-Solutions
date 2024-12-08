
import aocd

puzzle = aocd.models.Puzzle(year=2024, day=4)
inp = puzzle.input_data.splitlines()

surrounding_chars = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
diagonal_chars = [[0, 0], [-1,-1], [-1, 1], [1, -1], [1, 1]]

grid = [[i for i in line] for line in inp]

def find_word(loc, grid, direction):
    s = ''
    visit = []
    for i in range(4):
        new_x = loc[0] + direction[0]*i
        new_y = loc[1] + direction[1]*i
        if new_x in range(0, len(grid)) and new_y in range(0, len(grid)):
            s += grid[new_y][new_x]
            visit.append([new_x, new_y])
    if s == 'XMAS':
        return [s, visit]
    return False

def find_mas(loc, grid):
    s = ''
    visit = []
    for i in range(5):
        new_x = loc[0] + diagonal_chars[i][0]
        new_y = loc[1] + diagonal_chars[i][1]
        if new_x in range(0, len(grid[0])) and new_y in range(0, len(grid)):
            s += grid[new_y][new_x]
            visit.append([new_x, new_y])
    if s in ['AMSMS', 'ASSMM', 'ASMSM', 'AMMSS']:
        return [s, visit]
    return False

def process(grid):
    count = 0
    words = []
    mas_count = 0
    mas_words = []
    for y, row in enumerate(grid):
        for x, item in enumerate(row):
            loc = [x, y]
            mas_check = find_mas(loc, grid)
            if mas_check != False:
                mas_words += mas_check[1]
                mas_count += 1
            for direction in surrounding_chars:
                word_check = find_word(loc, grid, direction)
                if word_check != False:
                    words += word_check[1]
                    count += 1
    return count, mas_count

if __name__ == '__main__':
    count, mas_count = process(grid)
    print(count, mas_count)