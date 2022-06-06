class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        value = sum(set(nums))*3 - sum(nums)
        value /= 2
        return int(value)


