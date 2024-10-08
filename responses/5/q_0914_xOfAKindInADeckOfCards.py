from typing import List
from collections import Counter
from math import gcd

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        values = count.values()
        group_size = min(values)

        for size in range(2, group_size + 1):
            if all(val % size == 0 for val in values):
                return True

        return False
