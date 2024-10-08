from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_distance = 0
        prev_seat = None
        start_idx = None

        for i, seat in enumerate(seats):
            if seat == 1:
                if prev_seat is None:
                    max_distance = max(max_distance, i)
                else:
                    max_distance = max(max_distance, (i - start_idx) // 2)
                prev_seat = i
                start_idx = i
            elif i == len(seats) - 1:
                max_distance = max(max_distance, i - start_idx)

        return max_distance
