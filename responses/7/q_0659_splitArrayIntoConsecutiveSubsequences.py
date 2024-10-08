from collections import Counter

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = Counter(nums)
        tails = Counter()

        for num in nums:
            if count[num] == 0:
                continue
            elif tails[num] > 0:
                tails[num] -= 1
                tails[num + 1] += 1
            elif count[num + 1] > 0 and count[num + 2] > 0:
                count[num + 1] -= 1
                count[num + 2] -= 1
                tails[num + 3] += 1
            else:
                return False
            count[num] -= 1

        return True
