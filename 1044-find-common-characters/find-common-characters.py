class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) < 2:
            return words

        res = []
        word1 = set(words[0])
        for ch in word1:
            freq = min([word.count(ch) for word in words])
            res += [ch]*freq
        return res