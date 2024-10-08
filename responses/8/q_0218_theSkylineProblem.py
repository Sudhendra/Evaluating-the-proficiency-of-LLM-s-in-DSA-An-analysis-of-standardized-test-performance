from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []
        
        def merge(left, right):
            h1, h2 = 0, 0
            i, j = 0, 0
            result = []
            while i < len(left) and j < len(right):
                if left[i][0] < right[j][0]:
                    x, h1 = left[i]
                    h = max(h1, h2)
                    i += 1
                elif left[i][0] > right[j][0]:
                    x, h2 = right[j]
                    h = max(h1, h2)
                    j += 1
                else:
                    x, h1 = left[i]
                    h, h2 = h1, right[j][1]
                    j += 1
                    i += 1
                if not result or h != result[-1][1]:
                    result.append([x, h])
            result.extend(right[j:])
            result.extend(left[i:])
            return result

        def skyline(buildings, start, end):
            if start == end:
                return [[buildings[start][0], buildings[start][2]], [buildings[start][1], 0]]
            mid = (start + end) // 2
            left = skyline(buildings, start, mid)
            right = skyline(buildings, mid + 1, end)
            return merge(left, right)

        return skyline(buildings, 0, len(buildings) - 1)
