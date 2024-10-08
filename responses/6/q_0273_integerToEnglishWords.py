class Solution:

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def one(num):
            if num == 0:
                return ''
            elif num == 1:
                return 'One '
            elif num == 2:
                return 'Two '
            elif num == 3:
                return 'Three '
            elif num == 4:
                return 'Four '
            elif num == 5:
                return 'Five '
            elif num == 6:
                return 'Six '
            elif num == 7:
                return 'Seven '
            elif num == 8:
                return 'Eight '
            elif num == 9:
                return 'Nine '

        def two_less_20(num):
            if num == 10:
                return 'Ten '
            elif num == 11:
                return 'Eleven '
            elif num == 12:
                return 'Twelve '
            elif num == 13:
                return 'Thirteen '
            elif num == 14:
                return 'Fourteen '
            elif num == 15:
                return 'Fifteen '
            elif num == 16:
                return 'Sixteen '
            elif num == 17:
                return 'Seventeen '
            elif num == 18:
                return 'Eighteen '
            elif num == 19:
                return 'Nineteen '

        def ten(num):
            if num // 10 == 2:
                return 'Twenty '
            elif num // 10 == 3:
                return 'Thirty '
            elif num // 10 == 4:
                return 'Forty '
            elif num // 10 == 5:
                return 'Fifty '
            elif num // 10 == 6:
                return 'Sixty '
            elif num // 10 == 7:
                return 'Seventy '
            elif num // 10 == 8:
                return 'Eighty '
            elif num // 10 == 9:
                return 'Ninety '

        def two(num):
            if num == 0:
                return ''
            elif num < 10:
                return one(num)
            elif num < 20:
                return two_less_20(num)
            else:
                return ten(num) + one(num % 10)

        billion = num // 10**9
        million = (num % 10**9) // 10**6
        thousand = (num % 10**6) // 10**3
        result = ''

        if billion:
            result += one(billion) + 'Billion '
        if million:
            result += two(million) + 'Million '
        if thousand:
            result += two(thousand) + 'Thousand '
        result += two(num % 1000)

        return result.strip()
