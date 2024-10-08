from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand_count = Counter(hand)
        hand = sorted(hand)
        
        for card in hand:
            if hand_count[card] > 0:
                for i in range(groupSize):
                    if hand_count[card+i] == 0:
                        return False
                    hand_count[card+i] -= 1
        
        return True
