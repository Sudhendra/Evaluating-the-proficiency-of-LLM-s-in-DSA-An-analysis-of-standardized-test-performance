class Solution:
    
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        heaters = [float('-inf')] + heaters + [float('inf')]
        radius = 0
        i = 0
        
        for house in houses:
            while house > heaters[i+1]:
                i += 1
            radius = max(radius, min(house - heaters[i], heaters[i+1] - house))
        
        return radius
