from collections import deque
# Given an m x n binary matrix grid where 1s represent humans and 0s represent zombies, return the distance of the nearest zombie to each square in the grid.

# The distance between two adjacent cells horizontally/vertically is 1.


# Example Usage:

# grid_1 = [
#     [0,0,0],
#     [0,1,0],
#     [0,0,0]
#     ]

# grid_2 = [
#     [0,0,0],
#     [0,1,0],
#     [1,1,1]
#     ]

# print(nearest_zombie(grid_1))
# print(nearest_zombie(grid_2))
# Example Output:

# [
#     [0,0,0],
#     [0,1,0],
#     [0,0,0]
#     ]

# [
#     [0,0,0],
#     [0,1,0],
#     [1,2,1]
#     ]

#Understand:
#input: matrix (set of rows)
#output: matrix (set of rows)

#Match:
#DFS or BFS

def nearest_zombie(grid):
    distances = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]

    queue = deque()
    visited = []

    while queue:
        row, column = queue.popleft()
        for r, c in (row, column+1), (row, column-1), (row+1, column), (row-1, column):
            if (r, c) not in visited:
                queue.append(r, c)
                visited.add(r, c)

        for r, c in (row, column+1), (row, column-1), (row+1, column), (row-1, column):

    
    return distances

