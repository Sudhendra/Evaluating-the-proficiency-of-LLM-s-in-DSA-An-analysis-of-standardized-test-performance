class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        last_seen = {int(val): idx for idx, val in enumerate(num_str)}

        for i, digit in enumerate(num_str):
            for d in range(9, int(digit), -1):
                if d in last_seen and last_seen[d] > i:
                    num_str[i], num_str[last_seen[d]] = num_str[last_seen[d]], num_str[i]
                    return int("".join(num_str))

        return num
