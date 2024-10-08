from typing import List

class Solution:
    
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, path):
            if len(path) == 4 and start == len(s):
                res.append(".".join(path))
                return
            if len(path) == 4 or start >= len(s):
                return

            for i in range(1, 4):
                if start + i > len(s):
                    break
                if s[start] == "0" and i > 1:
                    continue
                if 0 <= int(s[start:start+i]) <= 255:
                    backtrack(start+i, path + [s[start:start+i]])

        res = []
        backtrack(0, [])
        return res
