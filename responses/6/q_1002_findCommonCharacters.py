from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        result = []
        common_count = Counter(words[0])

        for word in words[1:]:
            word_count = Counter(word)
            common_count &= word_count

        for char, count in common_count.items():
            result.extend([char] * count)

        return result
