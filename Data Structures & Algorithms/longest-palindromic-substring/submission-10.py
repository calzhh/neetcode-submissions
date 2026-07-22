class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)  
        longest = ""

        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for i in range(len(s) -1, -1, -1):
            for j in range(i, len(s)):
                dp[i][j] = s[i] == s[j] and (abs(i-j) < 3 or dp[i+1][j-1])

                if dp[i][j]:
                    if j - i + 1 > len(longest):
                        longest = s[i:j+1]


        return longest