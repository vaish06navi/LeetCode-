class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        
        for i in range(n):
            is_palindrome[i][i] = True
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or is_palindrome[i + 1][j - 1]:
                        is_palindrome[i][j] = True
        
        def dfs(start):
            if start == len(s):
                return [[]]
            
            result = []
            for end in range(start, len(s)):
                if is_palindrome[start][end]:
                    for sub in dfs(end + 1):
                        result.append([s[start:end + 1]] + sub)
            return result
        
        return dfs(0)
