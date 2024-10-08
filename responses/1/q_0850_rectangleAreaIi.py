class Solution:
    def rectangleArea(self, rectangles: List[List[int]) -> int:
        all_x = []
        events = []
        MOD = 10 ** 9 + 7

        for x1, y1, x2, y2 in rectangles:
            all_x.append(x1)
            all_x.append(x2)
            events.append((y1, x1, x2, 1))
            events.append((y2, x1, x2, -1))

        all_x.sort()
        all_x = {x: i for i, x in enumerate(all_x)}
        active_intervals = [0] * len(all_x)
        events.sort()

        prev_y, total_area = 0, 0

        for y, x1, x2, val in events:
            total_area += (y - prev_y) * sum(w for i, w in enumerate(active_intervals) if i > 0)
            prev_y = y
            for i in range(all_x[x1], all_x[x2]):
                active_intervals[i] += val

        return total_area % MOD