from collections import defaultdict

class Solution:
    def dist(self, p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        count = 0
        for p in points:
            d_dict = defaultdict(int)
            for q in points:
                distance = self.dist(p, q)
                d_dict[distance] += 1

            for dist_count in d_dict.values():
                count += dist_count * (dist_count - 1)  # Permutations of 2 from dist_count

        return count
