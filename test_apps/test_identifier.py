import unittest

from apps.validators import Validators


class ValidatorTest(unittest.TestCase):

    # Cenário 1: Identificador com tamanho válido
    def test_identifier_valid_size(self):
        result = Validators.check_valid_identifier(self, "natiane")
        self.assertTrue(result, "Identificador válido")

    # Cenário 2: Identificador muito curto
    def test_identifier_too_short(self):
        result = Validators.check_valid_identifier("A")
        self.assertFalse(result, "Identificador muito curto deve ser inválido")

    # Cenário 3: Identificador muito longo
    def test_identifier_too_long(self):
        result = Validators.check_valid_identifier("A" * 101)
        self.assertFalse(result, "Identificador muito longo deve ser inválido")

    # Cenário 4: Identificador contendo caracteres inválidos
    def test_identifier_invalid_characters(self):
        result = Validators.check_valid_identifier("Invalid@Name")
        self.assertFalse(result, "Identificador com caracteres inválidos deve ser inválido")

    # Cenário 5: Identificador vazio
    def test_identifier_empty(self):
        result = Validators.check_valid_identifier("")
        self.assertFalse(result, "Identificador vazio deve ser inválido")

    # Cenário 6: Identificador nulo
    def test_identifier_none(self):
        result = Validators.check_valid_identifier(None)
        self.assertFalse(result, "Identificador None deve ser inválido")

    # Cenário 7: Identificador com espaços em branco
    def test_identifier_with_spaces(self):
        result = Validators.check_valid_identifier("Natiane Santos")
        self.assertTrue(result, "Identificador com espaços válidos deve ser aceito")

    # Cenário 8: Identificador numérico
    def test_identifier_numeric(self):
        result = Validators.check_valid_identifier("123456")
        self.assertFalse(result, "Identificador numérico deve ser inválido")


if __name__ == '__main__':
    unittest.main()
