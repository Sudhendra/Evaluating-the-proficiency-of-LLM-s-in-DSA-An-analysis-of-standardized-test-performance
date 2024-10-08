class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = str(num)
        last_occurrence = {int(val): idx for idx, val in enumerate(num_str)}

        for idx, digit in enumerate(num_str):
            for d in range(9, int(digit), -1):
                if d in last_occurrence and last_occurrence[d] > idx:
                    num_list = list(num_str)
                    num_list[idx], num_list[last_occurrence[d]] = num_list[last_occurrence[d]], num_list[idx]
                    return int("".join(num_list))

        return num
