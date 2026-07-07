class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        openN = 0
        closeN = 0
        res = []
        def backtrack(openN, closeN, current):
            print(current)
            if len("".join(current)) == n * 2:
                res.append("".join(current))


            if openN < n:
                current.append("(")
                backtrack(openN+1, closeN, current)
                current.pop()

            if closeN < openN:
                current.append(")")
                backtrack(openN, closeN+1, current)
                current.pop()

        backtrack(0,0,[])
        return res