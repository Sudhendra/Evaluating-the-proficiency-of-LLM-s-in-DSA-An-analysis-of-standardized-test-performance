from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        modulo_dict = {0: 1}

        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            count += modulo_dict.get(prefix_sum, 0)
            modulo_dict[prefix_sum] = modulo_dict.get(prefix_sum, 0) + 1

        return count
