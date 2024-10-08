from sortedcontainers import SortedDict
from typing import List

class Solution:
    def fallingSquares(self, positions: List[List[int]) -> List[int]:
        intervals = SortedDict({0: 0})
        max_height = 0
        res = []

        for left, side_length in positions:
            right = left + side_length
            start_index = intervals.bisect_left(left)
            end_index = intervals.bisect_right(right)

            max_height = max(intervals.iloc[start_index:end_index].values()) + side_length
            intervals[left] = max_height
            intervals[right] = max(intervals[right], max_height)

            res.append(max(intervals.values()))

        return res
