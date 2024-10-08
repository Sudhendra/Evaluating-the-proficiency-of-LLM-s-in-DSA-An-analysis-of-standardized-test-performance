from sortedcontainers import SortedDict

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        next_higher = [0] * n
        next_lower = [0] * n
        stack = []
        sorted_arr = SortedDict()

        for num, i in sorted(zip(arr, range(n))):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)

        stack = []
        for num, i in sorted(zip(arr, range(n)), reverse=True):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        odd_jump = [False] * n
        even_jump = [False] * n
        odd_jump[-1] = even_jump[-1] = True
        count = 1

        for i in range(n - 1)[::-1]:
            if next_higher[i]:
                odd_jump[i] = even_jump[next_higher[i]]
            if next_lower[i]:
                even_jump[i] = odd_jump[next_lower[i]]
            if odd_jump[i]:
                count += 1

        return count
