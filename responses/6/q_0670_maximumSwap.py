class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [int(d) for d in str(num)]
        last_occurrence = {digit: i for i, digit in enumerate(digits)}
        
        for i, digit in enumerate(digits):
            for replacement in range(9, digit, -1):
                if replacement in last_occurrence and last_occurrence[replacement] > i:
                    digits[i], digits[last_occurrence[replacement]] = digits[last_occurrence[replacement]], digits[i]
                    return int("".join(map(str, digits)))

        return num
