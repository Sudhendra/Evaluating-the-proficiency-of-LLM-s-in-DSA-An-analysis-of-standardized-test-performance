from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        cur = set()
        for num in arr:
            cur = {num | x for x in cur} | {num}
            ans |= cur
        return len(ans)