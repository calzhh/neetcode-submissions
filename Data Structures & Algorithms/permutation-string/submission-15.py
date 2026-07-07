class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        matches = 0 

        if len(s1) > len(s2): return False
        s1_count = 26 * [0]
        s2_count = 26 * [0]

        for i in range(len(s1)):
            s1_count[ord(s1[i])-97] += 1
            s2_count[ord(s2[i])-97] += 1
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1

        L = 0

        for R in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = ord(s2[R]) - 97
            s2_count[index] += 1

            if s2_count[index] == s1_count[index]:
                matches += 1
            elif s2_count[index] == s1_count[index] + 1:
                matches -= 1

            index = ord(s2[L]) - 97
            s2_count[index] -= 1
            if s2_count[index] == s1_count[index]:
                matches += 1
            elif s2_count[index] == s1_count[index] - 1:
                matches -= 1
            L += 1
        return matches == 26
