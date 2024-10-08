class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        num = n + 1
        digits = list(map(int, str(num)))
        total_length = len(digits)

        def count_missing_non_repeated(d, remaining):
            if remaining == 0:
                return 1
            if d == 0:
                return 0
            return count_missing_non_repeated(d - 1, remaining - 1) * (10 - remaining + 1)

        def count_valid_non_repeated(num_str):
            total = 0
            length = len(num_str)
            for i in range(1, length):
                total += 9 * permute(9, i - 1)

            seen = set()
            for i, digit in enumerate(num_str):
                for x in range(0 if i else 1, int(digit)):
                    if x not in seen:
                        total += count_missing_non_repeated(9 - i, total_length - length)
                if digit in seen:
                    break
                seen.add(int(digit))

            return total

        result = num - 1
        for i in range(2, total_length):
            result -= permute(9, i - 1) * 9

        return result - count_valid_non_repeated(str(n))