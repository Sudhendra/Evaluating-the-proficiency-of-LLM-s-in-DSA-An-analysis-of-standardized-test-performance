class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        last_occurrence = {int(num_str[i]): i for i in range(len(num_str))}

        for i in range(len(num_str)):
            for d in range(9, int(num_str[i]), -1):
                if d in last_occurrence and last_occurrence[d] > i:
                    num_str[i], num_str[last_occurrence[d]] = num_str[last_occurrence[d]], num_str[i]
                    return int("".join(num_str))

        return num
