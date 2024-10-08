class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        num_str = str(n)
        n_digits = len(num_str)
        split_idx = n_digits

        for i in range(n_digits - 1, 0, -1):
            if int(num_str[i]) < int(num_str[i-1]):
                split_idx = i
                num_str = num_str[:i-1] + str(int(num_str[i-1]) - 1) + '9' * (n_digits - i)

        return int(num_str)
