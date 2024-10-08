from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, path):
            if len(path) == 4 and start == len(s):
                result.append('.'.join(path))
                return
            if len(path) >= 4:
                return
            for i in range(1, 4):
                if start + i > len(s):
                    break
                segment = s[start:start+i]
                if (segment[0] == '0' and len(segment) > 1) or int(segment) > 255:
                    continue
                backtrack(start+i, path + [segment])

        result = []
        backtrack(0, [])
        return result