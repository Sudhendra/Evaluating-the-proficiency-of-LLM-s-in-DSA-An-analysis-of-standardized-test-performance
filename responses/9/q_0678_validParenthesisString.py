class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0
        for char in s:
            lo += 1 if char == '(' else -1
            hi -= 1 if char == ')' else -1
            if hi < 0:
                break
            lo = max(lo, 0)
        return lo == 0
