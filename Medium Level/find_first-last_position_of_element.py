class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        values = [-1, -1]
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            if values[0] != -1 and values[1] != -1:
                break
            if values[0] == -1:
                if nums[l] == target:
                    values[0] = l
                else:
                    l += 1
            if values[1] == -1:
                if nums[r] == target:
                    values[1] = r
                else:
                    r -= 1
        
        return values
