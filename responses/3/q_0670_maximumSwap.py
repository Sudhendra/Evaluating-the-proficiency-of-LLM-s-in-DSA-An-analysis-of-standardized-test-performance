class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [int(x) for x in str(num)]
        last_positions = {digit: i for i, digit in enumerate(digits)}

        for i, digit in enumerate(digits):
            for d in range(9, digit, -1):
                if d in last_positions and last_positions[d] > i:
                    digits[i], digits[last_positions[d]] = digits[last_positions[d]], digits[i]
                    return int("".join(map(str, digits)))

        return num