from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_dist = 0
        prev_occupied_seat = None
        for i, seat in enumerate(seats):
            if seat == 1:
                if prev_occupied_seat is None:
                    max_dist = max(max_dist, i)
                else:
                    max_dist = max(max_dist, (i - prev_occupied_seat) // 2)
                prev_occupied_seat = i
        max_dist = max(max_dist, len(seats) - 1 - prev_occupied_seat)
        return max_dist
