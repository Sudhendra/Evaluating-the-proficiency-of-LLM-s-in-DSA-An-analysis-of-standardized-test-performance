class Solution:
    def rectangleArea(self, rectangles: List[List[int]) -> int:
        MOD = 10**9 + 7
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, x1, x2, 1))
            events.append((y2, x1, x2, -1))
        events.sort()
        active = []
        prev_y = 0
        result = 0
        for y, x1, x2, sign in events:
            width = 0
            prev_x = 0
            for a, b in active:
                width += max(0, b - max(a, prev_x))
                prev_x = b
            result += width * (y - prev_y)
            result %= MOD
            prev_y = y
            if sign == 1:
                active.append((x1, x2))
                active.sort()
            else:
                active.remove((x1, x2))
        return result
