from typing import List

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        def check_stamp(start):
            changed = False
            for i in range(len(stamp)):
                if target[start + i] == "?":
                    continue
                if target[start + i] != stamp[i]:
                    return False
                changed = True
            return changed
        
        m, n = len(stamp), len(target)
        stamp_set = set(stamp)
        result = []

        replaced = [False] * n
        cnt = 0

        while cnt < 10 * n:
            prev_cnt = cnt
            for i in range(n - m + 1):
                if not replaced[i] and check_stamp(i):
                    cnt += 1
                    result.append(i)
                    for j in range(m):
                        if target[i+j] != "?":
                            target = target[:i + j] + "?" + target[i + j + 1:]
                    replaced[i] = True
            if cnt == prev_cnt:
                break
        
        return result[::-1] if all(replaced) else []
