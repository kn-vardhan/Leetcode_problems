class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def fact(n):
            val = 1
            for i in range(1, n+1):
                val *= i
            return val
        
        Nr = fact(m+n-2)
        Dr = fact(m-1) * fact(n-1)
        
        return int(Nr/Dr)


