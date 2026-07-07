"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return node
        old_to_new = defaultdict()
        stack = [node]
        visited = set()
        while stack:
            curr = stack.pop()
            old_to_new[curr] = Node(curr.val)
            visited.add(curr)
            for new_node in curr.neighbors:
                if new_node not in visited:
                    stack.append(new_node)
        
        for old, new in old_to_new.items():
            for nei in old.neighbors:
                new.neighbors.append(old_to_new[nei])
        
        return old_to_new[node]