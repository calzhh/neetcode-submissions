from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses
        graph = defaultdict(list)
        order = []
        for lst in prerequisites:
            course = lst[0]
            pre = lst[1]

            graph[course].append(pre)

        def dfs(node):
            state = states[node]
            if state == VISITING: return False
            elif state == VISITED: return True
            states[node] = VISITING

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            states[node] = VISITED
            order.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return order

        