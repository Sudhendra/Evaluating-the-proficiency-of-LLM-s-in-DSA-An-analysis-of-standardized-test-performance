class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        bad = [0] * n

        for i in range(n):
            left = (i - nums[i] + 1) % n
            right = (i + 1) % n
            bad[left] -= 1
            bad[right] += 1
            if left > right:
                bad[0] -= 1

        best = -n
        ans = 0
        cur = 0
        for i in range(n):
            cur += bad[i]
            if cur > best:
                best = cur
                ans = i

        return ans