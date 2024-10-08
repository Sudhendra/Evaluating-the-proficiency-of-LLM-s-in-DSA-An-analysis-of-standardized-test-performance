class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return n
        
        higher, lower = [0] * n, [0] * n
        stack = []
        for a, i in sorted((a, i) for i, a in enumerate(arr)):
            while stack and stack[-1] < i:
                lower[stack.pop()] = i
            stack.append(i)
        
        stack = []
        for a, i in sorted((-a, i) for i, a in enumerate(arr)):
            while stack and stack[-1] < i:
                higher[stack.pop()] = i
            stack.append(i)
        
        odd, even = [0] * n, [0] * n
        odd[-1] = even[-1] = 1
        
        for i in range(n - 2, -1, -1):
            odd[i] = even[lower[i]]
            even[i] = odd[higher[i]]
        
        return sum(odd)