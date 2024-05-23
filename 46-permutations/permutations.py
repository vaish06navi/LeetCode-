class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        result = []
        for i,num in enumerate(nums):
            for r in self.permute(nums[:i] + nums[i+1:]):
                result.append([num]+r)
        return result
        