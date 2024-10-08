from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words_count = {}
        for word in (s1 + " " + s2).split():
            words_count[word] = words_count.get(word, 0) + 1

        return [word for word in words_count if words_count[word] == 1]
