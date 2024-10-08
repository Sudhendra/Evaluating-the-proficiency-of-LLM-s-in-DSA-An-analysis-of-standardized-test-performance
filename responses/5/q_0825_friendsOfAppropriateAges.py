class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        from collections import Counter
        
        def can_send_request(age1, age2):
            if age2 <= 0.5 * age1 + 7:
                return False
            if age2 > age1:
                return False
            if age2 > 100 and age1 < 100:
                return False
            return True
        
        def count_friend_requests(age_counts):
            total_requests = 0
            for age1, count1 in age_counts.items():
                for age2, count2 in age_counts.items():
                    if can_send_request(age1, age2):
                        total_requests += count1 * (count2 - (1 if age1 == age2 else 0))
            return total_requests
        
        age_counts = Counter(ages)
        return count_friend_requests(age_counts)