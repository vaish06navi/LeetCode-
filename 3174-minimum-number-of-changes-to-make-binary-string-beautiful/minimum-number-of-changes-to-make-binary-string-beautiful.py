# class Solution:
#     def minChanges(self, s: str) -> int:
#         l = 0
#         res = 0

#         for r in range(len(s)):
#             if s[l] != s[r]:
#                 if r %2 == 1:
#                     res += 1
#                 l = r
#         return res
        
class Solution:
    def minChanges(self, s: str) -> int:
        res = 0

        for i in range(0, len(s) , 2):
            if s[i] != s[i+1]:
                res += 1
        return res
        