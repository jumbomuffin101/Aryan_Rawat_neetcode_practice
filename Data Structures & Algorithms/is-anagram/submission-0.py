class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}

        if len(s) != len(t):
            return False

        for x in s:
            dict[x] = dict.get(x, 0) + 1
        
        for y in t:
            dict[y] = dict.get(y, 0) - 1
        for value in dict.values():
            if (value != 0):
                return False
        return True