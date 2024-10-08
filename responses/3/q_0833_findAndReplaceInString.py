from typing import List

class Solution:

    def findReplaceString(
        self, s: str, indices: List[int], sources: List[str], targets: List[str]
    ) -> str:
        n = len(s)
        updates = sorted(zip(indices, sources, targets), reverse=True)

        for idx, source, target in updates:
            if s[idx:idx + len(source)] == source:
                s = s[:idx] + target + s[idx + len(source):]

        return s
