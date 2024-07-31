class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    # add 1 to diagonal value
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # get max of right/bottom --> account for prev matches
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])

        return dp[0][0]
        