from typing import List

class Solution:

    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def get_key(w: str) -> str:
            even = ''.join(sorted(w[::2]))
            odd = ''.join(sorted(w[1::2]))
            return even + odd

        groups = set()
        for word in words:
            key = get_key(word)
            groups.add(key)

        return len(groups)
