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