class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        last_idx = {int(val): idx for idx, val in enumerate(num_str)}

        for idx, val in enumerate(num_str):
            for digit in range(9, int(val), -1):
                if digit in last_idx and idx < last_idx[digit]:
                    num_str[idx], num_str[last_idx[digit]] = num_str[last_idx[digit], num_str[idx]
                    return int("".join(num_str))
        return num
