from sortedcontainers import SortedDict

class Solution:
    def fallingSquares(self, positions: List[List[int]) -> List[int]:
        intervals = SortedDict()
        intervals[0] = 0
        result = []
        max_height = 0
        
        for left, side_length in positions:
            right = left + side_length
            # Find the intersecting intervals and update the heights
            curr_height = intervals.bisect_left(left)
            for start, end in intervals.items(left, right):
                curr_height = max(curr_height, end)
                
            intervals[left] = curr_height + side_length
            intervals[right] = curr_height
            
            # Update max height
            max_height = max(max_height, curr_height + side_length)
            result.append(max_height)
        
        return result
