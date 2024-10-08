from typing import List

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        def overlap(w1, w2):
            max_overlap = 0
            for i in range(1, min(len(w1), len(w2))):
                if w1[-i:] == w2[:i]:
                    max_overlap = i
            return max_overlap

        while len(words) > 1:
            max_overlap_len = 0
            to_merge = (0, 1)

            for i in range(len(words)):
                for j in range(i + 1, len(words)):
                    ol = overlap(words[i], words[j])
                    if ol > max_overlap_len:
                        max_overlap_len = ol
                        to_merge = (i, j)

            i, j = to_merge
            words[i] += words[j][max_overlap_len:]
            del words[j]

        return words[0] if words else ""