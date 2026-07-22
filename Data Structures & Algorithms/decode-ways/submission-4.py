class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        def is_valid(char):        
            return 1 <= int(char) <= 9 and s[0] != '0'
        def is_valid_sec(char):        
            return 10 <= int(char) <= 26 and s[0] != '0'

        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 1 if is_valid(s[0]) else 0

        for i in range(2, len(s)+1):
            helper = 0 
            if is_valid(s[i-1]):
                helper += dp[i-1]
            if is_valid_sec(s[i-2:i]):
                helper += dp[i-2]

            dp[i] += helper
        return dp[len(s)]