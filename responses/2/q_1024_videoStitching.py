class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key=lambda x: (x[0], -x[1]))

        if clips[0][0] > 0 or clips[-1][1] < time:
            return -1

        end_time = 0
        max_end_time = 0
        count = 0

        for clip in clips:
            start, end = clip
            if start > end_time:
                return -1
            if start > max_end_time:
                count += 1
                max_end_time = end_time
            end_time = max(end_time, end)

            if end_time >= time:
                return count

        return -1
