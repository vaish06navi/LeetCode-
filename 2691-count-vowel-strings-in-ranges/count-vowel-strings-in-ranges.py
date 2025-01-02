class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(words)
        
        # Check if words start and end with vowels
        is_vowel_word = [1 if word[0] in vowels and word[-1] in vowels else 0 for word in words]
        
        # Build prefix sum
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + is_vowel_word[i]
        
        # Process queries
        result = []
        for l, r in queries:
            result.append(prefix_sum[r + 1] - prefix_sum[l])
        return result
