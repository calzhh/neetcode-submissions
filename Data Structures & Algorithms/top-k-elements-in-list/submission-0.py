class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for element in nums:
            freq[element] = freq.get(element, 0) + 1
        
        while k > 0:
            maxi = max(freq, key=freq.get)
            res.append(maxi)
            freq[maxi] = 0
            k -= 1
        return res