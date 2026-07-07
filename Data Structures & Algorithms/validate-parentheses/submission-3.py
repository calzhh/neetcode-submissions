class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")": "(", "]": "[", "}": "{"}
        stack = []

        for parentheses in s:
            if parentheses in ")]}" and stack and hashmap[parentheses] == stack[-1]:
                stack.pop()
            else:
                stack.append(parentheses)
        return stack == []