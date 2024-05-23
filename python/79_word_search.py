class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(x, y, i):
            if i >= len(word):
                return True

            if (
                x < 0
                or y < 0
                or x >= ROWS
                or y >= COLS
                or (x, y) in visited
                or board[x][y] != word[i]
            ):
                return False
            
            visited.add((x, y))

            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
              if dfs(nx, ny, i + 1):
                return True

            visited.remove((x, y))


        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True

        return False
