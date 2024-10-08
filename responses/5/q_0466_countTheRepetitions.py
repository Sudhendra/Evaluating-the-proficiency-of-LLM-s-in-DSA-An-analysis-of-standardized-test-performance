class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if not set(s2).issubset(set(s1)):
            return 0

        s1_times = 0
        s2_times = 0
        pos_map = dict()
        while s1_times < n1:
            for char in s1:
                if char == s2[s2_times % len(s2)]:
                    s2_times += 1
            s1_times += 1

            if s2_times % len(s2) in pos_map:
                prev_s1_times, prev_s2_times = pos_map[s2_times % len(s2)]
                interval_s1_times = s1_times - prev_s1_times
                interval_s2_times = s2_times - prev_s2_times
                remaining_s1_times = (n1 - s1_times) % interval_s1_times
                s2_times = prev_s2_times + remaining_s1_times * (interval_s2_times // interval_s1_times)
                break
            else:
                pos_map[s2_times % len(s2)] = (s1_times, s2_times)

        return s2_times // len(s2) // n2