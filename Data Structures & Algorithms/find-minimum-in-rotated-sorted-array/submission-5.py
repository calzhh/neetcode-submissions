class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        res = nums[0]
        while L <= R:
            mid = (L + R) // 2
            if nums[L] <= res:
                res = min(nums[L], res)
            if nums[mid] <= res:
                res = min(nums[mid], res)

            if nums[mid] >= nums[L]:
                L = mid + 1
            else:
                R = mid - 1
        return res