class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(i, j, visited, prev_height):
            if (
                i not in range(ROWS)
                or j not in range(COLS)
                or (i, j) in visited
                or heights[i][j] < prev_height
            ):
                return

            visited.add((i, j))
            dfs(i + 1, j, visited, heights[i][j])
            dfs(i - 1, j, visited, heights[i][j])
            dfs(i, j + 1, visited, heights[i][j])
            dfs(i, j - 1, visited, heights[i][j])

        for i in range(ROWS):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, COLS - 1, atl, heights[i][COLS - 1])

        for j in range(COLS):
            dfs(0, j, pac, heights[0][j])
            dfs(ROWS - 1, j, atl, heights[ROWS - 1][j])

        res = []
        for i, j in pac:
            if (i, j) in atl:
                res.append([i, j])

        return res
