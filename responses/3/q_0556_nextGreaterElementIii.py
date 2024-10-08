class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n_list = list(str(n))
        i = len(n_list) - 2
        while i >= 0 and n_list[i] >= n_list[i+1]:
            i -= 1
        if i == -1:
            return -1
        j = len(n_list) - 1
        while j >= 0 and n_list[j] <= n_list[i]:
            j -= 1
        n_list[i], n_list[j] = n_list[j], n_list[i]
        n_list[i+1:] = n_list[i+1:][::-1]
        result = int("".join(n_list))
        return result if result < 2**31 - 1 else -1
