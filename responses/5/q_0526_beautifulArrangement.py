class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(index, arrangement):
            nonlocal count
            if index == n + 1:
                count += 1
                return
            for i in range(1, n + 1):
                if i not in arrangement and (i % index == 0 or index % i == 0):
                    arrangement.append(i)
                    backtrack(index + 1, arrangement)
                    arrangement.pop()

        count = 0
        backtrack(1, [])
        return count
