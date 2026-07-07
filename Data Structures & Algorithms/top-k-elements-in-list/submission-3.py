class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bsArr = [[] for element in range(len(nums)+1)]
        count = {}
        res = []
        print(bsArr)

        for element in nums:
            count[element] = count.get(element, 0) + 1

        for num, freq in count.items():
            bsArr[freq].append(num)
        print(bsArr)
        for lst in bsArr[::-1]:
            if k == 0:
                break
            while lst != []:
                res.append(lst.pop())
                k -= 1
        return res