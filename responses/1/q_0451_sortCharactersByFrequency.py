from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        sorted_chars = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
        result = []
        for char in sorted_chars:
            result.append(char * counts[char])
        return ''.join(result)