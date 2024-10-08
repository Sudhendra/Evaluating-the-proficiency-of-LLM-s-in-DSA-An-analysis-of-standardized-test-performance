from typing import List

class Solution:

    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n, m = len(stamp), len(target)
        stamp_chars = set(stamp)
        target_list = list(target)
        res = []
        replaced = False

        def check_valid(idx):
            nonlocal replaced
            changed = False
            for i in range(n):
                if target_list[idx + i] == '?':
                    continue
                if target_list[idx + i] != stamp[i]:
                    return False
                changed = True
            if changed:
                replaced = True
            return changed

        while replaced:
            replaced = False
            for i in range(m - n + 1):
                if check_valid(i):
                    res.append(i)
                    for j in range(n):
                        target_list[i + j] = '?'
        return res[::-1] if all(c == '?' for c in target_list) else []
