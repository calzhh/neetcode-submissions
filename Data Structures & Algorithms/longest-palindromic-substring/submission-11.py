class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s) 
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        longest=""
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 3 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if dp[i][j]:
                        if len(s[i:j+1]) > len(longest):
                            longest = s[i:j+1]

        return longest