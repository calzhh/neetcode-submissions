class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0 
        
        new_string = ""
        for char in s:
            if char.isalnum():
                new_string += char.lower()
        j = len(new_string) - 1
        while i < j:
            if new_string[i] == new_string[j]:
                i +=1 
                j -=1
            else:
                return False
        return True