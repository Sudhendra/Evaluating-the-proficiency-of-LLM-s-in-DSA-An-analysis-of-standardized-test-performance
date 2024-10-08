from typing import List

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def is_match(query, pattern):
            i, j = 0, 0
            while i < len(query) and j < len(pattern):
                if query[i] == pattern[j]:
                    i += 1
                    j += 1
                elif query[i].islower():
                    i += 1
                else:
                    return False
            if j == len(pattern):
                for k in range(i, len(query)):
                    if query[k].isupper():
                        return False
                return True
            return False
        
        return [is_match(query, pattern) for query in queries]
