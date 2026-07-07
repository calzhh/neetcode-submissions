class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }
        res = []
        comb = []
        helper = []
        def backtrack(comb, i):
            if len(digits) == len(comb) and digits != "":
                res.append(''.join(comb))
                return
            if i < len(digits):
                # 0
                # 1
                for j in hashmap[int(digits[i])]:
                    # d 0 
                    # e 0
                    # f 0
                    # g 1 
                    # h 1
                    # i 1
                    comb.append(j)
                    backtrack(comb, i + 1)
                    comb.pop()


        backtrack([], 0)
        return res