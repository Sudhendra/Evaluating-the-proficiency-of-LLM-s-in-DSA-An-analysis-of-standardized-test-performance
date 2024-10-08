from sortedcontainers import SortedList
from typing import List

class Solution:
    def rectangleArea(self, rectangles: List[List[int]) -> int:
        Mod = 10**9 + 7
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, x1, x2, 1))
            events.append((y2, x1, x2, -1))
        events.sort()
        active_x = SortedList()
        prev_y = ans = 0

        for y, x1, x2, sig in events:
            ans += (y - prev_y) * sum(x2 - x1 for x1, x2 in active_x) % Mod
            prev_y = y
            if sig == 1:
                active_x.add((x1, x2))
            else:
                active_x.remove((x1, x2))

        return ans % Mod
