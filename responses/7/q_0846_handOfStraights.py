from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counts = Counter(hand)
        
        while counts:
            min_elem = min(counts.keys())
            for i in range(min_elem, min_elem + groupSize):
                if i not in counts:
                    return False
                counts[i] -= 1
                if counts[i] == 0:
                    del counts[i]
        
        return True
