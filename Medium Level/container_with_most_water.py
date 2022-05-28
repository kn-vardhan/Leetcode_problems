class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        start = 0
        end = len(height) - 1
        temp = 0
        area = 0
        
        while start <= end:
            temp = (end-start) * min(height[start], height[end])
            
            if temp > area:
                area = temp
            
            if height[start] >= height[end]:
                end -= 1
            else:
                start += 1
        
        return area
