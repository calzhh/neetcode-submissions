class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])

        f_dp = [0] * (n-1)
        f_dp[0] = nums[0]
        f_dp[1] = max(nums[0], nums[1])

        for i in range(2, n-1):
            f_dp[i] = max(f_dp[i-2] + nums[i],
                            f_dp[i-1])

        s_dp = [0] * n
        s_dp[1] = nums[1]
        s_dp[2] = max(nums[1], nums[2])

        for i in range(3, n):
            s_dp[i] = max(s_dp[i-2] + nums[i],
                            s_dp[i-1])

        maxi = max(f_dp)
        maxii = max(s_dp)
        return max(maxi,maxii)