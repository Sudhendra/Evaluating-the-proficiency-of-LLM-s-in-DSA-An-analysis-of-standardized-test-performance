from itertools import permutations

class Solution:
    def shortestSuperstring(self, words):
        def overlap(a, b):
            max_overlap = min(len(a), len(b))
            for i in range(max_overlap, -1, -1):
                if a.endswith(b[:i]):
                    return i
            return 0

        while len(words) > 1:
            max_overlap_len = 0
            to_merge = ()
            for pair in permutations(words, 2):
                overlap_len = overlap(*pair)
                if overlap_len > max_overlap_len:
                    max_overlap_len = overlap_len
                    to_merge = pair

            if max_overlap_len == 0:
                break

            words.remove(to_merge[0])
            words.remove(to_merge[1])
            words.append(to_merge[0] + to_merge[1][max_overlap_len:])

        return words[0] if words else ""