from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        result = []
        target_count = len(words)
        char_count = [float('inf')] * 26  # Initialize with infinity count for each character

        for word in words:
            word_char_count = [0] * 26
            for char in word:
                word_char_count[ord(char) - ord('a')] += 1

            for i in range(26):
                char_count[i] = min(char_count[i], word_char_count[i])

        for i, count in enumerate(char_count):
            result.extend([chr(i + ord('a'))] * count)

        return result
