from typing import List

class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def backtrack(start, path):
            if start == len(num) and len(path) >= 3:
                self.result = path[:]
                return True

            for i in range(start, len(num)):
                if len(path) < 2 or int(num[start:i+1]) == path[-2] + path[-1]:
                    if i > start and num[start] == '0':
                        continue
                    current = int(num[start:i+1])
                    if current > 2**31 - 1:
                        continue
                    path.append(current)
                    if backtrack(i+1, path):
                        return True
                    path.pop()

            return False

        self.result = []
        backtrack(0, [])
        return self.result

# Example usage
solution = Solution()
print(solution.splitIntoFibonacci("1101111"))  # Output: [11, 0, 11, 11]
print(solution.splitIntoFibonacci("112358130"))  # Output: []
print(solution.splitIntoFibonacci("0123"))  # Output: []
