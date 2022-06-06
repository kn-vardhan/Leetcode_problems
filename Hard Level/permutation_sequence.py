class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        '''
        from itertools import permutations
        '''
        nums = []
        for i in range(1, n+1):
            nums.append(i)
        values = list(permutations(nums))
        answer = "".join(str(x) for x in values[k-1])
        return answer


