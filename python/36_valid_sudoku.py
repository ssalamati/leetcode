class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue

                if board[i][j] in rows[i]:
                    return False
                else:
                    rows[i].add(board[i][j])

                if board[i][j] in cols[j]:
                    return False
                else:
                    cols[j].add(board[i][j])

                if board[i][j] in boxes[i // 3][j // 3]:
                    return False
                else:
                    boxes[i // 3][j // 3].add(board[i][j])

        return True
