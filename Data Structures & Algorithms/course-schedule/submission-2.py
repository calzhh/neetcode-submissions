from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        graph = defaultdict(list)

        for lst in prerequisites:
            course = lst[0]
            pre = lst[1]
            graph[course].append(pre)

        states = [UNVISITED] * numCourses
        
        def dfs(node):
            state = states[node]
            if state == VISITED: return True
            if state == VISITING: return False

            states[node] = VISITING
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            states[node] = VISITED
            return True 

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True