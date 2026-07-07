class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxi = 1
        if len(nums) == 0:
            return 0
        print(numSet)

        for num in nums:
            if (num - 1) not in nums:
                k = 1
                while (num + 1) in nums:
                    num += 1
                    k += 1
                maxi = max(maxi, k)
        
        return maxi