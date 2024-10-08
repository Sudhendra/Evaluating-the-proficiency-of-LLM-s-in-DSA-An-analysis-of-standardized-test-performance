class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        tests_per_pig = minutesToTest // minutesToDie + 1
        return math.ceil(math.log(buckets) / math.log(tests_per_pig))
