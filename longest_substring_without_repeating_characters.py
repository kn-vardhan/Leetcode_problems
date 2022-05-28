class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        values = {}
        MAX = 0
        start = 0
        for i, j in enumerate(s):
            if j in values:
                SUM = values[j] + 1
                if SUM > start:
                    start = SUM
            
            temp = i - start + 1
            if temp > MAX:
                MAX = temp
            values[j] = i
        
        return MAX
