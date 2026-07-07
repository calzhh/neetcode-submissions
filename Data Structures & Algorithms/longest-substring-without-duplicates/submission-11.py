class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,0
        seen_before = []
        length_of_sub_strings = []

        while r < len(s):
            if s[r] == s[l] and l != r:
                l += 1
            elif s[r] in seen_before:
                length_of_sub_strings.append(len(seen_before))
                seen_before.clear()
                seen_before.append(s[r])
                l = r
                r += 1
                continue
            else:
                seen_before.append(s[r])
            r += 1
        length_of_sub_strings.append(len(seen_before))
        return max(length_of_sub_strings) if len(length_of_sub_strings) > 0 else "ane"