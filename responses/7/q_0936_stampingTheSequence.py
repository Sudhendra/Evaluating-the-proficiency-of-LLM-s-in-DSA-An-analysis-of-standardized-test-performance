from typing import List

class Solution:

    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        def check(i):
            changed = False
            for j in range(len(stamp)):
                if target[i+j] == '?':
                    continue
                if target[i+j] != stamp[j]:
                    return False
                changed = True
            if changed:
                stamped_indices.append(i)
            return changed

        m, n = len(stamp), len(target)
        stamped_indices = []
        all_stamped_indices = []
        target = list(target)
        while stamped_indices != all_stamped_indices:
            all_stamped_indices = list(stamped_indices)
            for i in range(n - m + 1):
                if all(check(k) for k in range(i, i + m)):
                    continue
                for k in range(i, i + m):
                    target[k] = '?'
        return stamped_indices[::-1] if ''.join(target) == '?' * n else []

# Example Usage
stamp = "abc"
target = "ababc"
solution = Solution()
print(solution.movesToStamp(stamp, target))
