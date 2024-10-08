class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        less_than_20 = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                        'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen',
                        'Eighteen', 'Nineteen']
        tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        thousands = ['Thousand', 'Million', 'Billion']

        def helper(n):
            if n == 0:
                return []
            elif n < 20:
                return [less_than_20[n-1]]
            elif n < 100:
                return [tens[n//10-2]] + helper(n % 10)
            else:
                return [less_than_20[n//100-1]] + ['Hundred'] + helper(n % 100)

        parts = []
        for i, unit in enumerate(thousands):
            if num % 1000 != 0:
                parts = helper(num % 1000) + [unit] + parts
            num //= 1000

        return ' '.join(parts).strip() or 'Zero'