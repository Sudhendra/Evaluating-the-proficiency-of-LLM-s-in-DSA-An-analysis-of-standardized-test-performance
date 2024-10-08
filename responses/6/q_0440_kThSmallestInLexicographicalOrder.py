class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        current = 1
        k -= 1

        while k > 0:
            steps = self.calculate_steps(n, current, current + 1)
            if steps <= k:
                current += 1
                k -= steps
            else:
                current *= 10
                k -= 1

        return current

    def calculate_steps(self, n, n1, n2):
        steps = 0
        while n1 <= n:
            steps += min(n + 1, n2) - n1
            n1 *= 10
            n2 *= 10
        return steps
