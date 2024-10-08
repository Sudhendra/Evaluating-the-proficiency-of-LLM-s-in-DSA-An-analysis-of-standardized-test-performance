class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_nums = [1]
        p2 = p3 = p5 = 0
        
        for _ in range(1, n):
            next_ugly = min(ugly_nums[p2] * 2, ugly_nums[p3] * 3, ugly_nums[p5] * 5)
            ugly_nums.append(next_ugly)
            
            if next_ugly == ugly_nums[p2] * 2:
                p2 += 1
            if next_ugly == ugly_nums[p3] * 3:
                p3 += 1
            if next_ugly == ugly_nums[p5] * 5:
                p5 += 1
        
        return ugly_nums[-1]