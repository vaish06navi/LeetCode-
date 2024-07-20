class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #base case
        if len(nums) < 2: return nums

        mid = len(nums) // 2

        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(nums,left,right)

    # define merge function to merge two arrays
    def merge(self, nums, left,right):
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
                k +=1
            else:
                nums[k] = right[j]
                j += 1
                k += 1

        while i < len(left):
            nums[k] = left[i]
            k += 1
            i += 1

        while j < len(right):
            nums[k] = right[j]
            k += 1
            j += 1
            
        return nums


