class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        counter = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in my_set:
                length = 1
                while (nums[i] + length) in my_set:
                    length += 1
                counter = max(counter, length)
        return counter