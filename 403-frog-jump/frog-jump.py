class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {stone : set() for stone in stones}
        dp[stones[0]].add(0)

        for s in stones:
            for jump in dp[s]:
                for next_jump in {jump-1 , jump , jump + 1}:
                    if next_jump > 0 and s + next_jump in dp:
                        dp[s + next_jump].add(next_jump)
        return bool(dp[stones[-1]])

        