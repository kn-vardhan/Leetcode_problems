class Solution:
    def minimumLines(self, points: List[List[int]]) -> int:
        
        points.sort()
        def slope(point1, point2):
            try:
                Y = point2[1] - point1[1]
                X = point2[0] - point1[0]
                return (X, Y)
            except:
                return float("inf")
        
        count = 1
        if len(points) == 1:
            return 0
        elif len(points) == 2:
            return count
            
        m = slope(points[0], points[1])
        for i in range(1, len(points) - 1):
            _m = slope(points[i], points[i+1])
            if m[0]*_m[1] != _m[0]*m[1]:
                count += 1
            m = _m
        
        return count


