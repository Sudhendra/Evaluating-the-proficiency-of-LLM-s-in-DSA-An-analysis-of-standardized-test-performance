from sortedcontainers import SortedDict

class Solution:
    def fallingSquares(self, positions: List[List[int]) -> List[int]:
        intervals = SortedDict()
        intervals[0] = 0
        result = []
        max_height = 0

        for position in positions:
            left, side_length = position
            right = left + side_length
            start_height = 0

            for start, end in intervals.items():
                if left < end and right > start:
                    start_height = max(start_height, end)

            new_height = start_height + side_length
            intervals[left] = max(intervals.bisect_left(left), start_height)
            intervals[right] = max(intervals.bisect_left(right), new_height)

            for key in list(intervals.keys()):
                if left < key < right:
                    intervals[key] = new_height

            max_height = max(max_height, new_height)
            result.append(max_height)

        return result
