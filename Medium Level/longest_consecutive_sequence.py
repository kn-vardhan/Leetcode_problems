class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        maximum = 0
        all_nums = set(nums)
        
        for num in all_nums:
            if num-1 not in all_nums:
                cur_num = num
                current = 1
                
                while cur_num+1 in all_nums:
                    cur_num += 1
                    current += 1
                    
                maximum = max(maximum, current)
                
        return maximum
