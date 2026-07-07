import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        diddy_list = []


        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hour = math.ceil(pile/mid)
                hours += hour

            if hours > h:
                left = mid + 1
            elif hours <= h:
                diddy_list.append(mid)
                right = mid - 1
        return min(diddy_list)