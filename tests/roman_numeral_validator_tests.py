import unittest
import nose.tools as nt

from romannumerals.roman_numeral_validator import RomanNumeralValidator

class RomanNumeralValidatorTest(unittest.TestCase):

    def setUp(self):
        self.validator = RomanNumeralValidator()

    def test_check_content_capital_i_returns_true(self):
        result = self.validator.check_content('I')

        nt.assert_equal(result, True)

    def test_check_content_some_invalid_value_returns_false(self):
        result = self.validator.check_content('blah')

        nt.assert_equal(result, False)
