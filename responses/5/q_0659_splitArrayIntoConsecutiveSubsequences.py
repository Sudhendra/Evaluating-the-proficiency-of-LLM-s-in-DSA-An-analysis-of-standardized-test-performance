from collections import Counter, defaultdict

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        left = Counter(nums)
        end = defaultdict(int)

        for num in nums:
            if left[num] == 0:
                continue
            left[num] -= 1
            if end[num - 1] > 0:
                end[num - 1] -= 1
                end[num] += 1
            elif left[num + 1] and left[num + 2]:
                left[num + 1] -= 1
                left[num + 2] -= 1
                end[num + 2] += 1
            else:
                return False

        return True
