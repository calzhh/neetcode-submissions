class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        bigasscock = 0
        while i < j:
            if heights[i] >= heights[j]:
                area = heights[j] * (j - i)
                j -= 1
            elif heights[j] >= heights[i]:
                area = heights[i] * (j - i)
                i += 1
            if area > bigasscock:
                bigasscock = area
            print(area)
        return bigasscock