class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a,b = edges[0]
        c,d = edges[1]

        return c if a == c or b == c else d