from typing import List

class Solution:
    def rectangleArea(self, rectangles: List[List[int]) -> int:
        MOD = 10**9 + 7

        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, x1, x2, 1))
            events.append((y2, x1, x2, -1))

        events.sort()
        active = []
        prev_y = events[0][0]
        ans = 0

        for curr_y, x1, x2, sign in events:
            width = 0
            for a, b in active:
                width += max(0, b-a)
            ans += width * (curr_y - prev_y)
            ans %= MOD

            if sign == 1:
                active.append((x1, x2))
                active.sort()
            else:
                active.remove((x1, x2))

            prev_y = curr_y

        return ans
