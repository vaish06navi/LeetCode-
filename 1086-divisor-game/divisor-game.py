class Solution:
    def divisorGame(self, n: int) -> bool:
        # n = 2 --> alice = 1
        # n = 4 --> alice = 1,3
        # n = 5 --> alice = 1,3,5 ==> if alice choses an odd value she will lose
        if n % 2 != 0: # n&1
            return False
        return True

        if n < 2:
            return False

        dp = [False]*(n+1)
        dp[2] = True

        for i in range(3,n+1):
            for j in range(1,int(math.sqrt(i)) + 1):
                if i % j == 0 and dp[i-j] == False:
                    dp[i] = True
        return dp[i-1]
        