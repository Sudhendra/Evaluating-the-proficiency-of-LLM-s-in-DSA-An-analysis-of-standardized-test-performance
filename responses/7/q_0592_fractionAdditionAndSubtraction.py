class Solution:
    def fractionAddition(self, expression: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def add_fractions(frac1, frac2):
            num1, den1 = frac1
            num2, den2 = frac2
            numerator = num1 * den2 + num2 * den1
            denominator = den1 * den2
            common = abs(gcd(numerator, denominator))
            return (numerator//common, denominator//common)

        fractions = []
        i = 0
        while i < len(expression):
            sign = -1 if expression[i] == '-' else 1
            if expression[i] in "+-":
                i += 1
            j = i
            while j < len(expression) and expression[j] != "+" and expression[j] != "-":
                j += 1
            num, den = map(int, expression[i:j].split("/"))
            fractions.append((sign * num, den))
            i = j
            
        ans = (0, 1)
        for frac in fractions:
            ans = add_fractions(ans, frac)
        
        return str(ans[0]) + '/' + str(ans[1])
