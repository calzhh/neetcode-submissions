class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxi = 0

        while r < len(prices):
            print(prices[r] - prices[l])
            if prices[l] > prices[r]:
                l += 1
                continue
            if prices[r] - prices[l] > maxi:
                maxi = prices[r] - prices[l]
            r += 1
        return maxi