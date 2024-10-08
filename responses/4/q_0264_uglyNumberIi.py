class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_nums = [1]
        idx2, idx3, idx5 = 0, 0, 0

        while len(ugly_nums) < n:
            next_ugly = min(ugly_nums[idx2] * 2, ugly_nums[idx3] * 3, ugly_nums[idx5] * 5)
            ugly_nums.append(next_ugly)

            if next_ugly == ugly_nums[idx2] * 2:
                idx2 += 1
            if next_ugly == ugly_nums[idx3] * 3:
                idx3 += 1
            if next_ugly == ugly_nums[idx5] * 5:
                idx5 += 1

        return ugly_nums[-1]
