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
        if not node:
            return None
        
        start = node
        old_to_new = {}
        stack = [node]
        visited = set()
        visited.add(start)
        while stack:
            node = stack.pop()
            old_to_new[node] = Node(node.val)

            for neighbor in node.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor)

        for old_node, new_node in old_to_new.items():
            on = old_node.neighbors 
            for neighbor in on:
                new_node.neighbors.append(old_to_new[neighbor])
            
        return old_to_new[start]