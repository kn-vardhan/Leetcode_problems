class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        return [key[0] for key in Counter(nums).most_common(k)]


