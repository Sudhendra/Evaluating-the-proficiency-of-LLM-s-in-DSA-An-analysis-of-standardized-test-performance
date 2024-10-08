class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def request_condition(age_x, age_y):
            if age_y <= 0.5 * age_x + 7 or age_y > age_x or (age_y > 100 and age_x < 100):
                return False
            return True

        age_count = [0] * 121
        for age in ages:
            age_count[age] += 1

        total_requests = 0
        for age_x in range(1, 121):
            for age_y in range(1, 121):
                if request_condition(age_x, age_y):
                    if age_x == age_y:
                        total_requests += age_count[age_x] * (age_count[age_y] - 1)
                    else:
                        total_requests += age_count[age_x] * age_count[age_y]

        return total_requests
