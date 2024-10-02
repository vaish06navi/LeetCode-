class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len , i-stack[-1])
        return max_len

'''i - stack[-1] calculates the length of the current valid parentheses substring.

i is the current index (where a closing ) is found).
stack[-1] gives the index of the last unmatched ( or the base index (could be -1).'''