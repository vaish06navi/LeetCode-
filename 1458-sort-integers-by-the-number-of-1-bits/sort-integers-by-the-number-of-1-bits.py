class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda x: (bin(x).count('1') , x))


    #  0 == 0000
    #  1 == 0001
    #  2 == 0010
    #  3 == 0011
    #  4 == 0100
    #  5 == 0101
    #  6 == 0110
    #  7 == 0111
    #  8 == 1000


