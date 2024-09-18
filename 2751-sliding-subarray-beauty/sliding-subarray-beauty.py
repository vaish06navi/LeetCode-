from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        arr = SortedList([])
        ans = []

        # step 1 : First we are add element of k-1 range  make window of k-1 range
        for ele in range(k):
            arr.add(nums[ele])

        # step 2 : Then we are iterate from iterate from the k+1,len(nums) and if len(a)>=x and xth smallest is <0 
        for i in range(k,len(nums)):
            if x <= len(arr) and arr[x-1] < 0:
                ans.append(arr[x-1])
            else:
                ans.append(0)
            
            # step 3 : Slide the window by adding and the remove first element
            arr.remove(nums[i-k])
            arr.add(nums[i])

        # print(ans)
        if x <= len(arr) and arr[x-1] < 0:
            ans.append(arr[x-1])
        else:
            ans.append(0)
        return ans
    

