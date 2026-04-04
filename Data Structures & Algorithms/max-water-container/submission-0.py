class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        i = 0; j = len(heights) - 1; my_max = 0;
        while (i < j):
            current_max = min(heights[i], heights[j]) * (j - i)
            my_max = max(current_max, my_max)
            
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
                
        return my_max
                