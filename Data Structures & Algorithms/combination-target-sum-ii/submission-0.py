class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(i, current, total):
            if total == target:
                res.append(current.copy())
                return
            if total > target:
                return
            if i == len(candidates):
                return 
            current.append(candidates[i])
            backtrack(i+1, current, total + candidates[i])
            current.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, current, total)


        backtrack(0,[],0)
        return res