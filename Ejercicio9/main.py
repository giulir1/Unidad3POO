import unittest
from palindromo import Palindromo


class TestPalindromo(unittest.TestCase):
    __palindromo = None

    def setUp(self):
        self.__palindromo = Palindromo('abba')

    def test_palindromo1(self):
        self.assertTrue(self.__palindromo.esPalindromo())

    def test_palindromo2(self):
        self.__palindromo.setPalabra('alla')
        self.assertTrue(self.__palindromo.esPalindromo())

    def test_palindromo3(self):
        self.__palindromo.setPalabra('Celular')
        self.assertFalse(self.__palindromo.esPalindromo())


if __name__ == '__main__':
    unittest.main()
