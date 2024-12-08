import aocd
from itertools import combinations

puzzle = aocd.models.Puzzle(year=2024, day=8)
inp = puzzle.input_data.splitlines()

grid = [list(i) for i in inp]

def parse_data(grid):
    locs = {}
    for y, row in enumerate(grid):
        for x, item in enumerate(row):
            if item != '.':
                locs.setdefault(item, []).append([x, y])
    return locs

def get_diffs(pair):
    x1, y1 = pair[0]
    x2, y2 = pair[1]
    return [[x1-x2, y1-y2], [x2-x1, y2-y1]]

def add_antinodes(pair, diffs, grid, visited):
    f_loc = [pair[0][0]+diffs[0][0], pair[0][1]+diffs[0][1]]
    s_loc = [pair[1][0]+diffs[1][0], pair[1][1]+diffs[1][1]]
    if 0 <= f_loc[0] < len(grid[0]) and 0 <= f_loc[1] < len(grid):
        visited.add(tuple(f_loc))
    if 0 <= s_loc[0] < len(grid[0]) and 0 <= s_loc[1] < len(grid):
        visited.add(tuple(s_loc))

def extend_path(start, diff, grid, visited):
    path = [start]
    while True:
        next_loc = [path[-1][0]+diff[0], path[-1][1]+diff[1]]
        if 0 <= next_loc[0] < len(grid[0]) and 0 <= next_loc[1] < len(grid):
            path.append(next_loc)
        else:
            break
    return path

if __name__ == '__main__':
    l_antinodes = set()
    antinodes = set()
    locs = parse_data(grid)

    for key, coords in locs.items():
        for pair in combinations(coords, r=2):
            f_diff, s_diff = get_diffs(pair)
            add_antinodes(pair, [f_diff, s_diff], grid, l_antinodes)

            fa_locs = extend_path(pair[0], f_diff, grid, antinodes)
            sa_locs = extend_path(pair[1], s_diff, grid, antinodes)
            antinodes.update(map(tuple, fa_locs+sa_locs))

    print(len(l_antinodes))
    print(len(antinodes))

