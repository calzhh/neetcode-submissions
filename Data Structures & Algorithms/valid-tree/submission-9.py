from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(start):
            q = deque()
            q.append((start, -1)) # [2, 3, 4]
            visited = set() # [0, 1, ]
            visited.add(0)
            while q:
                node, parent = q.popleft()
                for nei in graph[node]:
                    if nei == parent:
                        continue
                    if nei in visited:
                        return False
                    visited.add(nei)
                    q.append((nei, node))
            return len(visited) == n

        return bfs(0)