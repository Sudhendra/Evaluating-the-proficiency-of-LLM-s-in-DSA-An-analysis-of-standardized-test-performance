from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_chars = sorted(count.keys(), key=lambda x: count[x], reverse=True)
        result = "".join(char * count[char] for char in sorted_chars)
        return result
