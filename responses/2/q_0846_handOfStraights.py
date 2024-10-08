from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counter = Counter(hand)
        
        for num in sorted(counter):
            if counter[num] > 0:
                for i in range(groupSize - 1, -1, -1):
                    if counter[num + i] < counter[num]:
                        return False
                    counter[num + i] -= counter[num]
        
        return True