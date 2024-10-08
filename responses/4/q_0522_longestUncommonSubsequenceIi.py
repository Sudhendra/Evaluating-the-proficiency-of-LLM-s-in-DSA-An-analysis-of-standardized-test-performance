class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        i = 0
        for char in t:
            if i < len(s) and s[i] == char:
                i += 1
        return i == len(s)

    def findLUSlength(self, strs: List[str]) -> int:
        def is_unique(idx):
            for i, word in enumerate(strs):
                if i != idx and self.is_subsequence(strs[idx], word):
                    return False
            return True

        strs.sort(key=len, reverse=True)
        for idx, word in enumerate(strs):
            if is_unique(idx):
                return len(word)
        return -1
