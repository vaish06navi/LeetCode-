class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        arr = []
        maxCandies = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandies:
                arr.append(True)
            else:
                arr.append(False)
        return arr        