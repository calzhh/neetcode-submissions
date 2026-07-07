# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root, lst):
            if not root:
                return
            
            lst.append(root.val)
            dfs(root.left,lst)
            dfs(root.right,lst)
            return lst
        order_this = dfs(root,[])
        order_this = sorted(order_this[::-1])
        

        return order_this[k-1]