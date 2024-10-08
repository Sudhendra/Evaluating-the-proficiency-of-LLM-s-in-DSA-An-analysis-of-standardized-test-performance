from collections import Counter

class Solution:
    
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = Counter(arr)
        for num in sorted(count, key=abs):
            if count[num] > count[2*num]:
                return False
            count[2*num] -= count[num]
        return True
