class Solution:
    def binaryGap(self, n: int) -> int:
        binary_rep = bin(n)[2:]
        max_dist = 0
        dist = 0
        found_one = False

        for bit in binary_rep:
            if bit == '1':
                if not found_one:
                    found_one = True
                else:
                    max_dist = max(max_dist, dist)
                dist = 1
            elif found_one:
                dist += 1

        return max_dist
