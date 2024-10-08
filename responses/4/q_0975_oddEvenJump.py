from sortedcontainers import SortedDict

class Solution:
    def oddEvenJumps(self, arr):
        n = len(arr)
        next_higher, next_lower = [0] * n, [0] * n
        stack = []
        sorted_arr = SortedDict()
        for a in reversed(range(n)):
            sorted_arr[arr[a]] = a
            higher = sorted_arr.bisect_right(arr[a])
            lower = sorted_arr.bisect_left(arr[a])
            if higher != len(sorted_arr):
                next_higher[a] = sorted_arr[sorted_arr.iloc[higher]]
            if lower != 0:
                next_lower[a] = sorted_arr[sorted_arr.iloc[lower-1]]

        higher, lower = [0] * n, [0] * n
        higher[n-1] = lower[n-1] = 1
        for i in reversed(range(n-1)):
            if next_higher[i]:
                higher[i] = lower[next_higher[i]]
            if next_lower[i]:
                lower[i] = higher[next_lower[i]]

        return sum(higher)
