from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2 ** 31 - 1
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))
        length = 0 
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if grid[r][c] == INF:
                    grid[r][c] = length
                for dire in directions:
                    new_r = r + dire[0]
                    new_c = c + dire[1]
                    if rows <= new_r or cols <= new_c or new_r < 0 or new_c < 0 or grid[new_r][new_c] == -1:
                        continue
                    if (new_r,new_c) not in visited:
                        queue.append((new_r,new_c))
                        visited.add((new_r,new_c))

            length += 1

                    