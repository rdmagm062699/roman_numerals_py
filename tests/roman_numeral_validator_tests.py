import unittest
import nose.tools as nt

from romannumerals.roman_numeral_validator import RomanNumeralValidator

class RomanNumeralValidatorTest(unittest.TestCase):

    def setUp(self):
        self.validator = RomanNumeralValidator()

    def test_check_content_string_contains_all_possible_numerals_returns_true(self):
        numerals = 'IVXLCDM'
        result = self.validator.check_content(numerals)

        nt.assert_equal(result, True)

    def test_check_content_string_contains_all_possible_numerals_with_duplicates_returns_true(self):
        numerals = 'MMDVLXXVI'
        result = self.validator.check_content(numerals)

        nt.assert_equal(result, True)

    def test_check_content_string_contains_valid_and_invalid_returns_false(self):
        numerals = 'IVXLCDM_012343j'
        result = self.validator.check_content(numerals)

        nt.assert_equal(result, False)

    def test_check_content_string_contains_all_lowercase_valid_values_returns_true(self):
        numerals = 'ivxlcdm'
        result = self.validator.check_content(numerals)

        nt.assert_equal(result, True)

    def test_check_content_string_contains_mixed_case_valid_values_returns_false(self):
        numerals = 'IvXlCdm'
        result = self.validator.check_content(numerals)

        nt.assert_equal(result, False)
