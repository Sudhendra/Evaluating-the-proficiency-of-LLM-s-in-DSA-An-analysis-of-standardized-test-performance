from typing import List

class Solution:
    
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n, m = len(stamp), len(target)
        stamp_list = list(stamp)
        target_list = list(target)
        res = []

        def check_ok(i):
            changed = False
            for j in range(n):
                if target_list[i+j] == '*':
                    continue
                if target_list[i+j] != stamp_list[j]:
                    return False
                changed = True
            if changed:
                target_list[i:i + n] = ['*'] * n
                res.append(i)
            return changed

        changed = True
        while changed:
            changed = False
            for i in range(m - n + 1):
                changed |= check_ok(i)

        return res[::-1] if target_list.count('*') == m else []