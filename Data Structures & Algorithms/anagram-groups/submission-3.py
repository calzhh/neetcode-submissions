from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for string in strs:
            s = "".join(sorted(string))
            hashmap[s].append(string)   
        res = []
        print(hashmap)
        for element in hashmap:
            res.append(hashmap[element])
        return res