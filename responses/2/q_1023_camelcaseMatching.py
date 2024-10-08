class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def is_match(query: str, pattern: str) -> bool:
            idx_p = 0
            for char_q in query:
                if idx_p < len(pattern) and char_q == pattern[idx_p]:
                    idx_p += 1
                elif char_q.isupper():
                    return False
            return idx_p == len(pattern)

        return [is_match(query, pattern) for query in queries]