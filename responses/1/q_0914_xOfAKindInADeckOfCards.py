from typing import List

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter
        from math import gcd
        
        counts = Counter(deck)
        x = counts.most_common()[0][1]
        
        for count in counts.values():
            x = gcd(x, count)
        
        return x >= 2
