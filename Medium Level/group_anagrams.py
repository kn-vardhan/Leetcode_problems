class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        answer = defaultdict(list)
        for i in strs:
            answer[''.join(sorted(i))].append(i)
        return list(answer.values())
