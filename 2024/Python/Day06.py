import aocd

puzzle = aocd.models.Puzzle(year=2024, day=6)
inp = puzzle.input_data.splitlines()

grid = [list(row) for row in inp]

def check_next(loc, direction, grid):
    new_loc = [loc[0]+direction[0], loc[1]+direction[1], direction]
    if 0 <= new_loc[0] < len(grid[0]) and 0 <= new_loc[1] < len(grid):
        grid_value = grid[new_loc[1]][new_loc[0]]
        if grid_value in ['#', 'O']:
            return False
        else:
            return new_loc
    else:
        return "EXIT"

def process(grid):
    directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    count = 0
    loc = [60, 70, directions[count]]
    guard_exit = False
    inf_loop = False
    visited = set()
    d_visit = []
    while guard_exit == False:
        direction = directions[count]
        next_pos = check_next(loc, direction, grid)
        if next_pos == "EXIT":
            guard_exit = True
        elif next_pos == False:
            count = (count+1) % 4
        else:
            loc = next_pos
            visited.add(tuple(next_pos[:2]))
            if next_pos in d_visit:
                inf_loop = True
                break
            else:
                d_visit.append(next_pos)
    if inf_loop == True:
        return d_visit
    else:
        return visited

if __name__ == '__main__':
    visited = process(grid)
    print(len(visited))
    count = 0
    for i, position in enumerate(visited):
        pos = list(position)
        new_grid = [x[:] for x in grid]
        new_grid[pos[1]][pos[0]] = 'O'
        d_visit = process(new_grid)
        if type(d_visit) is list:
            count += 1
    print(count)
