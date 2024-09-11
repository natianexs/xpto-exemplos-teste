import unittest

from apps.validators import Validators


class ValidatorsEmailTest(unittest.TestCase):

    def test_email_valid(self):
        result = Validators.check_email(self, "natianexvs@gmail.com")
        self.assertTrue(result, True)

    def test_email_invalid(self):
        result = Validators.check_email(self, "natianexvs.com")
        self.assertFalse(result, False)
