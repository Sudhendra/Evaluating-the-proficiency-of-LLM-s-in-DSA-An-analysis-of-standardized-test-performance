from collections import Counter

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def request_condition(age1, age2):
            return not (age2 <= 0.5 * age1 + 7 or age2 > age1 or (age2 > 100 and age1 < 100))

        counter = Counter(ages)
        total_requests = 0

        for age1, count1 in counter.items():
            for age2, count2 in counter.items():
                if request_condition(age1, age2):
                    if age1 == age2:
                        total_requests += count1 * (count2 - 1)
                    else:
                        total_requests += count1 * count2

        return total_requests // 2
