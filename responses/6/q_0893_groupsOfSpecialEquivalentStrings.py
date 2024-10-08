from typing import List

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def generate_key(word):
            even_chars = ''.join(sorted(word[::2]))
            odd_chars = ''.join(sorted(word[1::2]))
            return even_chars + odd_chars

        unique_keys = set()
        for word in words:
            unique_keys.add(generate_key(word))
        
        return len(unique_keys)
