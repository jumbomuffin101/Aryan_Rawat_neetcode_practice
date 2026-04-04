class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}

        for string in strs:
            my_list = [0] * 26
            for letter in string:
                index = ord(letter) - ord('a')
                my_list[index] += 1
            my_tuple = tuple(my_list)
            if my_tuple in my_dict:
                my_dict[my_tuple].append(string)
            else:
                my_dict[my_tuple] = [string]
        return list(my_dict.values())