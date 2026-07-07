class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        unique = {}

        for number in nums:
            unique[number] = unique.get(number, 0) + 1

        for number in unique:
            if unique[number] > 1:
                return number

        