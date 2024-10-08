class Solution:
    def prevPermOpt1(self, arr):
        n = len(arr)
        i = n - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1
        if i == -1:
            return arr
        j = n - 1
        while arr[j] >= arr[i]:
            j -= 1
        while arr[j] == arr[j - 1]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
        return arr
