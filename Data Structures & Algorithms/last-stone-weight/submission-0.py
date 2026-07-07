import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [weight * -1 for weight in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            if x == y:
                continue
            else:
                heapq.heappush(stones,-abs(x - y))
        if len(stones) == 1:
            return -1 * stones[0]
        else:
            return 0