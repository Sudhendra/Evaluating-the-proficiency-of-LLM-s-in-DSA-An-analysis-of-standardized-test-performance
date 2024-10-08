class Solution:
    
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        heaters = [float('-inf')] + heaters + [float('inf')]
        res, i = 0, 0
        
        for house in houses:
            while house > heaters[i + 1]:
                i += 1
            dis = min(house - heaters[i], heaters[i + 1] - house)
            res = max(res, dis)
        
        return res
