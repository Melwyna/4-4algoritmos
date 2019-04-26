import unittest
from funciones import funciones44

class TestCollectionMethods(unittest.TestCase):

 def test_consecutivo(self):

  lista = (1, 1, 2, 3, 3, 4, 5, 2, 4, 5, 6, 7, 8, 9, 6, -1, 2)

  result4 = funciones44.consecutivo(lista)
  self.assertEqual(result4, 6)