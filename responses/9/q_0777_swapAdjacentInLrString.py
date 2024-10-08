class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace('X', '') != end.replace('X', ''):
            return False

        n = len(start)
        i = j = 0

        while i < n and j < n:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and end[j] == 'X':
                j += 1

            if (i < n and j < n and start[i] != end[j]) or (i < n and j == n) or (i == n and j < n):
                return False

            if i < n and j < n:
                if start[i] == 'L' and i < j:
                    return False
                if start[i] == 'R' and i > j:
                    return False

            i += 1
            j += 1

        return True
