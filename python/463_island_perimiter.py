class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        perimiter = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    continue
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if (
                        x not in range(ROWS)
                        or y not in range(COLS)
                        or grid[x][y] == 0
                    ):
                        perimiter += 1

        return perimiter
