from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        res = []
        temp_k = 0
        temp_c = sorted(c.keys(), key=lambda x: c[x], reverse=True)
        return temp_c[:k]
