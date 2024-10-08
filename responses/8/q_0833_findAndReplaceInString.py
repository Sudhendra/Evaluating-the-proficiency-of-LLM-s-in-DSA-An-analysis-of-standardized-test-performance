from typing import List

class Solution:

    def findReplaceString(
        self, s: str, indices: List[int], sources: List[str], targets: List[str]
    ) -> str:
        result = list(s)
        
        for i in range(len(indices)):
            idx = indices[i]
            source = sources[i]
            target = targets[i]
            
            if s[idx:idx+len(source)] == source:
                result[idx:idx+len(source)] = list(target)
                
        return "".join(result)
