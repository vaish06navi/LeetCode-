class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(cap):
            kk = i = 0
            while i < len(nums) and kk < k:
                if nums[i] <= cap:
                    kk += 1
                    i += 2
                else:
                    i += 1
            
            return kk == k

        minCap, maxCap = min(nums), max(nums)
        result = maxCap
        while minCap <= maxCap:
            cap = minCap + (maxCap - minCap)//2
            if check(cap):
                result = cap
                maxCap = cap - 1
            else:
                minCap = cap + 1
                
        return result