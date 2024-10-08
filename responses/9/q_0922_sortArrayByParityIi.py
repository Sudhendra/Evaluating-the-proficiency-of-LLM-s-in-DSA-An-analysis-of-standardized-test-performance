class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        odd_index, even_index = 1, 0
        result = [0] * n
        
        for num in nums:
            if num % 2 == 0:
                result[even_index] = num
                even_index += 2
            else:
                result[odd_index] = num
                odd_index += 2
        
        return result
