from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        seen = set()
        cur = set()
        for num in arr:
            cur = {num | c for c in cur} | {num}
            seen |= cur
        return len(seen)
