class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        
        n = len(s)

        dp = [0] * (n+1)

        def is_valid_one(char):
            return 1 <= int(char) <= 9 and int(char) != 0
        def is_valid_two(char):
            return 10 <= int(char) <= 26 and int(char[0]) != 0

        dp[0] = 1
        dp[1] = 1 if is_valid_one(s[0]) else 0

        for i in range(2, n+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if is_valid_two(s[i-2:i]):
                dp[i] += dp[i-2]
        return dp[n]