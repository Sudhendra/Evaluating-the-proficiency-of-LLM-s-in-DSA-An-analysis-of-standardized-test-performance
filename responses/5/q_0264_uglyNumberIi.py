class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        p2 = p3 = p5 = 0
        for _ in range(1, n):
            candidate = min(ugly[p2] * 2, ugly[p3] * 3, ugly[p5] * 5)
            ugly.append(candidate)
            if candidate == ugly[p2] * 2:
                p2 += 1
            if candidate == ugly[p3] * 3:
                p3 += 1
            if candidate == ugly[p5] * 5:
                p5 += 1
        return ugly[n - 1]