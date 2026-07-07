class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        coc = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in coc:
                return [coc[diff], i]
            coc[n] = i