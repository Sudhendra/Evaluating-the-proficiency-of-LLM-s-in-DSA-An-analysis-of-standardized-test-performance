class Solution:
    def findLUSlength(self, strs):
        def is_subsequence(s, t):
            i, j = 0, 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                j += 1
            return i == len(s)

        def is_unique(s, strs):
            for other in strs:
                if is_subsequence(s, other):
                    return False
            return True

        sorted_strs = sorted(strs, key=len, reverse=True)
        for i, s in enumerate(sorted_strs):
            if all(not is_subsequence(s, sorted_strs[j]) for j in range(len(sorted_strs)) if j != i):
                return len(s)
        return -1