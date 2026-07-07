class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        unique = set()

        for number in nums:
            if number in unique:
                return number
            else:
                unique.add(number)