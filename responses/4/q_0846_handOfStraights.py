from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        hand.sort()
        
        for card in hand:
            if count[card] > 0:
                for i in range(groupSize):
                    if count[card + i] == 0:
                        return False
                    count[card + i] -= 1
        
        return True
