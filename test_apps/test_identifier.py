import unittest

from apps.validators import Validators


class ValidatorTest(unittest.TestCase):

    # Cenário 1: Identificador com tamanho válido máximo 10 caracteres
    def test_identifier_valid_size_max(self):
        result = Validators.check_valid_identifier(self, "natianeSil")
        self.assertTrue(result, "Identificador válido")

    # Cenário 1: Identificador com tamanho válido mínimo 3 caracteres
    def test_identifier_valid_size_min(self):
        result = Validators.check_valid_identifier(self, "nat")
        self.assertTrue(result, "Identificador válido")

    # Cenário 2: Identificador muito curto
    def test_identifier_too_short(self):
        result = Validators.check_valid_identifier(self, "N")
        self.assertFalse(result, "Identificador muito curto deve ser inválido")

    # Cenário 3: Identificador muito longo
    def test_identifier_too_long(self):
        result = Validators.check_valid_identifier(self, "Natiane Xavier")
        self.assertFalse(result, "Identificador muito longo deve ser inválido")

    # Cenário 4: Identificador contendo caracteres inválidos
    def test_identifier_invalid_characters(self):
        result = Validators.check_valid_identifier(self, "@Natiane")
        self.assertFalse(result, "Identificador com caracteres inválidos deve ser inválido")

    # Cenário 5: Identificador vazio
    def test_identifier_empty(self):
        result = Validators.check_valid_identifier(self, "")
        self.assertFalse(result, "Identificador vazio deve ser inválido")

    # Cenário 6: Identificador com espaços em branco
    def test_identifier_with_spaces(self):
        result = Validators.check_valid_identifier(self, "Nati s")
        self.assertFalse(result, "Não aceita espaços em branco no identificador")

    # Cenário 7: Identificador numérico
    def test_identifier_numeric(self):
        result = Validators.check_valid_identifier(self, "123456")
        self.assertFalse(result, "Identificador numérico deve ser inválido")


if __name__ == '__main__':
    unittest.main()
