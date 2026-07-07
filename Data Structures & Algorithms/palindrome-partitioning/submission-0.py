class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def backtrack(i):
            if i >= len(s):
                res.append(current.copy())
                return
            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    current.append(s[i:j+1])
                    backtrack(j+1)
                    current.pop()
        def isPalindrome(s) -> bool:
            string = ""
            for word in s.lower():
                if word.isalnum():
                    string += word
            return string == string[::-1]
        res, current = [], []
        backtrack(0)
        return res