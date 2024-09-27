import unittest

from Cuenta import Cuenta
from faker import Faker

faker = Faker()


class CuentaTest(unittest.TestCase):
    def test_crear_cuenta(self):
        cuenta1 = Cuenta(faker.random_number(digits=5), faker.name(), "Expert", 0)
        self.assertEqual(cuenta1.saldo, 0)
        self.assertNotEqual(cuenta1.saldo, 100)

        cuenta2 = Cuenta(faker.random_number(digits=5), faker.name(), "Master", 0)
        self.assertEqual(cuenta2.saldo, 0)
        self.assertNotEqual(cuenta2.saldo, 50)

        cuenta3 = Cuenta(faker.random_number(digits=5), faker.name(), "Standard", 0)
        self.assertEqual(cuenta3.saldo, 0)
        self.assertNotEqual(cuenta3.saldo, 75)
