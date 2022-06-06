class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        nums.sort()
        if len(nums) < 2:
            return 0
        if len(nums) == 2:
            return nums[1] - nums[0]
        
        gap = nums[1] - nums[0]
        for i in range(len(nums)-1):
            if (nums[i+1] - nums[i]) > gap:
                gap =  nums[i+1] - nums[i]
        
        return gap


