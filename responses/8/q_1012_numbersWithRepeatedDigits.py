class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        num_str = str(n + 1)
        num_len = len(num_str)
        total = 0

        for i in range(1, num_len):
            total += 9 * self.permutations(9, i - 1)

        visited = set()
        for i, digit in enumerate(num_str):
            for j in range(0 if i > 0 else 1, int(digit)):
                if j not in visited:
                    total += self.permutations(9 - i, num_len - i - 1)
            if int(digit) in visited:
                break
            visited.add(int(digit))

        return n - total

    def permutations(self, n, k):
        result = 1
        for i in range(k):
            result *= n - i
        return result
