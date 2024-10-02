class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)
        max_len = 2

        for i in range(n):
            dp[i] = {}

            for j in range(i):
                diff = nums[i] - nums[j]

                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2
                max_len = max(max_len , dp[i][diff])
        return max_len
        