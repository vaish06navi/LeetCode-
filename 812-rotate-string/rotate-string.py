class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if set(s) != set(goal):
            return False

        for i in range(len(s)):
            newS = s[i:] + s[:i]
            if newS == goal:
                return True
        return False
        