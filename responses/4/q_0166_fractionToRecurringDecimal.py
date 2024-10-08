class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []
        # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        # Convert to positive absolute values
        num = abs(numerator)
        den = abs(denominator)

        # Append integer part
        result.append(str(num // den))

        remainder = num % den
        if remainder == 0:
            return "".join(result)

        result.append(".")
        index_map = {}
        while remainder != 0:
            if remainder in index_map:
                result.insert(index_map[remainder], "(")
                result.append(")")
                break
            index_map[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder // den))
            remainder %= den

        return "".join(result)
