class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum_so_far = 0
        sum_count = {0: 1}

        for num in nums:
            sum_so_far += num
            if sum_so_far - k in sum_count:
                count += sum_count[sum_so_far - k]
            if sum_so_far in sum_count:
                sum_count[sum_so_far] += 1
            else:
                sum_count[sum_so_far] = 1

        return count
