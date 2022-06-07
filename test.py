from Palindromo import Palindromo
import unittest
from unittest import TestCase

class TestPalindromo(TestCase):
    __unPalindromo=None
    __noPalindromo=None
    def inicia(self):
        self.__palindromo = Palindromo("neuquen")
        self.__noPalindromo = Palindromo("prueba")
    def palindromo(self):
        self.assertTrue(self.__palindromo.esPalindromo())
    def noalindromo(self):
        self.assertFalse(self.__noPalindromo.esPalindromo())

if __name__ == "__main__":
    unittest.main()
