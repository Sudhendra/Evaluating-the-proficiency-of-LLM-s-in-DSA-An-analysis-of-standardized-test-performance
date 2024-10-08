class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        
        total_duration = duration
        for i in range(1, len(timeSeries)):
            total_duration += min(duration, timeSeries[i] - timeSeries[i-1])
        
        return total_duration
