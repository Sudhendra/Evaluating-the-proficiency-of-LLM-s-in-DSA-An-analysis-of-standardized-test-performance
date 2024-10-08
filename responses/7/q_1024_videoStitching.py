from typing import List

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key=lambda x: (x[0], -x[1]))
        curr_end = count = 0
        new_end = -1
        
        for start, end in clips:
            if new_end >= time or start > new_end:
                break
            if start > curr_end:
                count += 1
                curr_end = new_end
            new_end = max(new_end, end)
        
        return count if new_end >= time else -1
