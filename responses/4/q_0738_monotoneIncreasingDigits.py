class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        num_str = list(str(n))
        i = 1
        while i < len(num_str) and num_str[i - 1] <= num_str[i]:
            i += 1
        while i > 0 and i < len(num_str) and num_str[i - 1] > num_str[i]:
            num_str[i - 1] = str(int(num_str[i - 1]) - 1)
            i -= 1
        num_str[i + 1:] = '9' * (len(num_str) - i - 1)
        return int("".join(num_str))
