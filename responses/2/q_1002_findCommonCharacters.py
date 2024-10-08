from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        if not words:
            return result
        
        char_map = {}
        for char in words[0]:
            if char in char_map:
                char_map[char] += 1
            else:
                char_map[char] = 1
        
        for char in char_map:
            min_count = char_map[char]
            for word in words[1:]:
                count = word.count(char)
                min_count = min(min_count, count)
            result.extend([char] * min_count)
        
        return result