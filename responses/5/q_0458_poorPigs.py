class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        tests_per_pig = minutesToTest // minutesToDie + 1
        num_pigs = 0
        while (tests_per_pig ** num_pigs) < buckets:
            num_pigs += 1
        return num_pigs
