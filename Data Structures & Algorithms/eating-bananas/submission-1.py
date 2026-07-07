import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Max k = Max Banana in Pile 
        # Min k = 1 

        low = 1 
        high = max(piles)
        diddy_list = []
        assholelicker = 0

        while low <= high:
            hours_total = 0
            mid = (low + high) // 2

            for bananas in piles:
                hours = math.ceil(bananas / mid)                 
                hours_total += hours
            
            if hours_total <= h:
                diddy_list.append(mid)


            if hours_total > h:
                low = mid + 1
            elif hours_total <= h:
                high = mid - 1
            
        return min(diddy_list)