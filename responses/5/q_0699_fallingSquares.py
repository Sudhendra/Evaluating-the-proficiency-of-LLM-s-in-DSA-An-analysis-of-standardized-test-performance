from sortedcontainers import SortedDict

class Solution:
    def fallingSquares(self, positions: List[List[int]) -> List[int]:
        intervals = SortedDict()
        intervals[0] = 0
        max_height = 0
        result = []

        for left, sideLength in positions:
            right = left + sideLength
            start_idx = intervals.bisect_left(left)
            end_idx = intervals.bisect_right(right)

            base_height = 0
            for i in range(start_idx, end_idx):
                base_height = max(base_height, intervals.iloc[i - 1])

            new_height = base_height + sideLength
            for key in list(intervals.keys())[start_idx:end_idx]:
                if intervals[key] < new_height:
                    intervals[key] = new_height

            intervals[left] = base_height
            intervals[right] = base_height

            max_height = max(max_height, new_height)
            result.append(max_height)

        return result
