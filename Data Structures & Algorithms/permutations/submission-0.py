class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i, current, boolean):
            if len(current) == len(nums):
                print('why not stopping')
                res.append(current[:])
                return 1
            for idx, boolean in enumerate(helper):
                if not boolean:
                    current.append(nums[idx])
                    helper[idx] = True
                    backtrack(i+1, current, helper)
                    current.pop()
                    helper[idx] = False
        helper = [False for i in range(len(nums))]
        res = []
        backtrack(0, [], helper)
        return res