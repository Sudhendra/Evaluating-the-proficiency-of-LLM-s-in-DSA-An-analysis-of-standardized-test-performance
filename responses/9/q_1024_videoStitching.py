from typing import List

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        n = len(clips)
        dp = [float('inf')] * (time + 1)
        dp[0] = 0

        for i in range(n):
            start, end = clips[i]
            for j in range(start, min(end, time) + 1):
                dp[j] = min(dp[j], dp[start] + 1)

        return dp[time] if dp[time] != float('inf') else -1
