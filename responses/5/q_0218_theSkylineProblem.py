from sortedcontainers import SortedDict
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = [] # store all the left and right edges of the buildings
        for left, right, height in buildings:
            events.append((left, -height)) # negative height for left edge
            events.append((right, height)) # positive height for right edge
        events.sort(key=lambda x: (x[0], x[1])) # sort events based on x coordinate and then by height

        result = [] # result skyline
        prev_height = 0
        active_heights = SortedDict({0: 1}) # heights of active buildings: key is height, value is count of buildings with that height

        for x, h in events:
            if h < 0:
                active_heights[-h] = active_heights.get(-h, 0) + 1
            else:
                active_heights[h] -= 1
                if active_heights[h] == 0:
                    del active_heights[h]

            current_max_height = active_heights.iloc[-1] if active_heights else 0
            if current_max_height != prev_height:
                result.append([x, current_max_height])
                prev_height = current_max_height

        return result
