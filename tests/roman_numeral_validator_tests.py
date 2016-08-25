import unittest
import nose.tools as nt

from romannumerals.roman_numeral_validator import RomanNumeralValidator

class RomanNumeralValidatorTest(unittest.TestCase):

    def setUp(self):
        self.validator = RomanNumeralValidator()

    def test_check_content_some_invalid_value_returns_false(self):
        result = self.validator.check_content('blah')

        nt.assert_equal(result, False)

    def test_check_content_string_contains_all_possible_numerals_returns_true(self):
        numerals = 'IVXLCDM'
        result = self.validator.check_content(numerals)

        nt.assert_equal(result, True)
