class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        count = value = floor(n / 5)
        i = 1
        while value != 0:
            i += 1
            value = floor(n / pow(5, i))
            count += value
        
        return count


