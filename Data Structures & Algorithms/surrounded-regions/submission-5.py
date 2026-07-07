from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        visited = set()
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i == 0 or i == rows - 1 or j == 0 or j == cols - 1):
                    q.append((i, j))
                    visited.add((i, j))


        while q:
            i, j = q.popleft()
            
            for r_off, c_off in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                r = i + r_off
                c = j + c_off

                if r < 0 or c < 0 or rows <= r or cols <= c:
                    continue

                if board[r][c] == "O" and (r, c) not in visited:
                    visited.add((r, c))
                    q.append((r, c))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"
        