class Solution:
    def frequencySort(self, s: str) -> str:
        char_freq = collections.Counter(s)
        sorted_chars = sorted(char_freq.keys(), key=lambda x: (-char_freq[x], x))
        result = ''.join([char * char_freq[char] for char in sorted_chars])
        return result