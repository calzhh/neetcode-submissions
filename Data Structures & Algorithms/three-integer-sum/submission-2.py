class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        hashmap = {}

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                twoSum = nums[i] + nums[j]
                hashmap[(nums[i], nums[j], i, j)] = twoSum
        for k in range(len(nums)):
            for indexes, key in enumerate(hashmap):
                if nums[k] + hashmap[key] == 0:
                    if k not in key[2:]:

                        keys = list(key)
                        keys = keys[:2]
                        keys.append(nums[k])
                        if sorted(keys) not in res:
                            print(k,keys)
                            res.append(sorted(keys))
        return res