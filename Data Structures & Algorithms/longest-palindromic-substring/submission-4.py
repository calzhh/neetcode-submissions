class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
            
        longest = ""
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True

        for i in range(len(s) -1, -1, -1):
            for j in range(i, len(s)):
                dp[i][j] = (s[i] == s[j]) and (abs(i-j) < 3 or dp[i+1][j-1])   

                if dp[i][j]:
                    current_length = j - i + 1     
                    if current_length > len(longest):
                        longest = s[i:j+1]
        return longest