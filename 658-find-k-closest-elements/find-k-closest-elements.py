from heapq import heapify,heappop,heappush

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        heapify(heap)
        for i in arr:
            heappush(heap,(-1*abs(x-i),-1*i))
            if len(heap) > k:
                heappop(heap)
        res = []
        for i,j in heap:
            res.append(-j)
        return sorted(res)
        