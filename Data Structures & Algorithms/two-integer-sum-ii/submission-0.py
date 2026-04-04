class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0; j = len(numbers) - 1
        my_list = []
        while (i < j):
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                my_list += [i + 1, j + 1]
                return my_list