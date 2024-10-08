from collections import Counter

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def send_request(a, b):
            return not (b <= 0.5 * a + 7 or b > a or (b > 100 and a < 100))
        
        counter = Counter(ages)
        total_requests = 0
        for age_a, count_a in counter.items():
            for age_b, count_b in counter.items():
                if send_request(age_a, age_b):
                    total_requests += count_a * (count_b - (age_a == age_b))
        
        return total_requests
