class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, current):
            current = sorted(current)
            if current not in res:
                res.append(current.copy())
            if i == len(nums):
                return
            current.append(nums[i])
            backtrack(i+1, current)
            current.pop()
            backtrack(i+1, current)
        res = []
        backtrack(0, [])
        return res