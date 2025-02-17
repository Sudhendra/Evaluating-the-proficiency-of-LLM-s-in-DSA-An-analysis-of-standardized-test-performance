from typing import List

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def is_match(query: str, pattern: str) -> bool:
            idx = 0
            for char in query:
                if idx < len(pattern) and char == pattern[idx]:
                    idx += 1
                elif char.isupper():
                    return False
            return idx == len(pattern)

        return [is_match(query, pattern) for query in queries]
