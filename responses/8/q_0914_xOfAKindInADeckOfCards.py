from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        gcd = 0
        for val in count.values():
            gcd = math.gcd(gcd, val)
        return gcd > 1
