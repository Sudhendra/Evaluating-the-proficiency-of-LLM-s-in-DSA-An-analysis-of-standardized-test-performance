class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def can_send_request(age1, age2):
            return not (age2 <= 0.5 * age1 + 7 or age2 > age1 or (age2 > 100 and age1 < 100))

        age_count = [0] * 121
        for age in ages:
            age_count[age] += 1

        total_requests = 0
        for age1 in range(1, 121):
            for age2 in range(1, 121):
                if can_send_request(age1, age2):
                    if age1 == age2:
                        total_requests += age_count[age1] * (age_count[age2] - 1)
                    else:
                        total_requests += age_count[age1] * age_count[age2]

        return total_requests