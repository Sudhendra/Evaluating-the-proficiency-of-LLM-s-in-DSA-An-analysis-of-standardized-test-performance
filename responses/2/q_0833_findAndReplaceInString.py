class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        replacements = sorted(zip(indices, sources, targets), key=lambda x: x[0], reverse=True)
        for index, source, target in replacements:
            if s[index:index + len(source)] == source:
                s = s[:index] + target + s[index + len(source):]
        return s