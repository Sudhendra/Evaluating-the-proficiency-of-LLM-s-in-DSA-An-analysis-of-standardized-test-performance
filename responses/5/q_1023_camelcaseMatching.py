from typing import List

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def match(query, pattern):
            j = 0
            for char in query:
                if j < len(pattern) and char == pattern[j]:
                    j += 1
                elif char.isupper():
                    return False
            return j == len(pattern)
        
        return [match(query, pattern) for query in queries]
