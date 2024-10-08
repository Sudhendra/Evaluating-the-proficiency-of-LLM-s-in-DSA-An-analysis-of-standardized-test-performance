from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, path, parts):
            if start == len(s) and parts == 4:
                result.append('.'.join(path))
                return

            if parts == 4 or start == len(s):
                return

            for size in range(1, 4):
                if start + size > len(s):
                    break

                if size > 1 and s[start] == '0':
                    continue

                segment = s[start:start+size]
                if int(segment) <= 255:
                    backtrack(start + size, path + [segment], parts + 1)

        result = []
        backtrack(0, [], 0)
        return result
