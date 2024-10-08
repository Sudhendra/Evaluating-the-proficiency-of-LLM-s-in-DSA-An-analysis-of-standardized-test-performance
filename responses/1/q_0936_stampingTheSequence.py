from typing import List

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        def check_valid(start_idx):
            nonlocal stamped
            changed = False
            for i in range(len(stamp)):
                if stamped[start_idx + i] != '?' and stamped[start_idx + i] != stamp[i]:
                    return False
                if stamped[start_idx + i] == '?':
                    changed = True
            return changed
        
        n, m = len(target), len(stamp)
        stamped = '?' * n
        res = []
        replaced = True
        
        while replaced:
            replaced = False
            for i in range(n - m + 1):
                if check_valid(i):
                    replaced = True
                    res.append(i)
                    stamped = stamped[:i] + stamp + stamped[i + m:]
            
        if stamped != target:
            return []
        
        return res[::-1] if res else []