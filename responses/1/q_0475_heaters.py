from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        max_radius = 0
        
        i, j = 0, 0
        while i < len(houses):
            while j < len(heaters) - 1 and abs(houses[i] - heaters[j]) >= abs(houses[i] - heaters[j + 1]):
                j += 1
            max_radius = max(max_radius, abs(houses[i] - heaters[j]))
            i += 1
        
        return max_radius