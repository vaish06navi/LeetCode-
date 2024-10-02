class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        nums.sort()  # Sort the numbers
        
        n = len(nums)
        dp = [1] * n  # dp[i] will store the size of the largest divisible subset ending at nums[i]
        prev = [-1] * n  # prev[i] will store the index of the previous element in the subset
        max_index = 0  # Index of the largest element in the largest divisible subset
        
        # Build the dp array
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            
            # Update max_index to the largest subset found
            if dp[i] > dp[max_index]:
                max_index = i
        
        # Reconstruct the largest subset
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]
        
        return result[::-1]  # Reverse to get the correct order