from typing import List

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        def overlap(s1, s2):
            max_overlap = min(len(s1), len(s2))
            for i in range(max_overlap, 0, -1):
                if s1.endswith(s2[:i]):
                    return i
            return 0

        def combine(s1, s2, overlap_len):
            if overlap_len == 0:
                return s1 + s2
            if s1.endswith(s2[:overlap_len]):
                return s1 + s2[overlap_len:]
            return s1 + s2

        def dfs(state, path):
            if len(path) == len(words):
                return ''.join(path)

            last_word = path[-1] if path else ''
            max_overlap = 0
            next_word = ''
            for word in words:
                if word not in state:
                    overlap_len = overlap(last_word, word)
                    if overlap_len > max_overlap:
                        max_overlap = overlap_len
                        next_word = word

            state.add(next_word)

            path.append(combine(last_word, next_word, max_overlap))
            result = dfs(state, path)
            path.pop()
            state.remove(next_word)

            return result

        start_word = max(words, key=len)
        return dfs(set([start_word]), [start_word])
