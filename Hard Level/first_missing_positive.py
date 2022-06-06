class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        count = {}
        MAX = nums[0]
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
            if i > MAX:
                MAX = i
        
        MAX = abs(MAX)
        for i in range(1, MAX+2):
            if i not in count:
                return i


