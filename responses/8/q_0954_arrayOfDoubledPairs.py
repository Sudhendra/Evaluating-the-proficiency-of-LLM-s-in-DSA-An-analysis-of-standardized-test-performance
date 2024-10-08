from collections import Counter

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        for num in sorted(arr, key=abs):
            if counter[num] == 0:
                continue
            if counter[2*num] == 0:
                return False
            counter[num] -= 1
            counter[2*num] -= 1
        return True
