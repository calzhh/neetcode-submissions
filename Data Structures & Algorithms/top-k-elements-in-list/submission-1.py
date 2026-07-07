class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for element in nums:
            freq[element] = freq.get(element, 0) + 1
        arr = []
        for item, count in freq.items():
            arr.append([count, item])
        arr.sort()
        res = []
        while k > 0:
            res.append(arr.pop()[1])
            k -= 1
        return res