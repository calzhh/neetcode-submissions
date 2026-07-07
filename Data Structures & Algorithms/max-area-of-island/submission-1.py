class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if rows <= r or cols <= c or c < 0 or r < 0 or grid[r][c] != 1:
                return 0
            else:
                grid[r][c] = 2
                area = 1
                area += dfs(r + 1, c)
                area += dfs(r - 1, c)
                area += dfs(r, c + 1)
                area += dfs(r, c - 1)
                return area
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))

        return max_area