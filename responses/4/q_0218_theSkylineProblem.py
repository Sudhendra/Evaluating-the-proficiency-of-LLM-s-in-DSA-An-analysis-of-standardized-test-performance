from sortedcontainers import SortedDict
from sortedcontainers import SortedList
from itertools import chain

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = SortedDict()
        for left, right, height in buildings:
            events.setdefault(left, SortedList()).add(-height)
            events.setdefault(right, SortedList()).add(height)
        result = []
        active_heights = SortedList([0])
        for x, heights in events.items():
            for height in heights:
                if height < 0:
                    active_heights.add(-height)
                else:
                    active_heights.discard(height)
            max_height = -active_heights[0]
            if not result or max_height != result[-1][1]:
                result.append([x, max_height])
        return result
