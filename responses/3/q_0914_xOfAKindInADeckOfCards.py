from collections import Counter
from math import gcd
from typing import List

class Solution:
    
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        n = len(deck)
        gcd_val = 0
        for val in count.values():
            gcd_val = gcd(gcd_val, val)
        return gcd_val >= 2