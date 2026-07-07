from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        graph = defaultdict(list)
        order = []
        states = [UNVISITED] * numCourses

        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(node):
            state = states[node]
            if state == VISITING: return False
            if state == VISITED: return True

            states[node] = VISITING
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            states[node] = VISITED
            order.append(node)
            return True
        for node in range(numCourses):
            if not dfs(node):
                return []

        return order