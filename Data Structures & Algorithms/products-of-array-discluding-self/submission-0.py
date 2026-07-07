class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            total = 1
            for j in range(len(nums)):
                if j == i:
                    pass
                else:
                    total *= nums[j]
            res.append(total)
        return res