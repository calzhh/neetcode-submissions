import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = [] 
        heapq.heapify(heap)
        for point in points:
            distance = ((point[0]) ** 2 + (point[1]) ** 2) ** 0.5
            heapq.heappush(heap, [distance, point])
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])

        return res