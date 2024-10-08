class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def one(num):
            return [
                "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
            ][num]

        def ten(num):
            return [
                "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
            ][num]

        def two(num):
            if not num:
                return ''
            elif num < 20:
                return one(num)
            else:
                return ten(num // 10) + (' ' + one(num % 10) if num % 10 else '')

        def three(num):
            hundred = num // 100
            rest = num % 100
            if rest == 0:
                return one(hundred) + " Hundred"
            else:
                return one(hundred) + " Hundred " + two(rest)

        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000

        result = ''
        if billion:
            result += three(billion) + " Billion"
        if million:
            if result: result += ' '
            result += three(million) + " Million"
        if thousand:
            if result: result += ' '
            result += three(thousand) + " Thousand"
        if rest:
            if result: result += ' '
            result += three(rest)

        return result
