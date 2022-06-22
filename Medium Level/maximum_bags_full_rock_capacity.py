class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        total = []
        extra = additionalRocks
        for i in range(len(rocks)):
            total.append((rocks[i], capacity[i]))
        total.sort(key=lambda x: x[1]-x[0])
        
        answer = 0
        for i in range(len(total)):
            diff = total[i][1] - total[i][0]
            if diff == 0:
                answer += 1
            if diff != 0 and extra >= diff: 
                extra -= diff
                answer += 1
            elif diff != 0 and extra < diff:
                extra = 0
                break

        return answer


