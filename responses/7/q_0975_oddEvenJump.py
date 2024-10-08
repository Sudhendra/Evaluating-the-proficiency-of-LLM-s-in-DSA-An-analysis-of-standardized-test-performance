class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        def next_higher_index(arr, indices):
            stack = []
            result = [0] * len(arr)
            for index in indices:
                while stack and stack[-1] < index:
                    result[stack.pop()] = index
                stack.append(index)
            return result

        def next_lower_index(arr, indices):
            stack = []
            result = [0] * len(arr)
            for index in indices:
                while stack and stack[-1] < index:
                    result[stack.pop()] = index
                stack.append(index)
            return result

        n = len(arr)
        odd_next_higher = next_higher_index(arr, sorted(range(n), key=lambda x: (arr[x], x)))
        even_next_lower = next_lower_index(arr, sorted(range(n), key=lambda x: (-arr[x], x)))

        odd_dp = [False] * n
        even_dp = [False] * n
        odd_dp[-1] = even_dp[-1] = True
        res = 1

        for i in range(n - 2, -1, -1):
            if odd_next_higher[i]:
                odd_dp[i] = even_dp[odd_next_higher[i]]
            if even_next_lower[i]:
                even_dp[i] = odd_dp[even_next_lower[i]]

            res += odd_dp[i]

        return res
