class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total_sum = sum(arr)
        if total_sum % 3 != 0:
            return False

        part_sum = total_sum // 3
        partition_count = 0
        curr_sum = 0

        for num in arr:
            curr_sum += num
            if curr_sum == part_sum:
                partition_count += 1
                curr_sum = 0

        return partition_count >= 3
