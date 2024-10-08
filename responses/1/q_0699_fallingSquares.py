from sortedcontainers import SortedDict

class Solution:
    def fallingSquares(self, positions: List[List[int]) -> List[int]:
        intervals = [(left, left + sideLength, sideLength) for left, sideLength in positions]
        result = []
        maxHeight = 0
        heights = SortedDict({0: 0})

        for start, end, height in intervals:
            left = heights.bisect_right(start)
            right = heights.bisect_left(end)

            max_height = 0
            for h in heights.values()[left:right]:
                max_height = max(max_height, h)
            max_height += height

            for key in list(heights.irange_key(start, end)):
                del heights[key]
            heights[start] = max_height
            heights[end] = heights.peekitem()[1]

            maxHeight = max(maxHeight, max_height)
            result.append(maxHeight)

        return result
