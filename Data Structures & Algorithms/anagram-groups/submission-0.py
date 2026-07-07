class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}

        for i, word in enumerate(strs):
            lst = []
            for letter in word:
                lst.append(letter)
            new_list = sorted(lst)
            my_tuple = tuple(new_list)
            
            if my_tuple in hashmap:
                hashmap[my_tuple].append(i)
            else:
                hashmap[my_tuple] = [i]
                
        print(hashmap)
        final_list = []
        for key in hashmap:
            helper_list = []
            value_list = hashmap[key]
            for element in value_list:
                helper_list.append(strs[element])
            final_list.append(helper_list)

        return final_list