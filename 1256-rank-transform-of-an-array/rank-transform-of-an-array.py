class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num_to_rank = {}

        nums = sorted(set(arr))

        rank = 1
        for num in nums:
            num_to_rank[num] = rank
            rank += 1
        
        for i in range(len(arr)):
            arr[i] = num_to_rank[arr[i]]
        return arr

            # 40,20,10,30
            # sorted(set(arr)) --> 10,20,30,40 
            # 10 = 1
            # 20 = 2
            # 30 = 3
            # 40 = 4
