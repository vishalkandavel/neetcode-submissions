class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(grid, i, j):
            grid[i][j] = 0
            area = 1 
            
            if i > 0 and grid[i-1][j] == 1:
                area = area + dfs(grid, i-1, j)
            if j > 0 and grid[i][j-1] == 1:
                area = area + dfs(grid, i, j-1)
            if i+1 < len(grid) and grid[i+1][j] == 1:
                area = area + dfs (grid, i+1, j)
            if j+1 < len(grid[0]) and grid[i][j+1] == 1:
                area = area + dfs (grid, i, j+1)
            
            return area 
            
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                  area = dfs(grid,i,j)
                  max_area = max(area,max_area)
        
        return max_area

    
        
  
                