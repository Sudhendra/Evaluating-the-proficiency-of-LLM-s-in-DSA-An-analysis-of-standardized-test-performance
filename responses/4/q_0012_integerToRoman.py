from collections import OrderedDict

class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = OrderedDict([(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                               (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                               (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')])
        
        roman = ''
        for key, value in mapping.items():
            count = num // key
            roman += value * count
            num -= key * count
        
        return roman
