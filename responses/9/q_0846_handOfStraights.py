from collections import Counter

class Solution:
    
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counts = Counter(hand)
        hand.sort()
        
        for card in hand:
            if counts[card] > 0:
                for i in range(groupSize):
                    if counts[card + i] == 0:
                        return False
                    counts[card + i] -= 1
        
        return True
