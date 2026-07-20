class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        longest = ""
        for i in range(len(s)):
            dp[i][i] = True

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                dp[i][j] = s[i] == s[j] and (abs(i - j) < 3 or dp[i+1][j-1])
                if dp[i][j]:
                    num = j - i + 1
                    if num > len(longest):
                        longest = s[i:j+1]
        return longest