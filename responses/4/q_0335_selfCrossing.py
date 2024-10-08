from typing import List

class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        if len(distance) < 4:
            return False

        for i in range(3, len(distance)):
            # Case 1: Fourth line crosses first line
            if i >= 3 and distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]:
                return True

            # Case 2: Fifth line overlaps with first line
            if i >= 4 and distance[i - 1] == distance[i - 3] and distance[i] + distance[i - 4] >= distance[i - 2]:
                return True

            # Case 3: Sixth line crosses first line
            if i >= 5 and distance[i - 2] >= distance[i - 4] and distance[i] + distance[i - 4] >= distance[i - 2] and distance[i - 1] <= distance[i - 3] and distance[i - 1] + distance[i - 5] >= distance[i - 3]:
                return True

        return False
