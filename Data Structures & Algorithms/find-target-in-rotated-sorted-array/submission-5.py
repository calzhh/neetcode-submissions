class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            print(mid)
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if nums[mid] == target:
                return mid
            
            if nums[r] > nums[mid]:
                r = mid - 1
            elif nums[mid] > target and target < nums[r]:
                l = mid + 1
            elif target > nums[mid] and target > nums[r]:
                l = mid + 1 
            elif target < nums[mid] and target > nums[l]:
                r = mid - 1
            else:
                return -1
        return -1
