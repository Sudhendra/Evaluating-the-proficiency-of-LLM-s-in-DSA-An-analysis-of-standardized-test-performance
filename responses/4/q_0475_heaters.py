from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        max_radius = 0

        i, j = 0, 0
        while i < len(houses):
            while j < len(heaters) - 1 and abs(heaters[j + 1] - houses[i]) <= abs(heaters[j] - houses[i]):
                j += 1
            max_radius = max(max_radius, abs(heaters[j] - houses[i]))
            i += 1

        return max_radius
