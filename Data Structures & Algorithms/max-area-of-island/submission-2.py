from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def bfsMaxArea(i, j):
            queue = deque()
            queue.append((i, j))
            grid[i][j] = 0

            area = 1
            while queue:
                row, col = queue.popleft()

                neighbors = [
                (row+1, col),
                (row-1, col),
                (row, col+1),
                (row, col-1)
                ]

                for r, c in neighbors:
                    if r < 0 or r >= rows or c < 0 or c >= cols:
                        continue

                    if grid[r][c] == 1:
                        grid[r][c] = 0
                        queue.append((r,c))
                        area += 1

            return area

        maxArea = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = bfsMaxArea(i, j)
                    maxArea = max(maxArea, area)

        return maxArea




"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != 1:
                return 0

            grid[i][j] = 0

            return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i, j + 1)

        max_area = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

        return max_area

"""