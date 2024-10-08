from typing import List

class Solution:
    def rectangleArea(self, rectangles: List[List[int]) -> int:
        MOD = 10**9 + 7
        events = []

        for x1, y1, x2, y2 in rectangles:
            events.append((y1, 1, x1, x2))
            events.append((y2, -1, x1, x2))

        events.sort()
        x_intervals = []
        prev_y = events[0][0]
        prev_val = 0
        result = 0

        for y, delta, x1, x2 in events:
            result += (y - prev_y) * prev_val
            result %= MOD
            if delta == 1:
                x_intervals.append((x1, x2))
            else:
                x_intervals.remove((x1, x2))

            x_intervals.sort()
            total = 0
            prev_x = None

            for x_start, x_end in x_intervals:
                x_start = max(x_start, prev_x or x_start)
                total += max(0, x_end - x_start)
                prev_x = x_end

            prev_y = y
            prev_val = total

        return result
