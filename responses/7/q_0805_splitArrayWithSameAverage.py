from typing import List

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        def possible(A, B, total, length):
            if length == 0:
                return total == 0
            if total < length * A[0] or total > length * A[-1]:
                return False

            for i, num in enumerate(A):
                if i > 0 and A[i] == A[i-1]:
                    continue
                if possible(A[i+1:], B, total - num, length - 1):
                    return True

            for i, num in enumerate(B):
                if i > 0 and B[i] == B[i-1]:
                    continue
                if possible(A, B[i+1:], total - num, length - 1):
                    return True

            return False

        n = len(nums)
        nums.sort()
        total = sum(nums)

        for lengthA in range(1, n // 2 + 1):
            if total * lengthA % n == 0:
                if possible(nums, nums, total * lengthA // n, lengthA):
                    return True

        return False
