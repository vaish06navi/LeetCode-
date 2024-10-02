class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        LIS = [1]*n
        LDS = [1]*n

        # longest increasing subsequence from left
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    LIS[i] = max(LIS[i] , 1 + LIS[j])

        
        # longest increasing subsequence from right
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[j] < nums[i]:
                    LDS[i] = max(LDS[i] , 1 + LDS[j])
        
        ans = 1000
        for a,b in zip(LIS,LDS):
            if a == 1 or b == 1:
                continue
            else:
                ans = min(ans , n - (a+b-1))
        return ans
        