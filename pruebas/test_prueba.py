import unittest
from prueba import sumar, restar, multiplicar, dividir

class TestPrueba(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(1, 2), 3)

    def test_restar(self):
        self.assertEqual(restar(2, 1), 1)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(2, 3), 6)

    def test_dividir(self):
        self.assertEqual(dividir(6, 3), 2)
        with self.assertRaises(ValueError):
            dividir(1, 0)

if __name__ == '__main__':
    unittest.main()