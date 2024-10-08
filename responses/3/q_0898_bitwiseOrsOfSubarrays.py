from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        cur = set()
        for num in arr:
            cur = {num | ele for ele in cur} | {num}
            res |= cur
        return len(res)
