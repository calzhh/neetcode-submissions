class Solution:

    def encode(self, strs: List[str]) -> str:
        full_word = ""
        for word in strs:
            full_word += word + "#gdsnjfdnjsfdhnjsdfhjnkkbnnsgfbg"
        return full_word

    def decode(self, s: str) -> List[str]:
        new_list = s.split("#gdsnjfdnjsfdhnjsdfhjnkkbnnsgfbg")
        new_list.pop()
        return new_list