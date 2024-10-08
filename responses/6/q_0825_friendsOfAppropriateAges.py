from typing import List

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = [0] * 121
        for age in ages:
            count[age] += 1

        total_requests = 0
        for age_a, count_a in enumerate(count):
            for age_b, count_b in enumerate(count):
                if age_a * 0.5 + 7 >= age_b: continue
                if age_a < age_b: continue
                if age_a < 100 < age_b: continue
                total_requests += count_a * count_b
                if age_a == age_b:
                    total_requests -= count_a
        
        return total_requests
