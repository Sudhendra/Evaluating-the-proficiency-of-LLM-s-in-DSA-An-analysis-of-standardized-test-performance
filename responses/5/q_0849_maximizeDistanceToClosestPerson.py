from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_dist = 0
        empty_seats = [idx for idx, seat in enumerate(seats) if seat == 0]
        
        for i in range(len(empty_seats)):
            if i == 0 or i == len(empty_seats) - 1:
                dist = empty_seats[i] if i == 0 else len(seats) - 1 - empty_seats[i]
            else:
                dist = (empty_seats[i] - empty_seats[i-1]) // 2
            
            max_dist = max(max_dist, dist)
        
        return max_dist
