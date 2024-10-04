class Solution:
    def bottomup(self, K, p):
        dp = [[[0 for _ in range(K + 1)] for _ in range(3)] for _ in range(len(p) + 1)]
        
        for ind in range(len(p) - 1, -1, -1):
            for b in range(2):
                for k in range(1, K + 1):
                    if b:
                        dp[ind][b][k] = max(-p[ind] + dp[ind + 1][0][k], dp[ind + 1][b][k])
                    else:
                        dp[ind][b][k] = max(p[ind] + dp[ind + 1][1][k - 1], dp[ind + 1][b][k])
        
        return dp[0][1][K]

    def maxProfit(self, k, prices):
        return self.bottomup(k, prices)