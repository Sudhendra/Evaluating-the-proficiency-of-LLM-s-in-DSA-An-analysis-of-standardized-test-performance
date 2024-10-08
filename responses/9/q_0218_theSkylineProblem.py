from typing import List
from sortedcontainers import SortedList

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = [(left, -height, right) for left, right, height in buildings] + [(right, 0, 0) for _, right, _ in buildings]
        events.sort()
        res = []
        live = SortedList([0])
        for pos, neg_height, right in events:
            if neg_height != 0:
                if -neg_height > live[-1]:
                    res.append([pos, -neg_height])
                live.add(-neg_height)
            else:
                live.remove(live.index(right))
                if right > live[-1]:
                    res.append([pos, live[-1]])
        return res
