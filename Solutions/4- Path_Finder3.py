from itertools import product
import heapq
def path_finder(maze):
    maze, start_vertex,n, MAX_INT = maze.split("\n"), (0,0), len(maze.split("\n")), 10**9
    cart, processed = list(product([x for x in range(n)],[x for x in range(n)])), set()
    get_weight, min_heap, marks = lambda i,j,x,y: abs(int(maze[i][j])-int(maze[x][y])), [(0,0,0)], {(x,y):0 for x,y in cart}
    adjacency_list, distances = {(i,j):[] for i,j in cart}, {(i, j): 0 if i == 0 and j == 0 else MAX_INT for i, j in cart}
    for i,j in marks:
        for x,y in (i,j-1),(i,j+1),(i-1,j),(i+1,j):
            if 0 <= x < n and 0 <= y < n: adjacency_list[(i,j)].append((get_weight(i,j,x,y),x,y))
    while len(processed) != n*n:
        _,i,j = heapq.heappop(min_heap)
        if (i,j) not in processed:
            for w2,x,y in adjacency_list[(i,j)]:
                if distances[(i,j)] + w2 < distances[(x,y)]: distances[(x,y)],_ = distances[(i,j)]+w2,heapq.heappush(min_heap,(distances[(i,j)]+w2,x,y))
            processed.add((i,j))
    return distances[(n-1,n-1)]