class Solution:
    def isValid(self, s: str) -> bool:
        matchOC = {")":"(", "}":"{", "]":"["}
        stack = []
        for par in s:
            if par in matchOC and stack != []:
                if stack[len(stack) - 1] == matchOC[par]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(par)

        return stack == []
                