from collections import defaultdict
from typing import List

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        tail = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        for num in nums:
            if count[num] == 0:  # Skip if num has been used
                continue
            
            count[num] -= 1  # Mark num as used

            if tail[num - 1] > 0:
                tail[num - 1] -= 1
                tail[num] += 1
            elif count[num + 1] > 0 and count[num + 2] > 0:
                count[num + 1] -= 1
                count[num + 2] -= 1
                tail[num + 2] += 1
            else:
                return False
        
        return True