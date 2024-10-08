from collections import Counter

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def friend_request(age1, age2):
            return age2 > 0.5 * age1 + 7 and age2 <= age1
        
        total_requests = 0
        age_counter = Counter(ages)
        
        for age1, count1 in age_counter.items():
            for age2, count2 in age_counter.items():
                if friend_request(age1, age2):
                    if age1 == age2:
                        total_requests += count1 * (count2 - 1)
                    else:
                        total_requests += count1 * count2
        
        return total_requests // 2
