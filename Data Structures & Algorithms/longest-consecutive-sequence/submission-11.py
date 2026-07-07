class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxi = 1
        if len(nums) == 0:
            return 0

        for num in numSet:
            if (num - 1) not in numSet:
                k = 1
                while (num + 1) in numSet:
                    num += 1
                    k += 1
                maxi = max(maxi, k)
        
        return maxi
