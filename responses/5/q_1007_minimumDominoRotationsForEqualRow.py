from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        target = tops[0]  # First domino top value
        swaps_top = 0  # Number of swaps needed if all dominoes have 'target' on top
        swaps_bottom = 0  # Number of swaps needed if all dominoes have 'target' on bottom
        swaps_top_bottom = 0  # Number of swaps needed if the first domino has 'target' on top, and all rest have 'target' on bottom
        swaps_bottom_top = 0  # Number of swaps needed if the first domino has 'target' on bottom, and all rest have 'target' on top
        
        for i in range(n):
            if tops[i] != target and bottoms[i] != target:
                break
            if tops[i] != target:
                swaps_top += 1
            if bottoms[i] != target:
                swaps_bottom += 1
            if tops[i] != target and bottoms[i] == target:
                swaps_top_bottom += 1
            if tops[i] == target and bottoms[i] != target:
                swaps_bottom_top += 1
        else:
            return min(swaps_top, swaps_bottom, swaps_top_bottom, swaps_bottom_top)

        target = bottoms[0]  # First domino bottom value
        swaps_top = 0
        swaps_bottom = 0
        swaps_top_bottom = 0
        swaps_bottom_top = 0
        
        for i in range(n):
            if tops[i] != target and bottoms[i] != target:
                break
            if tops[i] != target:
                swaps_top += 1
            if bottoms[i] != target:
                swaps_bottom += 1
            if tops[i] != target and bottoms[i] == target:
                swaps_top_bottom += 1
            if tops[i] == target and bottoms[i] != target:
                swaps_bottom_top += 1
        else:
            return min(swaps_top, swaps_bottom, swaps_top_bottom, swaps_bottom_top)

        return -1
