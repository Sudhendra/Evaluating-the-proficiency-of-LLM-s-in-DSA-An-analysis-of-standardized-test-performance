from collections import Counter

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = Counter(arr)
        for num in sorted(arr, key=abs):
            if count[num] == 0:
                continue
            if count[2*num] == 0:
                return False
            count[num] -= 1
            count[2*num] -= 1
        return True
