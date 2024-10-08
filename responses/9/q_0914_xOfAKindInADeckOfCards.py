from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        min_count = min(count.values())
        if min_count < 2:
            return False
        for x in range(2, min_count + 1):
            if all(val % x == 0 for val in count.values()):
                return True
        return False
