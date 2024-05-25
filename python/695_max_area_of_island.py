class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(i, j):
            if min(i, j) < 0 or i >= ROWS or j >= COLS or grid[i][j] == 0:
                return 0

            count = 1

            grid[i][j] = 0

            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                count += dfs(x, y)

            return count

        res = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))

        return res
