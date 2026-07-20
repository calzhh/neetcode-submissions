class Solution:
    def countSubstrings(self, s: str) -> int:
        res = len(s)
        goat = 0
        dp = [[False] * res for _ in range(res)]
        for i in range(len(s)):
            dp[i][i] = True

        for i in range(len(s) -1 , -1, -1):
            for j in range(i, len(s)):
                dp[i][j] = s[i] == s[j] and (abs(i-j) < 3 or dp[i+1][j-1])
                if dp[i][j]:
                    goat += 1
        return goat