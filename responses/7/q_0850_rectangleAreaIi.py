class Solution:
    def rectangleArea(self, rectangles: List[List[int]) -> int:
        MOD = 10**9 + 7
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, x1, x2, 1))
            events.append((y2, x1, x2, -1))
        events.sort()
        
        def vertically_actives():
            return [x2 - x1 for x1, x2 in active] if active else [0]
        
        active = []
        cur_y = ans = 0
        for y, x1, x2, sig in events:
            ans += sum(vertically_actives()) * (y - cur_y)
            cur_y = y
            if sig == 1:
                active.append((x1, x2))
                active.sort()
            else:
                active.remove((x1, x2))
        return ans % MOD
