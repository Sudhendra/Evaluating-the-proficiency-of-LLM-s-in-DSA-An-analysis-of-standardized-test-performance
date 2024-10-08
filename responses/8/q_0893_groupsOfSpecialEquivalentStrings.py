from typing import List

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def count_special_equiv(word):
            even_chars = sorted(word[::2])
            odd_chars = sorted(word[1::2])
            return ''.join(even_chars) + ''.join(odd_chars)

        groups = set()
        for word in words:
            groups.add(count_special_equiv(word))

        return len(groups)
