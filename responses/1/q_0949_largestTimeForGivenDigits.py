from typing import List

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        max_time = ""
        
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    if i == j or j == k or k == i:
                        continue
                    hour = str(arr[i]) + str(arr[j])
                    minute = str(arr[k]) + str(arr[6 - i - j - k])
                    time = hour + ":" + minute
                    if hour < "24" and minute < "60" and time > max_time:
                        max_time = time
        
        return max_time
