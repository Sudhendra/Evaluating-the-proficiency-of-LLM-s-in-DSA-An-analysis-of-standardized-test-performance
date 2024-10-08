from typing import List

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def is_match(query, pattern):
            i = 0
            for letter in query:
                if i < len(pattern) and letter == pattern[i]:
                    i += 1
                elif 'A' <= letter <= 'Z':
                    return False
            return i == len(pattern)

        return [is_match(query, pattern) for query in queries]
