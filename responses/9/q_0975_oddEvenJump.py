from sortedcontainers import SortedDict

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        next_higher, next_lower = [0] * n, [0] * n
        stack = []
        sorted_arr = SortedDict()

        for a, i in sorted([(a, i) for i, a in enumerate(arr)]):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)

        stack.clear()

        for a, i in sorted([(-a, i) for i, a in enumerate(arr)]):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        odd_jump, even_jump = [0] * n, [0] * n
        odd_jump[n - 1] = even_jump[n - 1] = 1

        for i in range(n - 2, -1, -1):
            odd_jump[i] = even_jump[next_higher[i]]
            even_jump[i] = odd_jump[next_lower[i]]

        return sum(odd_jump)
