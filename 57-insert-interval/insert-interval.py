class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def overlap(interval1,interval2):
            return interval1[1] >= interval2[0] and interval2[1] >= interval1[0]

        res = []
        temp = newInterval
        for i in intervals:
            if not overlap(temp,i):
                res.append(i)
            else:
                temp = [min(temp[0],i[0]) , max(temp[1],i[1])]
        res.append(temp)
        return sorted(res)
        