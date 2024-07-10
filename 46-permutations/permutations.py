class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ml = []

        def permutations(i):
            if i == len(nums):
                sl = []
                for n in nums:
                    sl.append(n)

                ml.append(sl.copy())
                return

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                permutations(i + 1)
                nums[i], nums[j] = nums[j], nums[i]

        permutations(0)
        return ml
        