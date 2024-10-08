from typing import List

class Solution:
    def rectangleArea(self, rectangles: List[List[int]) -> int:
        MOD = 10**9 + 7
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, x1, x2, 1))
            events.append((y2, x1, x2, -1))
        events.sort()

        def sweep():
            current_x_sum = 0
            prev_y = 0
            result = 0
            for y, x1, x2, sig in events:
                result += (y - prev_y) * current_x_sum
                current_x_sum = update_x_sum(current_x_sum, x1, x2, sig)
                prev_y = y
            return result

        def update_x_sum(current_x_sum, x1, x2, sign):
            if sign == 1:
                return current_x_sum + (x2 - x1)
            else:
                return current_x_sum - (x2 - x1)

        return sweep() % MOD