class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        for i in count:
            while count[i] > 2:
                nums.remove(i)
                count[i] -= 1

        return len(nums)


