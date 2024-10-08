class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = ""
        if (numerator < 0) ^ (denominator < 0):
            result += "-"

        numerator, denominator = abs(numerator), abs(denominator)
        result += str(numerator // denominator)

        remainder = numerator % denominator
        if remainder == 0:
            return result

        result += "."

        rem_dict = {}
        while remainder != 0:
            if remainder in rem_dict:
                result = result[:rem_dict[remainder]] + "(" + result[rem_dict[remainder]:] + ")"
                break

            rem_dict[remainder] = len(result)
            remainder *= 10
            result += str(remainder // denominator)
            remainder %= denominator

        return result
