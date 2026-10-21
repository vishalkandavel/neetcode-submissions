from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:
            i, j = q.popleft()

            for r, c in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if (0 <= r < len(grid) and
                    0 <= c < len(grid[0]) and
                    grid[r][c] == 2147483647):

                    grid[r][c] = grid[i][j] + 1
                    q.append((r, c))