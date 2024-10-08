from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = defaultdict(int)
        
        for bill in bills:
            if bill == 5:
                money[5] += 1
            elif bill == 10:
                money[10] += 1
                if money[5] <= 0:
                    return False
                money[5] -= 1
            else:  # bill == 20
                if money[10] >= 1 and money[5] >= 1:
                    money[10] -= 1
                    money[5] -= 1
                elif money[5] >= 3:
                    money[5] -= 3
                else:
                    return False
        
        return True
