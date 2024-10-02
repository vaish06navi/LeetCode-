class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        cuts = [0] * n
        is_palindrome = [[False] * n for _ in range(n)]
        
        for i in range(n):
            is_palindrome[i][i] = True
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or is_palindrome[i + 1][j - 1]:
                        is_palindrome[i][j] = True
        
        for i in range(n):
            if is_palindrome[0][i]:
                cuts[i] = 0
            else:
                cuts[i] = min(cuts[j] + 1 for j in range(i) if is_palindrome[j + 1][i])
        
        return cuts[n - 1]
