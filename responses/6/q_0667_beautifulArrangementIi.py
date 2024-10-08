class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        arr = [1] * n
        diff = k
        for i in range(1, k+1):
            if i % 2 == 1:
                arr[i] = arr[i-1] + diff
            else:
                arr[i] = arr[i-1] - diff
            diff -= 1
        for i in range(k+1, n):
            arr[i] = i + 1
        return arr
