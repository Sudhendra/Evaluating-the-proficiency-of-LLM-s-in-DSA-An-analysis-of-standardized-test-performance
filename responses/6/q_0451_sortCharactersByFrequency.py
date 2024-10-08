from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        sorted_chars = sorted(counts, key=lambda x: (-counts[x], x))
        return ''.join(char * counts[char] for char in sorted_chars)
