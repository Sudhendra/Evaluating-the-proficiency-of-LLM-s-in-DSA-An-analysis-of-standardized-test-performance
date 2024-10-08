from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        char_count = Counter(s)
        sorted_chars = sorted(char_count, key=lambda c: (-char_count[c], c))
        return ''.join(c * char_count[c] for c in sorted_chars)
