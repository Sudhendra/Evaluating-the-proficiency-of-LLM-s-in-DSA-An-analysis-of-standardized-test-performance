class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        max_dist = 0
        prev = None
        for i in range(len(binary)):
            if binary[i] == '1':
                if prev is not None:
                    max_dist = max(max_dist, i - prev)
                prev = i
        return max_dist