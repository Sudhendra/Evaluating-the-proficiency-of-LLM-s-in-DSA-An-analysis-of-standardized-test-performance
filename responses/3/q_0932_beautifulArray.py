class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        result = [1]
        while len(result) < n:
            result = [i*2-1 for i in result] + [i*2 for i in result]
        return [x for x in result if x <= n]
