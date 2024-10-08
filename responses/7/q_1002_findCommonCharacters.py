from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        def count_chars(word):
            char_count = [0] * 26
            for char in word:
                char_count[ord(char) - ord('a')] += 1
            return char_count
        
        common = count_chars(words[0])
        for word in words:
            current_count = count_chars(word)
            for i in range(26):
                common[i] = min(common[i], current_count[i])
        
        result = []
        for i in range(26):
            result.extend([chr(ord('a') + i)] * common[i])
        
        return result
