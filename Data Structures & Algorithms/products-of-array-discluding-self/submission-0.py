class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            left_products[i] = prefix
            prefix = prefix * nums[i]

        right_products = [1] * len(nums)
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            right_products[i] = suffix
            suffix = suffix * nums[i]
        
        my_list = []
        for i in range(len(nums)):
            my_list.append(left_products[i] * right_products[i])
        return my_list