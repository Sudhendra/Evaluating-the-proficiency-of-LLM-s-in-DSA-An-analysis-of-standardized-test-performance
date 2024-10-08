from sortedcontainers import SortedDict

class Solution:
    def fallingSquares(self, positions: List[List[int]) -> List[int]:
        events = []
        for left, side_length in positions:
            right = left + side_length
            events.append((left, right, side_length))
            events.append((right, 0, 0))
        
        intervals = SortedDict()
        intervals[0] = 0
        max_height = 0
        result = []
        for left, right, side_length in events:
            height = intervals.bisect_left(left)
            for start, end in list(intervals.items(left, right)):
                height = max(height, end)
            new_height = height + side_length
            intervals[left] = new_height
            intervals[right] = height
            max_height = max(max_height, new_height)
            result.append(max_height)
        
        return result
