from typing import List

class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        def can_stamp(s, t, i):
            stamped = False
            for j in range(len(s)):
                if t[i+j] != '?' and t[i+j] != s[j]:
                    return False
                if t[i+j] != '?':
                    stamped = True
            return stamped

        def stamp_at(s, t, i):
            for j in range(len(s)):
                t[i+j] = '?'

        n, m = len(target), len(stamp)
        target = list(target)
        res = []
        found = True

        while found:
            found = False
            for i in range(n - m + 1):
                if can_stamp(stamp, target, i):
                    stamp_at(stamp, target, i)
                    res.append(i)
                    found = True

        if all(c == '?' for c in target):
            return res[::-1]
        else:
            return []

# Example usage
solution = Solution()
print(solution.movesToStamp("abc", "ababc"))  # Output: [0, 2]
print(solution.movesToStamp("abca", "aabcaca"))  # Output: [3, 0, 1]
