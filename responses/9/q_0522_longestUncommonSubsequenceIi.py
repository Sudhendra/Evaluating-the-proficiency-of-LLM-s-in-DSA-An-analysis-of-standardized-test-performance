from collections import Counter

class Solution:
    def is_subsequence(self, s1, s2):
        i = j = 0
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i += 1
            j += 1
        return i == len(s1)

    def findLUSlength(self, strs: List[str]) -> int:
        def dfs(start, curr_seq):
            nonlocal max_seq_len
            if start == len(strs):
                for s in strs:
                    if self.is_subsequence(curr_seq, s):
                        return
                max_seq_len = max(max_seq_len, len(curr_seq))
                return
            dfs(start + 1, curr_seq)
            dfs(start + 1, curr_seq + strs[start])

        strs.sort(key=len, reverse=True)
        max_seq_len = -1
        dfs(0, "")
        return max_seq_len
