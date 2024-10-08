from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        char_freq = Counter(s)
        sorted_chars = sorted(char_freq.keys(), key=lambda x: (-char_freq[x], x))
        sorted_str = ''.join([char * char_freq[char] for char in sorted_chars])
        return sorted_str
