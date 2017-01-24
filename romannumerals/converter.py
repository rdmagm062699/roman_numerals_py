
class Converter(object):
    def convert_from_number_to_roman_numeral(self, number):
        result = ''

        for value in range(0, number):
            result += 'I'

        return result
