from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change_available = defaultdict(int)
        
        for bill in bills:
            change = bill - 5
            change_available[bill] += 1
            
            if change > 0:
                while change >= 20 and change_available[20] > 0:
                    change -= 20
                    change_available[20] -= 1
                
                while change >= 10 and change_available[10] > 0:
                    change -= 10
                    change_available[10] -= 1
                    
                while change >= 5 and change_available[5] > 0:
                    change -= 5
                    change_available[5] -= 1
            
            if change > 0:
                return False
        
        return True
