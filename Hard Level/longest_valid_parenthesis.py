class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        values = []
        for i in range(len(s)):
            if s[i] == '(' or not values:
                values.append(i)
            else:
                t = values.pop()
                if s[t] == ')':
                    values.append(t)
                    values.append(i)

        right, longest = len(s), 0
        while len(values) > 0:
            left = values.pop()
            longest = max(longest, right-left-1)
            right = left

        return max(longest,right)


