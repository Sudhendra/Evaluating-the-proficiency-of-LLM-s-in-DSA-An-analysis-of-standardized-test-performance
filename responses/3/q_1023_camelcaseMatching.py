from typing import List

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def is_match(query, pattern):
            idx_q, idx_p = 0, 0
            while idx_q < len(query) and idx_p < len(pattern):
                if query[idx_q] == pattern[idx_p]:
                    idx_q += 1
                    idx_p += 1
                elif query[idx_q].isupper():
                    return False
                else:
                    idx_q += 1
            if idx_p == len(pattern):
                return all(char.islower() for char in query[idx_q:])
            else:
                return False

        return [is_match(query, pattern) for query in queries]
