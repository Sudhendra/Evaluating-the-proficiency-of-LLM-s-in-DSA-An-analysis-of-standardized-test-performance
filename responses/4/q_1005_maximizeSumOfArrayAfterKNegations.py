from heapq import heapify, heappush, heappop

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        i = 0
        while k > 0:
            if nums[i] == 0:
                break
            if nums[i] > 0:
                if k % 2 == 1:
                    if i > 0 and abs(nums[i-1]) < nums[i]:
                        nums[i-1] = -nums[i-1]
                    else:
                        nums[i] = -nums[i]
                break
            nums[i] = -nums[i]
            k -= 1
            i += 1
        return sum(nums)
