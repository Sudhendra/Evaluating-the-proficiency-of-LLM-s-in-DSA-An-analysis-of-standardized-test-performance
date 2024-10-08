from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change_available = {5: 0, 10: 0}

        for bill in bills:
            if bill == 5:
                change_available[5] += 1
            elif bill == 10:
                change_available[10] += 1
                if change_available[5] == 0:
                    return False
                change_available[5] -= 1
            else:  # bill == 20
                if change_available[10] >= 1 and change_available[5] >= 1:
                    change_available[10] -= 1
                    change_available[5] -= 1
                elif change_available[5] >= 3:
                    change_available[5] -= 3
                else:
                    return False

        return True
