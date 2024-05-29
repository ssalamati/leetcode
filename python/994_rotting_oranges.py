class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        queue = collections.deque()
        fresh = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        time = 0
        while fresh > 0 and queue:
            length = len(queue)
            for _ in range(length):
                i, j = queue.popleft()

                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if x in range(ROWS) and y in range(COLS) and grid[x][y] == 1:
                        fresh -= 1
                        grid[x][y] = 2
                        queue.append((x, y))

            time += 1

        return time if fresh == 0 else -1
