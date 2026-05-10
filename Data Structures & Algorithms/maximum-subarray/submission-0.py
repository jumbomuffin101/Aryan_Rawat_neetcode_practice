class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = 0
        bestSum = nums[0]
        for num in nums:
            if currentSum < 0:
                currentSum = 0
                currentSum += num
            else:
                currentSum += num
            bestSum = max(currentSum, bestSum)
        return bestSum