class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(0,len(nums)):
            if nums.index(nums[i]) != i:
                return nums[i]
            

        