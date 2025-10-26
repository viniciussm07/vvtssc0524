import unittest
import placar

class TestPlacar(unittest.TestCase):

    def setUp(self):
        self.p1 = placar.Placar()
        
    def test_conta(self):
        self.assertEqual(self.p1.conta(1, [1, 1, 3, 3, 3]), 2)
        self.assertEqual(self.p1.conta(3, [1, 2, 4, 5, 6]), 0)
        self.assertEqual(self.p1.conta(1, [1, 1, 1, 1, 1]), 5)

    def test_full_house_true(self):
        self.assertTrue(self.p1.checkFull([3,3,3,2,2]))
        self.assertTrue(self.p1.checkFull([1,1,1,1,1]))
        self.assertTrue(self.p1.checkFull([1,1,5,5,5]))
    
    def test_full_house_false(self):
        self.assertFalse(self.p1.checkFull([1,2,3,4,2]))
        self.assertFalse(self.p1.checkFull([1,1,1,1,3]))
        self.assertFalse(self.p1.checkFull([1,1,3,5,5]))

    def test_posicao_invalida(self):
        with self.assertRaises(IndexError) as cm:
            self.p1.add(12 , [1, 2, 3, 4, 5, 6])
        self.assertEqual(str(cm.exception), "Valor da posição no placar é ilegal")

    def test_posicao_ocupada(self):
        self.p1.add(1, [1, 1, 1, 2, 2])
        with self.assertRaises(ValueError) as cm:
            self.p1.add(1, [3, 3, 3, 4, 4])
        self.assertEqual(str(cm.exception), "Posição ocupada no placar")

    def test_quadra(self):
        self.assertTrue(self.p1.checkQuadra([2,2,2,2,5]))

    def test_quina(self):
        self.assertFalse(self.p1.checkQuina([4,4,4,4,5]))

    def test_sequencia(self):
        self.assertTrue(self.p1.checkSeqMaior([2,3,4,5,6]))

    def test_str(self):
        expected = "(1)    |   (7)    |  (4) \n-------|----------|-------\n(2)    |   (8)    |  (5) \n-------|----------|-------\n(3)    |   (9)    |  (6) \n-------|----------|-------\n       |   (10)   |\n       +----------+\n"
        self.assertEqual(str(self.p1), expected)