


class Solution:
    def helper(self, out, temp, A, remain, index):
        if remain < 0:
            return
        elif remain == 0:
            out.append(list(temp))
        else:
            for i in range(index, len(A)):
                if i > index and A[i] == A[i - 1]:
                    continue  # skip duplicates
                temp.append(A[i])
                self.helper(out, temp, A, remain - A[i], i + 1)  # Note: we use 'i + 1' because we cannot reuse the same element
                temp.pop()

    def combinationSum2(self, candidates, target):
        out = []
        candidates.sort()
        self.helper(out, [], candidates, target, 0)
        return out