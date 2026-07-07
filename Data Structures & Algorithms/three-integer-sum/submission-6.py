class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashmap = {}

        nums = sorted(nums)
        res = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            left, right = i+1, len(nums) - 1

            while left < right:
                total = nums[left] + nums[right] + a

                if total == 0:
                    res.append([nums[left], nums[right], a])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
        return res