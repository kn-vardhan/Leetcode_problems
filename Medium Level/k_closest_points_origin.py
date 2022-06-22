class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dist = []
        ans = []
        for point in points:
            value = point[0]**2 + point[1]**2
            dist.append((value, point))

        dist.sort()
        for i in range(k):
            ans.append(dist[i][1])
        return ans


