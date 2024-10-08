class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def to_decimal(array):
            result = 0
            for i in range(len(array)):
                result += array[-i-1] * (-2) ** i
            return result

        def to_negabinary(num):
            if num == 0:
                return [0]
            result = []
            while num != 0:
                remainder = num % -2
                num = num // -2
                if remainder < 0:
                    remainder += 2
                    num += 1
                result.insert(0, remainder)
            return result

        sum_decimal = to_decimal(arr1) + to_decimal(arr2)
        sum_negabinary = to_negabinary(sum_decimal)

        return sum_negabinary
