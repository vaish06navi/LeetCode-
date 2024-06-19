class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        ans = -1
        start, end = 0, max(bloomDay)

        def numberOfBouquets(bloomDay, mid, k):
            ans, cnt = 0, 0

            for day in bloomDay:
                if day <= mid:
                    cnt += 1
                else:
                    cnt = 0

                if cnt == k:
                    ans += 1
                    cnt = 0
            return ans

        while start <= end:
            mid = (start + end) // 2

            if numberOfBouquets(bloomDay, mid, k) >= m:
                ans = mid
                end = mid - 1
            else:
                start = mid + 1

        return ans

        

        