class Solution:
    def binaryGap(self, n: int) -> int:
        binary_str = bin(n)[2:]  # Convert integer to binary string
        max_distance = 0
        prev_idx = None

        for idx, digit in enumerate(binary_str):
            if digit == '1':
                if prev_idx is not None:
                    distance = idx - prev_idx
                    max_distance = max(max_distance, distance)
                prev_idx = idx

        return max_distance
