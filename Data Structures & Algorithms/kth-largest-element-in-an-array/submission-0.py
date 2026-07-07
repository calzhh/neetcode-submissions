import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [x * -1 for x in nums]
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
            print(nums)

        return -heapq.heappop(nums)