from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        heaters = [float('-inf')] + heaters + [float('inf')]  # add dummy heaters at boundary
        radius = 0
        i = 0
        
        for house in houses:
            while house > heaters[i+1]:
                i += 1
            radius = max(radius, min(house - heaters[i], heaters[i+1] - house))
        
        return radius
