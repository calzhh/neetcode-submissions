class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(i, current, total):
            if total > target:
                return
            if total == target:
                res.append(current.copy())
                return
            if i == len(nums):
                return
            current.append(nums[i])
            backtrack(i, current, total + nums[i])
            current.pop()
            backtrack(i+1, current, total)

        res = []
        backtrack(0,[],0)

        return res        