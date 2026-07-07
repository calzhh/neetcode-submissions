from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        INF = 2 ** 31 - 1
        visited = set()
        q = deque()
        directions = [(1,0), (-1, 0), (0,-1), (0, 1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        chests = len(visited)
        print(len(visited))
        length = 0
        iterations = 0
        while q:      
            for i in range(len(q)):
                row, col = q.popleft()
                if grid[row][col] == INF:
                    grid[row][col] = length
                for dire in directions:
                    #cord = tuple(map(sum, zip(dire, (r,c))))
                    cord = (dire[0] + row, dire[1] + col)
                    if rows <= cord[0] or cols <= cord[1] or cord[1] < 0 or cord[0] < 0 or grid[cord[0]][cord[1]] == -1:
                        continue
                    if cord not in visited:
                        q.append(cord)
                        visited.add(cord)
            length += 1
                    
        
            