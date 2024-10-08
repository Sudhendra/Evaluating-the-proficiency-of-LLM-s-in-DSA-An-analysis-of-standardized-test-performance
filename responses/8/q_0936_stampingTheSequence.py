from typing import List

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        def check_stamp(start):
            changed = False
            for i in range(len(stamp)):
                if s[start + i] == '?':
                    continue
                if s[start + i] != stamp[i]:
                    return False
                changed = True
            if changed:
                nonlocal total_changes
                total_changes += len(stamp)
                for i in range(len(stamp)):
                    s[start + i] = '?'
                return True

        s = list(target)
        n, m = len(target), len(stamp)
        result = []
        total_changes = 0

        while total_changes < n * 10:
            changed = False
            for i in range(n - m + 1):
                if check_stamp(i):
                    result.append(i)
                    changed = True
            if not changed:
                break

        return result[::-1] if total_changes == n * 10 else []
