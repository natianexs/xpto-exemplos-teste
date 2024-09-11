import unittest

from apps.validators import Validators


class ValidatorPasswodTest(unittest.TestCase):

    def test_password_valid(self):
        result = Validators.check_password(self, "N@t1@1234")
        self.assertEqual(result, 0)

    def test_password_invalid(self):
        result = Validators.check_password(self, "MACACOAZUL123")
        self.assertEqual(result, -1)

    def test_password_empty(self):
        result = Validators.check_password(self, "")
        self.assertEqual(result, -1)
