class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n < len(original) or m*n > len(original):
            return []  
        
        List = []
        cnt = 0
        cnt2 = n
        for i in range(m):
            lst = []
            for j in range(cnt,n):
                lst.append(original[j])
            List.append(lst)
            cnt = n
            n = n + cnt2

        return List 