class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        start = 0
        end = len(nums) - 1
        value = nums[0]
        
        if len(nums) == 1:
            return value
        
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            elif nums[mid] < nums[start]:
                end = mid
            else:
                end = end - 1
        
        return nums[start]


