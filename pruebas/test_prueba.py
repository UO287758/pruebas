import unittest
from prueba import sumar, restar, multiplicar, dividir, potencia, raiz_cuadrada

class TestPrueba(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(1, 2), 3)

    def test_restar(self):
        self.assertEqual(restar(2, 1), 1)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(2, 3), 6)

    def test_dividir(self):
        self.assertEqual(dividir(6, 3), 2)
    
    def test_error_division(self):
        with self.assertRaises(ValueError):
            dividir(1, 0)
    
    def test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)

    def test_raiz_cuadrada(self):
        self.assertEqual(raiz_cuadrada(4), 2)
if __name__ == '__main__':
    unittest.main()