from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start, parts):
            if len(parts) == 4:
                if start == len(s):
                    output.append(".".join(parts))
                return

            # Try 1, 2, or 3 digits as the next part
            for size in range(1, 4):
                if start + size <= len(s):
                    part = s[start:start+size]
                    if str(int(part)) == part and int(part) <= 255:
                        backtrack(start + size, parts + [part])

                    # Avoid leading zeros except for 0 itself
                    if s[start] == "0":
                        break

        output = []
        backtrack(0, [])
        return output
