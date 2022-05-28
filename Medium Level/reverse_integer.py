class Solution:
    def reverse(self, x: int) -> int:
        m = -pow(2, 31)
        M = pow(2, 31) - 1
        
        reverse = []
        x = str(x)
        if x[0] == '-':
            x = x[1:]
            x = x[::-1]
            x = -int(x)
            if x < m or x > M: return 0
            else: return x
        else:
            x = x[::-1]
            x = int(x)
            if x < m or x > M: return 0
            else: return x


