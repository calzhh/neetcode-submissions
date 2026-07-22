class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = 0 
        for i in range(n):
            dp[i][i] = True

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                dp[i][j] = s[i] == s[j] and (abs(j-i) < 3 or dp[i+1][j-1])
                if dp[i][j]:
                    res += 1

        return res