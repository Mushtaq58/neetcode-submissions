class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols: # out of bound
                return

            if grid[row][col] == "0":
                return

            grid[row][col] = "0"

            dfs(row - 1, col) # Checking top neighbor
            dfs(row + 1, col) # Checking below neighbor
            dfs(row, col - 1) # Checking left neighbor
            dfs(row, col + 1) # Checking right neighbor

        islands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)

        return islands




# BFS Solution
"""
from collections import deque

class Solution(object):
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        def bfs(row, col):
            queue = deque() # deque = Double-Ended Queue
            queue.append((row, col))
            grid[row][col] = "0"

            while queue:
                row, col = queue.popleft()

                neighbors = [
                    (row - 1, col),  # top
                    (row + 1, col),  # bottom
                    (row, col - 1),  # left
                    (row, col + 1)   # right
                ]

                for r, c in neighbors:
                    # Check boundaries
                    if r < 0 or r >= rows or c < 0 or c >= cols:
                        continue

                    # If unvisited land
                    if grid[r][c] == "1":
                        grid[r][c] = "0"
                        queue.append((r, c))

        islands = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    bfs(row, col)

        return islands
"""