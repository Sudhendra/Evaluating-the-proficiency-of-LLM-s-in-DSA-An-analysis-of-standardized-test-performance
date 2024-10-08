from typing import List

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        curr_end = 0
        max_end = 0
        clip_count = 0
        
        for start, end in clips:
            if start > curr_end:
                return -1
            if end > max_end:
                clip_count += 1
                curr_end = max_end
            if end >= time:
                return clip_count
            max_end = max(max_end, end)
        
        return -1
