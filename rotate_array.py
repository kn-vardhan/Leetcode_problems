class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        for i in range(k % N):
            value = (nums.pop())
            nums.insert(0, value)


