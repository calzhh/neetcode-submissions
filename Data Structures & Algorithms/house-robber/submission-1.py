class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return max(nums)

        dp = [0] * (n+1)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])

        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i],
                        dp[i-1])
            print(f"chose {dp[i]}")
        
        print(nums)
        print(dp)
        return dp[n-1]
            # [2,9,8,3,6]
            # 2 8 = 10
            