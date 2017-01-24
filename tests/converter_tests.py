import unittest
import nose.tools as nt

from romannumerals.converter import Converter


class ConverterTest(unittest.TestCase):

    def setUp(self):
        self.converter = Converter()

    def test_convert_from_number_to_roman_numeral_converts_1(self):
        rn = self.converter.convert_from_number_to_roman_numeral(1)
        nt.assert_equal(rn, 'I')

    def test_convert_from_number_to_roman_numeral_converts_2(self):
        rn = self.converter.convert_from_number_to_roman_numeral(2)
        nt.assert_equal(rn, 'II')

    def test_convert_from_number_to_roman_numeral_converts_3(self):
        rn = self.converter.convert_from_number_to_roman_numeral(3)
        nt.assert_equal(rn, 'III')