class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        mod = pow(10, 9) + 7
        
        if target > n * k:
            return 0
        
        matrix = [[0 for i in range(target + 1)] for i in range(n + 1)]
        
        tmin, tmax = max(1, target - (n - 1)*k), min(target - (n - 1), k)
        for i in range(tmin, tmax + 1):
            matrix[1][i] = 1
        
        for i in range(2, n+1):
            tmin, tmax = max(i, target - (n - i)*k), min(i*k, target - (n - i))
            for j in range(tmin, tmax + 1):
                fmin, fmax = max(1, j - (i - 1)*k), min(j - (i - 1), k)
                for x in range(fmin, fmax + 1):
                    matrix[i][j] += matrix[i - 1][j - x]
                matrix[i][j] = matrix[i][j] % mod

        return matrix[n][target]

