from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        max_radius = 0
        i, j = 0, 0
        
        while i < len(houses):
            house = houses[i]
            while j < len(heaters) - 1 and abs(heaters[j+1] - house) <= abs(heaters[j] - house):
                j += 1
            max_radius = max(max_radius, abs(heaters[j] - house))
            i += 1
        
        return max_radius
