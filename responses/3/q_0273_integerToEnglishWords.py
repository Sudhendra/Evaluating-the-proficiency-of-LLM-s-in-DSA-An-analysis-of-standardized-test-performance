class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def one(num):
            ones = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
            return ones[num - 1]

        def two_less_than_20(num):
            if num < 10:
                return one(num)
            teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
            return teens[num - 10]

        def ten(num):
            tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
            return tens[num - 2]

        def two(num):
            if num == 0:
                return ''
            elif num < 10:
                return one(num)
            elif num < 20:
                return two_less_than_20(num)
            else:
                tens = num // 10
                ones = num % 10
                return ten(tens) + ' ' + one(ones) if ones else ten(tens)

        def three(num):
            hundreds = num // 100
            rest = num % 100
            if hundreds and rest:
                return one(hundreds) + ' Hundred ' + two(rest)
            elif not hundreds and rest:
                return two(rest)
            elif hundreds and not rest:
                return one(hundreds) + ' Hundred'

        billion = num // 10**9
        million = (num % 10**9) // 10**6
        thousand = (num % 10**6) // 10**3
        rest = num % 10**3

        result = ''
        if billion:
            result += three(billion) + ' Billion '
        if million:
            result += three(million) + ' Million ' if result else three(million) + ' Million'
        if thousand:
            result += ' ' if result else ''
            result += three(thousand) + ' Thousand' if result else three(thousand) + ' Thousand'
        if rest:
            result += ' ' if result else ''
            result += three(rest)
        return result.strip()
