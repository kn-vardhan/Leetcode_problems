class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort()
        
        N = len(nums)
        for i in range(N):
            swap = False
            for j in range(0, N-i-1):
                if nums[j] > nums[j+1] :
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swap = True
            if swap == False:
                swap
