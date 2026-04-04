class Solution:

    def encode(self, strs: List[str]) -> str:
        my_strs = ""
        for string in strs:
            my_strs = my_strs + str(len(string)) + '#' + string
        return my_strs

    def decode(self, s: str) -> List[str]:
        i = 0
        my_list = []
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            my_list.append(s[j+1:j+1+length])
            i = j + 1 + length
        return my_list