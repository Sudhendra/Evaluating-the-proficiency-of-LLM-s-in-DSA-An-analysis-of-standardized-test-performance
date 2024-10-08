from typing import List

class Solution:
    
    def commonChars(self, words: List[str]) -> List[str]:
        def get_char_count(word):
            char_count = [0] * 26
            for char in word:
                char_count[ord(char) - ord('a')] += 1
            return char_count
        
        common_count = [float('inf')] * 26
        for word in words:
            curr_count = get_char_count(word)
            for i in range(26):
                common_count[i] = min(common_count[i], curr_count[i])
        
        result = []
        for i in range(26):
            result.extend([chr(i + ord('a'))] * common_count[i])
        
        return result
