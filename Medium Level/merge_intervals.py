class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        N = len(intervals)
        answer = []
        intervals = sorted(intervals, key = lambda x : (x[0], x[1]))
        
        if N == 1:
            answer.append(intervals[0])
        
        else:
            for i in range(1, N):
                start1 = intervals[i-1][0]
                start2 = intervals[i][0]
                end1 = intervals[i-1][1]
                end2 = intervals[i][1]
                if end1 >= start2:
                    intervals[i][0] = min(start1, start2, end1, end2)
                    intervals[i][1] = max(start1, start2, end1, end2)
                    if intervals[i-1] in answer:
                        answer.remove(intervals[i-1])
                    answer.append(intervals[i])
                else:
                    if intervals[i-1] not in answer:
                        answer.append(intervals[i-1])
                    if intervals[i] not in answer:
                        answer.append(intervals[i])

        return answer
