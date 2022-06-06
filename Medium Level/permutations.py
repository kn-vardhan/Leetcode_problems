class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        '''
        from itertools import permutations
        '''
        values = list(permutations(nums))
        return values
        
