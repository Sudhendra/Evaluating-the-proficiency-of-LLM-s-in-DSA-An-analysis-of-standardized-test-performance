from collections import Counter

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        append_freq = Counter()
        last_element = Counter()

        for num in nums:
            if freq[num] == 0:
                continue
            elif append_freq[num] > 0:
                append_freq[num] -= 1
                append_freq[num + 1] += 1
            elif freq[num + 1] > 0 and freq[num + 2] > 0:
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                append_freq[num + 3] += 1
            else:
                return False

            freq[num] -= 1

        return True
