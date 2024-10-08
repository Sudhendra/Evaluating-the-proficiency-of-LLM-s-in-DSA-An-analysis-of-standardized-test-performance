from collections import Counter

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        freq_tops = Counter(tops)
        freq_bottoms = Counter(bottoms)
        same = set([tops[0], bottoms[0]])
        
        for i in range(1, n):
            same.intersection_update([tops[i], bottoms[i]])
        
        if not same:
            return -1
        
        target = same.pop()
        return min(n - freq_tops[target], n - freq_bottoms[target])