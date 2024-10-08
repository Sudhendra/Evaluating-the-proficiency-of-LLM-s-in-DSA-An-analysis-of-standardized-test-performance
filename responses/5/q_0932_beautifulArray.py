class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        def divide_conquer(nums):
            if len(nums) <= 1:
                return nums
            odds = divide_conquer([num * 2 - 1 for num in nums])
            evens = divide_conquer([num * 2 for num in nums])
            return odds + evens
        
        return divide_conquer(list(range(1, n + 1)))