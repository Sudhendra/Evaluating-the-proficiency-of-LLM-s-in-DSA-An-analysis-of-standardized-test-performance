class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_index, odd_index = 0, 1
        result = [0] * len(nums)
        
        for num in nums:
            if num % 2 == 0:
                result[even_index] = num
                even_index += 2
            else:
                result[odd_index] = num
                odd_index += 2
                
        return result
