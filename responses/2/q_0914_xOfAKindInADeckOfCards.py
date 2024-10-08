from collections import Counter
from math import gcd
from typing import List

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        x = 0
        for val in count.values():
            x = gcd(x, val)
            if x == 1:
                return False
        return True
