from typing import List

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        mappings = sorted(zip(indices, sources, targets), reverse=True)
        for index, source, target in mappings:
            if s[index:index+len(source)] == source:
                s = s[:index] + target + s[index+len(source):]
        return s
