from collections import Counter

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        min_group_size = min(count.values())
        
        for x in range(2, min_group_size+1):
            if all(val % x == 0 for val in count.values()):
                return True
        
        return False
