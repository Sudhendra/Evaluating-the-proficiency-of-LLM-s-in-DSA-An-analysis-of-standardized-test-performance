class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result = set()
        cur = set()
        for num in arr:
            cur = {num | x for x in cur} | {num}
            result |= cur
        return len(result)
