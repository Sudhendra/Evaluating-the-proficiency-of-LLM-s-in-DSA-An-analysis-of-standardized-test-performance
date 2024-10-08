from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand_dict = Counter(hand)
        hand.sort()

        for num in hand:
            if hand_dict[num] > 0:
                for i in range(groupSize):
                    if hand_dict[num + i] == 0:
                        return False
                    hand_dict[num + i] -= 1
        
        return True