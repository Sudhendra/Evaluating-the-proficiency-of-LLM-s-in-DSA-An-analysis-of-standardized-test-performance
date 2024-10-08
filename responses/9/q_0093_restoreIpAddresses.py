from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, path, parts):
            if start == len(s) and parts == 4:
                res.append(".".join(path))
                return
            if parts >= 4:
                return
            for i in range(1, 4):
                if start + i > len(s):
                    break
                if i > 1 and s[start] == "0":
                    continue
                num = int(s[start:start+i])
                if 0 <= num <= 255:
                    backtrack(start + i, path + [s[start:start+i]], parts + 1)
        
        res = []
        backtrack(0, [], 0)
        return res
