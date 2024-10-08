from collections import Counter

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def request_condition(age1, age2):
            return not (age2 <= 0.5 * age1 + 7 or age2 > age1 or (age2 > 100 and age1 < 100))

        age_counts = Counter(ages)
        total_requests = 0

        for age1, count1 in age_counts.items():
            for age2, count2 in age_counts.items():
                if request_condition(age1, age2):
                    if age1 == age2:
                        total_requests += count1 * (count2 - 1)
                    else:
                        total_requests += count1 * count2

        return total_requests // 2  # Dividing by 2 to remove double counting

# Time complexity: O(n^2), where n is the number of ages
# Space complexity: O(n), where n is the number of ages
