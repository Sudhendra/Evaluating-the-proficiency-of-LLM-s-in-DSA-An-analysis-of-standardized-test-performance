from typing import List

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def get_odd_even_counts(word):
            odd = [0] * 26
            even = [0] * 26
            for i, char in enumerate(word):
                if i % 2 == 0:
                    even[ord(char) - ord('a')] += 1
                else:
                    odd[ord(char) - ord('a')] += 1
            return tuple(odd + even)

        unique_groups = set()
        for word in words:
            unique_groups.add(get_odd_even_counts(word))

        return len(unique_groups)
