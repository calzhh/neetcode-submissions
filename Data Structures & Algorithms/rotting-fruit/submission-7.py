from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        rows = len(grid)
        cols = len(grid[0])

        minutes = 0
        contains_one = False
        contains_two = False
        two_next_to_one = False
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for row in range(rows):
            for col in range(cols):
                print(row, col)
                fruit = grid[row][col]
                if fruit == 1:
                    contains_one = True
                if fruit == 2:
                    contains_two = True
                    q.append((row, col))
        if not q and not contains_one:
            return 0
        if not contains_two:
            return -1
        if not contains_one:
            return 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dire in directions:
                    nr = r + dire[0]
                    nc = c + dire[1]
                    if rows <= nr or cols <= nc or nr < 0 or nc < 0 or grid[nr][nc] != 1:
                        continue
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                print(grid, minutes)
            minutes += 1

        for row in range(rows):
            for col in range(cols):
                fruit = grid[row][col]
                if fruit == 1:
                    return - 1


        return minutes - 1