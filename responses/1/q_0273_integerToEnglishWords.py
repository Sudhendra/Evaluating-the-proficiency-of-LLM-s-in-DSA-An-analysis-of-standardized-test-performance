class Solution:
    def numberToWords(self, num: int) -> str:
        def one_digit(num):
            dict_1_to_9 = {
                1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 
                6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'
            }
            return dict_1_to_9[num]

        def two_digits(num):
            dict_10_to_19 = {
                10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
                15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'
            }
            dict_tens = {
                2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 
                6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'
            }
            if num < 10:
                return one_digit(num)
            elif num < 20:
                return dict_10_to_19[num]
            else:
                return dict_tens[num // 10] + ('' if num % 10 == 0 else ' ' + one_digit(num % 10))

        def three_digits(num):
            hundreds = num // 100
            if hundreds == 0:
                return two_digits(num % 100)
            res = one_digit(hundreds) + ' Hundred'
            if num % 100 != 0:
                res += ' ' + two_digits(num % 100)
            return res

        if num == 0:
            return 'Zero'

        billion = num // 10 ** 9
        million = (num % 10 ** 9) // 10 ** 6
        thousand = (num % 10 ** 6) // 10 ** 3
        ones = num % 10 ** 3

        res = ''
        if billion > 0:
            res += three_digits(billion) + ' Billion'
        if million > 0:
            if res:
                res += ' '
            res += three_digits(million) + ' Million'
        if thousand > 0:
            if res:
                res += ' '
            res += three_digits(thousand) + ' Thousand'
        if ones > 0:
            if res:
                res += ' '
            res += three_digits(ones)

        return res