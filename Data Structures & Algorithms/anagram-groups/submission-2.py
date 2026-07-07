class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}
        lst = []
        res = []
        for i, word in enumerate(strs):
            for letter in word:
                lst.append(letter)
            lst.sort()
            tt = tuple(lst)

            if tt in hashmap:
                hashmap[tt].append(word)
            else:
                hashmap[tt] = [word]
            lst = []
            
        for key, value in hashmap.items():
            res.append(value)
        return res