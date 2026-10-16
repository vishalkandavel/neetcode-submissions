class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(grid, i, j):
            grid[i][j] = "0"
            if i>0 and grid[i-1][j] == "1":
                dfs(grid, i-1, j)
            if i+1 < len(grid) and grid[i+1][j] == "1":
                dfs(grid, i+1, j)
            if j>0 and grid[i][j-1] == "1":
                dfs(grid, i, j-1)
            if j+1 < len(grid[0]) and grid[i][j+1] == "1":
                dfs(grid, i, j+1)

        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num = num + 1
                    dfs(grid, i, j)
        return num