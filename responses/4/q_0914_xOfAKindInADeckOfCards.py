from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counts = Counter(deck)
        gcd = counts[deck[0]]
        for num in counts.values():
            gcd = self.calculate_gcd(gcd, num)
            if gcd == 1:
                return False
        return True
    
    def calculate_gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
