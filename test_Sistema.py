import unittest

from Sistema import Sistema
from Cuenta import Cuenta
from faker import Faker

faker = Faker()


class SistemaTest(unittest.TestCase):
    def test_iniciar_sistema(self):
        sistema = Sistema()
        self.assertEqual(len(sistema.cuentas), 0)
        self.assertNotEqual(len(sistema.cuentas), 1)

    def test_agregar_cuenta(self):
        sistema = Sistema()
        cuenta1 = Cuenta(faker.random_number(digits=5), faker.name(), "Expert", 0)
        sistema.agregar_cuenta(cuenta1)
        self.assertEqual(len(sistema.cuentas), 1)

        cuenta2 = Cuenta(faker.random_number(digits=5), faker.name(), "Master", 100)
        sistema.agregar_cuenta(cuenta2)
        self.assertEqual(len(sistema.cuentas), 2)

        cuenta3 = Cuenta(faker.random_number(digits=5), faker.name(), "Standard", 200)
        sistema.agregar_cuenta(cuenta3)
        self.assertEqual(len(sistema.cuentas), 3)
        self.assertNotEqual(len(sistema.cuentas), 5)

    def test_cargar_puntos(self):
        sistema = Sistema()
        cuenta1 = Cuenta(faker.random_number(digits=5), faker.name(), "Expert", 0)
        sistema.agregar_cuenta(cuenta1)
        self.assertEqual(cuenta1.cargar_puntos(100), 100)
        self.assertNotEqual(cuenta1.cargar_puntos(100), 250)

        cuenta2 = Cuenta(faker.random_number(digits=5), faker.name(), "Master", 100)
        sistema.agregar_cuenta(cuenta2)
        self.assertEqual(cuenta2.cargar_puntos(50), 150)
        self.assertNotEqual(cuenta2.cargar_puntos(50), 300)

        cuenta3 = Cuenta(faker.random_number(digits=5), faker.name(), "Standard", 200)
        sistema.agregar_cuenta(cuenta3)
        self.assertEqual(cuenta3.cargar_puntos(100), 300)
        self.assertNotEqual(cuenta3.cargar_puntos(100), 0)

    def test_redimir_puntos(self):
        sistema = Sistema()
        cuenta1 = Cuenta(faker.random_number(digits=5), faker.name(), "Expert", 0)
        sistema.agregar_cuenta(cuenta1)
        self.assertEqual(cuenta1.redimir_puntos(0), 0)
        self.assertNotEqual(cuenta1.redimir_puntos(0), 50)

        cuenta2 = Cuenta(faker.random_number(digits=5), faker.name(), "Master", 100)
        sistema.agregar_cuenta(cuenta2)
        self.assertEqual(cuenta2.redimir_puntos(70), 30)

        cuenta3 = Cuenta(faker.random_number(digits=5), faker.name(), "Standard", 200)
        sistema.agregar_cuenta(cuenta3)
        self.assertEqual(cuenta3.redimir_puntos(50), 150)
