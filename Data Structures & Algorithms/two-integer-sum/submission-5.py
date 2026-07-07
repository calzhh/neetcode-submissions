from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)

        for idx, element in enumerate(nums):
            if target - element in hashmap:
                return [hashmap[target - element], idx]
            else:
                hashmap[element] = idx
