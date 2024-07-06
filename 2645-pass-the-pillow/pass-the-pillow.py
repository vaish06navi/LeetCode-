
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        rounds = time // (n - 1)
        ans = 0
        if rounds % 2 == 0:
            ans = 1 + time % (n - 1)
        else:
            ans = n - time % (n - 1)
        return ans
