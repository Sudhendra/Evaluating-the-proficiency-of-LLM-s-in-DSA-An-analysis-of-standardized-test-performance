from heapq import heappush, heappop

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly_nums = [1]
        pq = [(prime, 0, prime) for prime in primes]  # (current value, index in ugly_nums, prime)
        while len(ugly_nums) < n:
            val, idx, prime = heappop(pq)
            if val > ugly_nums[-1]:
                ugly_nums.append(val)
            heappush(pq, (prime * ugly_nums[idx], idx+1, prime))
        return ugly_nums[-1]