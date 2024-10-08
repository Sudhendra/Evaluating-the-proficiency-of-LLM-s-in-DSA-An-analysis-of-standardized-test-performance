class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dollars = {5: 0, 10: 0}

        for bill in bills:
            if bill == 5:
                dollars[5] += 1
            elif bill == 10:
                if not dollars[5]:
                    return False
                dollars[5] -= 1
                dollars[10] += 1
            else:
                if dollars[10] >= 1 and dollars[5] >= 1:
                    dollars[10] -= 1
                    dollars[5] -= 1
                elif dollars[5] >= 3:
                    dollars[5] -= 3
                else:
                    return False
        
        return True
