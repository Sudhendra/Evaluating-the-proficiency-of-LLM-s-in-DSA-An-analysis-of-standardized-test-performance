from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        hand.sort()

        for num in hand:
            if count[num] == 0:
                continue

            for i in range(groupSize):
                if count[num + i] == 0:
                    return False
                count[num + i] -= 1

        return True
