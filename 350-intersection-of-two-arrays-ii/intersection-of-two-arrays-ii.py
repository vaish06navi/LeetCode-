class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sortedArr1 = sorted(nums1)
        sortedArr2 = sorted(nums2)

        i = 0
        j = 0
        output = []

        while i<len(sortedArr1) and j<len(sortedArr2):
            if sortedArr1[i] < sortedArr2[j]:
                i+=1
            elif sortedArr1[i] > sortedArr2[j]:
                j+=1
            else:
                output.append(sortedArr1[i])
                i += 1
                j += 1
        return output
        