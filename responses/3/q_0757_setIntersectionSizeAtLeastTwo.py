class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        
        result = 0
        end1, end2 = -1, -1
        
        for start, end in intervals:
            if start > end1:
                result += 2
                end2 = end
                end1 = end - 1
            elif start > end2:
                result += 1
                end2 = end1
                end1 = end
        
        return result