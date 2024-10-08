from sortedcontainers import SortedDict

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        next_higher, next_lower = [0] * n, [0] * n
        stack = []
        sorted_values = SortedDict()

        for a in sorted(range(n), key=lambda i: arr[i]):
            while stack and stack[-1] < a:
                next_higher[stack.pop()] = a
            stack.append(a)

        stack = []
        for a in sorted(range(n), key=lambda i: arr[i]):
            while stack and stack[-1] < a:
                next_lower[stack.pop()] = a
            stack.append(a)

        dp_odd, dp_even = [False] * n, [False] * n
        dp_odd[-1] = dp_even[-1] = True

        for i in range(n - 2, -1, -1):
            dp_odd[i] = dp_even[next_higher[i]]
            dp_even[i] = dp_odd[next_lower[i]]

        return sum(dp_odd)
