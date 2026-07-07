# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        list1 = []
        list2 = []
        def normalSearch(root):
            nonlocal list1
            if not root:
                list1.append("FUCKU")
                return 0
            list1.append(root.val)
            normalSearch(root.left)
            normalSearch(root.right)
        def normalSearch2(root):
            nonlocal list2
            if not root:
                list2.append("FUCKU")
                return 0
            list2.append(root.val)
            normalSearch2(root.left)
            normalSearch2(root.right)
        normalSearch(p)
        normalSearch2(q)
        print(list1, list2)
        return list1 == list2