from typing import List

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        m, n = len(stamp), len(target)
        stamp_list = list(stamp)
        target_list = list(target)
        stamped = [False] * n
        result = []
        is_stamped = True

        def check_stamped(start_index):
            is_changed = False
            for i in range(m):
                if not stamped[start_index + i] and target_list[start_index + i] != '?':
                    is_changed = True
                    break
            if not is_changed:
                for i in range(m):
                    stamped[start_index + i] = True
            return not is_changed

        while is_stamped:
            is_stamped = False
            for i in range(n - m + 1):
                is_stamped |= check_stamped(i)
        
        for i in range(n - m + 1):
            if stamped[i] and all(stamped[i:i+m]):
                result.append(i)
                for j in range(m):
                    stamped[i + j] = False

        if not all(stamped):
            return []
        return result[::-1]
