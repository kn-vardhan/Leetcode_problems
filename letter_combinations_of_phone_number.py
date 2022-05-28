class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        letters = {'2': ['a', 'b', 'c'],
                  '3': ['d', 'e', 'f'],
                  '4': ['g', 'h', 'i'],
                  '5': ['j', 'k' ,'l'],
                  '6': ['m', 'n', 'o'],
                  '7': ['p', 'q', 'r', 's'],
                  '8': ['t', 'u', 'v'],
                  '9': ['w', 'x', 'y', 'z']}
        combinations = []
        answer = []
        final = []
        
        temp = digits
        N = len(digits)
        if N == 0:
            return final
        
        for values in letters[digits[0]]:
            combinations.append(values)
        digits = digits[1:]
        
        while digits != "":
            for values in letters[digits[0]]:
                for i in range(len(combinations)):
                    combinations.append(combinations[i]+values)
            digits = digits[1:]

        for i in combinations:
            if len(i) == N:
                answer.append(i)
                
        for i in answer:
            count = 0
            for j in range(N):
                if i[j] in letters[temp[j]]:
                    count += 1
            if count == N and i not in final:
                final.append(i)

        return final
