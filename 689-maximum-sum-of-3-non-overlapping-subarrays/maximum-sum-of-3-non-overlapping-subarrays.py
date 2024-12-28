from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # Step 1: Calculate the sum of all subarrays of size k
        sums = [sum(nums[i:i+k]) for i in range(n - k + 1)]
        
        # Step 2: Initialize DP arrays
        left = [0] * len(sums)
        right = [0] * len(sums)
        
        # Fill the `left` array (max subarray index from start to i)
        max_index = 0
        for i in range(len(sums)):
            if sums[i] > sums[max_index]:
                max_index = i
            left[i] = max_index
        
        # Fill the `right` array (max subarray index from i to end)
        max_index = len(sums) - 1
        for i in range(len(sums) - 1, -1, -1):
            if sums[i] >= sums[max_index]:  # Use >= to prioritize rightmost indices
                max_index = i
            right[i] = max_index
        
        # Step 3: Iterate over the middle subarray and compute the result
        max_sum = 0
        res = []
        for j in range(k, len(sums) - k):
            l, r = left[j - k], right[j + k]
            total = sums[l] + sums[j] + sums[r]
            if total > max_sum:
                max_sum = total
                res = [l, j, r]
        
        return res
