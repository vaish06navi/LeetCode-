class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l , m, r = 0,0,len(nums)-1
        while m <= r:
            x = nums[m]
            if x == 0:
                nums[l],nums[m] = nums[m],nums[l]
                l += 1
                m += 1
            elif x == 1:
                m += 1
            else:
                nums[m],nums[r] = nums[r],nums[m]
                r -= 1
                
        