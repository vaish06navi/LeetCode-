class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = maxSum = sum(nums[:k])

        for i in range(k,len(nums)):
            currSum = currSum - nums[i-k] + nums[i]
            maxSum = max(maxSum,currSum)
        return maxSum/k
        