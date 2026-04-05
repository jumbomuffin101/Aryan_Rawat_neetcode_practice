class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_list = []
        max_length = 0

        for l in s:
            while l in my_list:
                my_list.pop(0)
            my_list.append(l)
            max_length = max(max_length, len(my_list))

        return max_length