class Solution:
    def getSum(self, a: int, b: int) -> int:
        def sum(a,b):
            if not a or not b:
                return a or b
            return add(a^b,(a&b) <<1)
        return add(a,b)
        