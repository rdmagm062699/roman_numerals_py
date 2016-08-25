VALID_NUMERALS = ['I', 'V', 'X', 'L', 'C', 'D', 'M']


class RomanNumeralValidator(object):

    def check_content(self, roman_numeral):
        if all(numeral in VALID_NUMERALS for numeral in roman_numeral):
            return True

        return False
