from itertools import permutations

class Solution:
    def shortestSuperstring(self, words):
        def overlap(w1, w2):
            max_overlap = 0
            for i in range(1, min(len(w1), len(w2))):
                if w1.endswith(w2[:i]):
                    max_overlap = i
            return max_overlap

        def merge(w1, w2):
            max_overlap = overlap(w1, w2)
            return w1 + w2[max_overlap:]

        while len(words) > 1:
            max_overlap_len = 0
            to_merge = ()
            for pair in permutations(words, 2):
                overlap_len = overlap(*pair)
                if overlap_len > max_overlap_len:
                    max_overlap_len = overlap_len
                    to_merge = pair

            if max_overlap_len == 0:
                words.append(words.pop(0))
            else:
                words.remove(to_merge[0])
                words.remove(to_merge[1])
                words.append(merge(*to_merge))

        return words[0]
