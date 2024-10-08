from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, parts):
            if start == len(s) and len(parts) == 4:
                result.append(".".join(parts))
                return
            if len(parts) >= 4:
                return
            for size in range(1, 4):
                if start + size > len(s):
                    break
                if size > 1 and s[start] == '0':
                    continue
                chunk = s[start:start+size]
                if 0 <= int(chunk) <= 255:
                    backtrack(start+size, parts + [chunk])
        
        result = []
        backtrack(0, [])
        return result
