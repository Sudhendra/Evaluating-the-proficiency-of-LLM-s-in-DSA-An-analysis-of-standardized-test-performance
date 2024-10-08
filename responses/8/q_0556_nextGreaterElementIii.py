class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n_str = list(str(n))
        i = len(n_str) - 2
        while i >= 0 and n_str[i] >= n_str[i + 1]:
            i -= 1
        if i == -1:
            return -1
        j = len(n_str) - 1
        while j > i and n_str[j] <= n_str[i]:
            j -= 1
        n_str[i], n_str[j] = n_str[j], n_str[i]
        n_str[i+1:] = reversed(n_str[i+1:])
        result = int(''.join(n_str))
        return result if result < 2**31 else -1
