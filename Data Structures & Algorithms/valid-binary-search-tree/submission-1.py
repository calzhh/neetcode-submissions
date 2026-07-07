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
            if not dfs(root.left, leftMin, root.val):
                return False
            if not dfs(root.right, root.val, rightMin):
                return False
            if leftMin < root.val < rightMin:
                return True
            else:
                print("FUCK")
                return False
                

        return dfs(root, -1001, 1001)


        