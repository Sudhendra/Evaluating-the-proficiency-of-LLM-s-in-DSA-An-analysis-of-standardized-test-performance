from typing import List

class Solution:
    def findReplaceString(
        self, s: str, indices: List[int], sources: List[str], targets: List[str]
    ) -> str:
        replacements = sorted(zip(indices, sources, targets), reverse=True)
        
        for i, source, target in replacements:
            if s[i:i + len(source)] == source:
                s = s[:i] + target + s[i + len(source):]

        return s
