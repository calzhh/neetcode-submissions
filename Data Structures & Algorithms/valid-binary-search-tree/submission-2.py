# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, leftMin, rightMin):
            if not root:
                return True
            if not leftMin < root.val < rightMin:
                return False
            
            return dfs(root.left, leftMin, root.val) and dfs(root.right, root.val, rightMin)
                

        return dfs(root, -1001, 1001)


        