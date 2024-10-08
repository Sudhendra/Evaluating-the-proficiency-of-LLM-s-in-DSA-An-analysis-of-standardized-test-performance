from typing import List

class Solution:
    def rectangleArea(self, rectangles: List[List[int]) -> int:
        MOD = 10**9 + 7

        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, 1, x1, x2))
            events.append((y2, -1, x1, x2))
        events.sort()

        def get_area() -> int:
            ans = 0
            curr_x_intervals = []
            curr_y = events[0][0]
            for y, delta, x1, x2 in events:
                ans += sum(x2 - x1 for x1, x2 in curr_x_intervals) * (y - curr_y)
                if delta == 1:
                    curr_x_intervals.append((x1, x2))
                    curr_x_intervals.sort()
                else:
                    curr_x_intervals.remove((x1, x2))
                curr_y = y
            return ans % MOD

        return get_area()
