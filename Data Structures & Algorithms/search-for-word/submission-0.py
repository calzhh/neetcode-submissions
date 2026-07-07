class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        col_length = len(board[0])
        row_length = len(board)
        def backtrack(row, col, i):
            coords = (row,col)
            if i == len(word):
                return True
            if row >= row_length or row < 0 or col < 0 or col >= col_length or board[row][col] != word[i] or coords in visited:
                return False
            visited.add((row,col))
            res = (backtrack(row - 1, col, i + 1) or
                backtrack(row + 1, col, i + 1) or
                backtrack(row, col - 1, i + 1) or
                backtrack(row, col + 1, i + 1))
            visited.remove((row,col))
            return res
        for l in range(row_length):
            for k in range(col_length):
                if backtrack(l, k, 0): return True
        return False