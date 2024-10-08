class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        n = len(s)
        changes = []
        
        for i in range(len(indices)):
            index = indices[i]
            source = sources[i]
            target = targets[i]
            if s[index:index+len(source)] == source:
                changes.append((index, len(source), target))
        
        changes.sort(reverse=True)  # Sort changes so that we can apply them from right to left
        
        for index, length, target in changes:
            s = s[:index] + target + s[index + length:]
        
        return s
