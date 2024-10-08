from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(num):
            return str(int(num)) == num and 0 <= int(num) <= 255

        def backtrack(start, parts):
            if start == len(s) and len(parts) == 4:
                result.append(".".join(parts))
            elif len(parts) < 4:
                for size in range(1, 4):
                    if start + size <= len(s):
                        part = s[start:start+size]
                        if is_valid(part):
                            backtrack(start+size, parts + [part])

        result = []
        backtrack(0, [])
        return result