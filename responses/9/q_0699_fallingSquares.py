from sortedcontainers import SortedDict

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        intervals = [(left, left + side, side) for left, side in positions]
        max_heights = []  # to store the max height of the falling squares at each position
        height_map = SortedDict()  # to keep track of intervals and their heights
        
        max_height = 0
        for left, right, side in intervals:
            max_h = height_map.bisect_left(left)  # find largest element <= left
            for s, e, h in height_map.items(max_h):
                if s < right and e > left:
                    left = min(left, s)
                    right = max(right, e)
                    side = max(side, h)
            
            # update the intervals and heights
            for key in list(height_map.keys(left, right)):
                del height_map[key]
            height_map[left] = right, side
            max_height = max(max_height, side)
            max_heights.append(max_height)
        
        return max_heights
