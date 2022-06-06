class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split()
        words = words[::-1]
        answer = " ".join(x for x in words)
        return answer


