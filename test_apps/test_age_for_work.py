import unittest

from apps.validators import Validators


class ValidatorTest(unittest.TestCase):

    def test_age_no_employ_minor(self):
        result = Validators.check_age_for_work(self, 16)
        self.assertEqual(result, "Não Empregar")

    def test_age_no_employ_old(self):
        result = Validators.check_age_for_work(self, 101)
        self.assertEqual(result, "Empregado Como Múmia")

    def test_age_employed_part_time(self):
        result = Validators.check_age_for_work(self, 18)
        self.assertEqual(result, "Empregado Parcial")

    def test_age_employ_full(self):
        result = Validators.check_age_for_work(self, 55)
        self.assertEqual(result, "Empregado Integral")
