class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor_result = x ^ y
        hamming_dist = 0
        while xor_result:
            hamming_dist += xor_result & 1
            xor_result >>= 1
        return hamming_dist
