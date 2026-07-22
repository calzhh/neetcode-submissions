class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return max(nums)

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n-1):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        pd = [0] * n
        pd[1] = nums[1]
        pd[2] = max(nums[1], nums[2])

        for i in range(3, n):
            pd[i] = max(pd[i-2] + nums[i], pd[i-1])

        return max(max(pd), max(dp))