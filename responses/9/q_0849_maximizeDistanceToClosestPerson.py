from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_distance = 0
        prev_person = -1
        n = len(seats)

        for i in range(n):
            if seats[i] == 1:
                if prev_person == -1:
                    max_distance = max(max_distance, i)
                else:
                    max_distance = max(max_distance, (i - prev_person) // 2)
                prev_person = i

        # Check the distance to the last seat
        max_distance = max(max_distance, n - 1 - prev_person)

        return max_distance
