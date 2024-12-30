class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        m = len(s)
        n = len(spaces)

        res = []
        first = 0
        second = 0

        while first < m:
            if second < n and first == spaces[second]:
                res.append(' ')
                second += 1
            res.append(s[first])
            first += 1
        return ''.join(res)
