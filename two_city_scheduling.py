class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        n = int(len(costs) / 2)
        costs.sort(key=lambda x: x[1]-x[0])
        minimum = 0
        
        for i in range(n):
            minimum += costs[i][1]
        for i in range(n, 2*n):
            minimum += costs[i][0]
        
        return minimum


