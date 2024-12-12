import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            max_idx = gifts.index(max(gifts))
            gifts[max_idx] = math.floor(math.sqrt(gifts[max_idx]))
        return sum(gifts)
        