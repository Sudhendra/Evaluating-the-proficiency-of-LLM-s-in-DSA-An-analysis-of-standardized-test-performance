class Solution:
    def insert(self, intervals: List[List[int], newInterval: List[int]) -> List[List[int]]:
        merged = []
        insert_pos = 0
        for interval in intervals:
            if interval[1] < newInterval[0]:
                merged.append(interval)
                insert_pos += 1
            elif interval[0] > newInterval[1]:
                merged.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        merged.insert(insert_pos, newInterval)
        return merged