class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def less_than_thousand(n):
            ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
            teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
            tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

            result = ""
            if n >= 100:
                result += ones[n // 100] + " Hundred "
                n %= 100
            if n >= 20:
                result += tens[n // 10] + " "
                n %= 10
            if n >= 10:
                result += teens[n - 10]
                return result
            if n >= 1:
                result += ones[n]
            return result

        def helper(n):
            if n >= 10**9:
                return helper(n // 10**9) + " Billion " + helper(n % 10**9)
            elif n >= 10**6:
                return helper(n // 10**6) + " Million " + helper(n % 10**6)
            elif n >= 10**3:
                return helper(n // 10**3) + " Thousand " + helper(n % 10**3)
            else:
                return less_than_thousand(n)

        return helper(num).strip()
