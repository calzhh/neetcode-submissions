class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()

        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for nei in graph[node]:
                dfs(nei)
            return True   
                    
        res = 0
        for i in range(n):
            if dfs(i):
                res += 1

        return res