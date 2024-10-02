class Solution:
    def divisorGame(self, n: int) -> bool:
        # n = 2 --> alice = 1
        # n = 4 --> alice = 1,3
        # n = 5 --> alice = 1,3,5 ==> if alice choses an odd value she will lose
        if n % 2 != 0:
            return False
        return True
        