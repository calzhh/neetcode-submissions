class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        helperlist = [nums[i], nums[j], nums[k]]
                        mini = min(helperlist)
                        helperlist.remove(mini)
                        maxi = max(helperlist)
                        helperlist.remove(maxi)
                        res.add((mini,helperlist[0],maxi))

        return list(res)