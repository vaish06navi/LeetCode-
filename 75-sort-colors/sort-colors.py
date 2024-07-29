class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zeros = 0
        ones = 0
        n = len(nums)

        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
        
        for i in range(0,zeros):
            nums[i] = 0

        for i in range(zeros , zeros+ones):
            nums[i] = 1

        for i in range(zeros+ones , n):
            nums[i] = 2    