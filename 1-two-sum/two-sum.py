class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1 , n):
                if nums[i] + nums[j] == target:
                    return [i, j ]
        return []

    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        n = len(nums)

        # build the hash map
        for i in range(n):
            h[nums[i]] = i
        
        # find the complement
        for i in range(n):
            comp = target - nums[i]
            if comp in h and h[comp] != i:
                return [i, h[comp]]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        n = len(nums)

        for i in range(n):
            comp = target - nums[i]
            if comp in h:
                return [h[comp] , i]
            h[nums[i]] = i
        return []
