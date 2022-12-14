import aoc_utils
import string
from collections import deque

alphabet = list(string.ascii_lowercase)
graph = aoc_utils.input_string_list()
checker_graph = [[0 for _ in range(len(graph[0]))] for _ in range(len(graph[0]))]
for x,xx in enumerate(graph):
    for y,yy in enumerate(xx):
        if yy=='S':
            checker_graph[x][y] = 1
        elif yy == 'E':
            checker_graph[x][y] = 26
        else:
            index = alphabet.index(yy)
            checker_graph[x][y] = index+1

queue = deque()
for xindex,x in enumerate(graph):
    for yindex,y in enumerate(graph[0]):
        if (checker_graph[xindex][yindex] == 1):
            queue.append(((xindex,yindex), 0))


def loop():
    path = set()
    while queue:
        (x,y),d = queue.popleft()
        if (x,y) in path:
            continue
        path.add((x,y))
        if graph[x][y]=='E':
            return d
        offset = [(-1,0),(0,1),(1,0),(0,-1)]
        for dx,dy in offset:
            xx = x+dx
            yy = y+dy
            if 0<=xx<len(graph) and 0<=yy<len(graph[0]) and checker_graph[xx][yy]<=1+checker_graph[x][y]:
                queue.append(((xx,yy),d+1))

if __name__ == '__main__':
    print('Part 1: 520') #lost part 1 code cba to find it
    print('Part 2:', loop())