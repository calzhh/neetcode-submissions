from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_que = deque()
        p_seen = set()

        a_que = deque()
        a_seen = set()

        rows = len(heights)
        cols = len(heights[0])

        directions = [(1,0), (-1,0), (0, 1), (0, -1)]

        for i in range(cols):
            p_que.append((0, i))
            p_seen.add((0, i))
        for i in range(1, rows):
            p_que.append((i, 0))
            p_seen.add((0, i))

        for i in range(rows):
            a_que.append((i, cols-1))
            a_seen.add((i, cols-1))
        for i in range(cols - 1):
            a_que.append((rows - 1, i))
            a_seen.add((rows - 1, i))

        def get_coords(que, seen):
            coords = set()
            while que:
                i, j = que.popleft()
                coords.add((i, j))
                for dire in directions:
                    r, c = i + dire[0], j + dire[1]
                    if 0 <= r < rows and 0 <= c < cols and heights[r][c] >= heights[i][j] and (r, c) not in seen:
                        que.append((r,c))
                        seen.add((r, c))
            return coords
        p_coords = get_coords(p_que, p_seen)
        a_coords = get_coords(a_que, a_seen)

        return list(p_coords.intersection(a_coords))