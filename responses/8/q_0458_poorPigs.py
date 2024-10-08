from math import ceil

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        tests_per_pig = minutesToTest // minutesToDie + 1
        pigs_needed = ceil(log(buckets) / log(tests_per_pig))
        return pigs_needed
