class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        def max_sum(arr_len):
            max_sum_result = 0
            max_first_sum = 0
            for i in range(arr_len, len(prefix_sum)):
                max_first_sum = max(max_first_sum, prefix_sum[i-arr_len] - prefix_sum[i-arr_len-arr_len])
                max_sum_result = max(max_sum_result, max_first_sum + prefix_sum[i] - prefix_sum[i-arr_len])
            return max_sum_result

        return max(max_sum(firstLen), max_sum(secondLen))
