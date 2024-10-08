class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = str(num)
        max_num_str = sorted(num_str, reverse=True)

        for i in range(len(num_str)):
            if num_str[i] != max_num_str[i]:
                max_num_str[i] = num_str[i]
                break

        return int(''.join(max_num_str))
