class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        '''
        from itertools import permutations
        '''
        values = list(set(permutations(nums)))
        return values


