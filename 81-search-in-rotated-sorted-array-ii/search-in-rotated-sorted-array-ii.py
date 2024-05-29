class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return True

            if nums[start] == nums[mid]:
                start += 1
                continue
            elif nums[mid] <= nums[end]:
                if target >= nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if target >= nums[start] and target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

        return False
            
        