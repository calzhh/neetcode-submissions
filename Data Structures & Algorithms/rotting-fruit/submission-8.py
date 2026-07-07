from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        numFresh = 0
        minutes = 0
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    numFresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        if numFresh == 0:
            return minutes
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dire in directions:
                    nr = dire[0] + r
                    nc = dire[1] + c
                    if rows <= nr or cols <= nc or nr < 0 or nc < 0 or grid[nr][nc] != 1:
                        continue
                    elif grid[nr][nc] == 1:
                        numFresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr,nc))
            minutes += 1
        
        if numFresh > 0:
            return -1
        return minutes - 1