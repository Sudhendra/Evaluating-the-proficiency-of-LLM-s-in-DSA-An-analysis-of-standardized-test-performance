from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freq_map = Counter(s)
        sorted_chars = sorted(freq_map.keys(), key=lambda x: (-freq_map[x], x))
        sorted_str = ''.join(char * freq_map[char] for char in sorted_chars)
        return sorted_str
