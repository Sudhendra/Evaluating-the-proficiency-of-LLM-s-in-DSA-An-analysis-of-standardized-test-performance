from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, path, segments):
            if len(path) == 4:
                if start == len(s):
                    result.append('.'.join(path))
                return
            for size in range(1, 4):
                if start + size <= len(s):
                    segment = s[start:start+size]
                    if str(int(segment)) == segment and 0 <= int(segment) <= 255:
                        backtrack(start + size, path + [segment], segments + 1)

        result = []
        backtrack(0, [], 0)
        return result
