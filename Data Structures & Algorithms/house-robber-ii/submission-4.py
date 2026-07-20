class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        length = len(nums)
        for i in range(2, length-1):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        pd = [0] * len(nums)
        pd[1] = nums[1]
        pd[2] = max(nums[1], nums[2])

        for i in range(3, length):
            pd[i] = max(pd[i-2] + nums[i], pd[i-1])
        print(dp, pd)
        return max(max(pd), max(dp))