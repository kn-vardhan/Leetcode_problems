class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        _nums = {}
        for i in range(len(nums)):
            _nums[nums[i]] = i
        for row in operations:
            nums[_nums[row[0]]] = row[1]
            _nums[row[1]] = _nums[row[0]]
    
        return nums


