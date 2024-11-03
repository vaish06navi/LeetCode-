class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}

        for i, num in enumerate(nums):
            if num in mp and abs(mp[num] - i) <= k:
                return True
            else:
                mp[num] = i
        return False
        