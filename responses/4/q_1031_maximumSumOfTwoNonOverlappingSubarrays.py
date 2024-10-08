from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)

        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        def max_sum_helper(A: List[int], L: int, M: int) -> int:
            res = 0
            max_L = [0] * (len(A) - L + 1)
            max_M = [0] * (len(A) - M + 1)

            for i in range(len(A) - L, -1, -1):
                max_L[i] = max(max_L[i + 1], sum(A[i:i + L]))

            for i in range(len(A) - M, -1, -1):
                max_M[i] = max(max_M[i + 1], sum(A[i:i + M]))

            for i in range(len(A) - L + 1):
                res = max(res, max_L[i] + max_M[i + L])

            return res

        return max(max_sum_helper(prefix_sum, firstLen, secondLen), max_sum_helper(prefix_sum, secondLen, firstLen))
