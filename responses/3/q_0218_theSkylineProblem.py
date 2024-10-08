from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []

        def merge(left, right):
            h1, h2 = 0, 0
            res = []
            while left or right:
                if not left:
                    return res + right
                elif not right:
                    return res + left
                x = 0
                if left[0][0] < right[0][0]:
                    x, h1 = left.pop(0)
                elif left[0][0] > right[0][0]:
                    x, h2 = right.pop(0)
                else:
                    x, h1 = left.pop(0)
                    h2 = right.pop(0)
                H = max(h1, h2)
                if not res or H != res[-1][1]:
                    res.append([x, H])
            return res

        n = len(buildings)
        if n == 1:
            left, right, height = buildings[0]
            return [[left, height], [right, 0]]

        mid = n // 2
        left_skyline = self.getSkyline(buildings[:mid])
        right_skyline = self.getSkyline(buildings[mid:])
        
        return merge(left_skyline, right_skyline)