class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in range(0,len(s)):
            if s[i] != '*':
                stack.append(s[i])
            elif stack:
                stack.pop()
        return ''.join(stack)


        