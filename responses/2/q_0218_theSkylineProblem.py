from sortedcontainers import SortedDict

class Solution:
    def getSkyline(self, buildings):
        events = []
        for left, right, height in buildings:
            events.append((left, -height))  # entering event
            events.append((right, height))  # leaving event
        events.sort()

        result = []
        active_heights = SortedDict({0: 1})  # height -> count mapping
        prev_max_height = 0

        for pos, height in events:
            height = abs(height)
            if height < 0:  # entering event
                active_heights[-height] = active_heights.get(-height, 0) + 1
            else:  # leaving event
                if active_heights[-height] == 1:
                    del active_heights[-height]
                else:
                    active_heights[-height] -= 1
            
            curr_max_height = active_heights.peekitem(-1)[0] if active_heights else 0
            if curr_max_height != prev_max_height:
                result.append([pos, curr_max_height])
                prev_max_height = curr_max_height
        
        return result
