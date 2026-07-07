from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        q = deque()
        visited = set()
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O" and (i == 0 or j == 0 or i == ROWS - 1 or j == COLS - 1):
                    q.append((i, j))
                    visited.add((i, j))
        print(q)
        while q:
            i, j = q.popleft()
            for r_off, c_off in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r = i + r_off
                c = j + c_off

                if r < 0 or c < 0 or ROWS <= r or COLS <= c:
                    continue
                if board[r][c] == "O" and (r, c) not in visited:
                    q.append((r, c))
                    visited.add((r, c))

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"