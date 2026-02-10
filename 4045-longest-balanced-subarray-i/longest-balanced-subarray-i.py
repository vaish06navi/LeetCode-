class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        max_len = 0
        n = len(nums)

        for i in range(n):
            even_set = set()
            odd_set = set()

            for j in range(i, n):
                if nums[j] %2 == 0:
                    even_set.add(num[j])
                else:
                    odd_set.add(num[j])

                if len(even_set) == len(odd_set):
                    max_len = max(max_len,  j-i+1)
        return max_len
        

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for l in range(n):
            freq = {}
            even_count = 0
            odd_count = 0

            for r in range(l, n):
                x = nums[r]

                if x not in freq:
                    if x%2 == 0:
                        even_count += 1
                    else:
                        odd_count += 1
                    freq[x] = 1
                else:
                    freq[x] += 1
                if even_count == odd_count:
                    ans = max(ans , r-l+1)
        return ans