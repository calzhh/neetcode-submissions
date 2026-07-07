from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict()
        res = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for i in range(k):
            maxi = max(freq, key=freq.get)
            res.append(maxi)
            freq[maxi] = 0

        return res