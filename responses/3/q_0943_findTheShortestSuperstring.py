from itertools import permutations

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        def combine(s1, s2):
            for i in range(len(s1)):
                if s2.startswith(s1[i:]):
                    return s1[:i] + s2
            return s1 + s2

        def merge(s1, s2):
            max_overlap = 0
            res = ""
            for i in range(len(s1)):
                if s2.startswith(s1[i:]):
                    if len(s1) - i > max_overlap:
                        max_overlap = len(s1) - i
                        res = s1[:i] + s2
            return res

        shortest_superstring = "".join(words)
        
        for perm in permutations(words):
            superstring = perm[0]
            for i in range(1, len(perm)):
                superstring = merge(superstring, perm[i])
            if len(superstring) < len(shortest_superstring):
                shortest_superstring = superstring
        
        return shortest_superstring
