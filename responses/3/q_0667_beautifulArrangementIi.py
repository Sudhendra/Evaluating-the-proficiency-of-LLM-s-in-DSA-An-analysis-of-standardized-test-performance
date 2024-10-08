class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        result = [1]
        for i in range(k):
            if i % 2 == 0:
                result.append(result[-1] + (k - i))
            else:
                result.append(result[-1] - (k - i))
        for i in range((n-k-1)):
            result.append(i + k + 2)
        return result