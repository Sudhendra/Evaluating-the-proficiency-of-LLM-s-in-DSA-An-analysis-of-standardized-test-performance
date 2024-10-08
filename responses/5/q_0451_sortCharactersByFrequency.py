class Solution:
    def frequencySort(self, s: str) -> str:
        char_frequency = {}
        for char in s:
            char_frequency[char] = char_frequency.get(char, 0) + 1
        
        sorted_chars = sorted(char_frequency, key=lambda x: (-char_frequency[x], x))
        result = ''.join(char * char_frequency[char] for char in sorted_chars)
        
        return result