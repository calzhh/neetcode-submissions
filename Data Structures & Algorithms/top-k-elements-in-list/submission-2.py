class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst = [0] * 2001  # btw should be 2001 if you want indexes 0..2000

        for element in nums:
            lst[element + 1000] += 1   # shift to handle negatives (-1000..1000)

        result = []
        for _ in range(k):
            # find max each time
            max_freq = max(lst)              # O(n)
            max_idx = lst.index(max_freq)    # O(n)
            result.append(max_idx - 1000)
            lst[max_idx] = -1                # mark as used
        return result
