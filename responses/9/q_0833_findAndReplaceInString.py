class Solution:
    def findReplaceString(
        self, s: str, indices: List[int], sources: List[str], targets: List[str]
    ) -> str:
        sources_mapping = {indices[i]: (sources[i], targets[i]) for i in range(len(indices))}
        sorted_indices = sorted(sources_mapping.keys(), reverse=True)
        
        for index in sorted_indices:
            source, target = sources_mapping[index]
            if s[index:index+len(source)] == source:
                s = s[:index] + target + s[index+len(source):]
        
        return s
