class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        low, high = 0, len(nums) - 1

        if nums[low] < nums[high]:
            return nums[low]

        while low <= high:
            if nums[low] < nums[high]:
                ans = min(ans, nums[low])
                break
            
            mid = (low + high) // 2
            ans = min(ans, nums[mid])

            
            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1
        return ans
