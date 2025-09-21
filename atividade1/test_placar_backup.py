import unittest
import placar

class TestPlacar(unittest.TestCase):

    def setUp(self):
        self.p1 = placar.Placar()

    # def test_conta(self):
    # def test_conta2(self)

    def test_full_house1(self):
        self.assertTrue(self.p1.checkFull([3,3,3,2,2]))

    def test_full_house2(self):
        self.assertTrue(self.p1.checkFull([5,5,5,5,5]))

    def test_posicao_invalida(self):
        with self.assertRaises(IndexError) as cm:
            self.p1.add(12 , [1, 2, 3, 4, 5, 6])
        self.assertEqual(str(cm.exception), "Valor da posição no placar é ilegal")

    def test_posicao_ocupada(self):
        self.p1.add(1, [1, 1, 1, 2, 2])
        with self.assertRaises(ValueError) as cm:
            self.p1.add(1, [3, 3, 3, 4, 4])
        self.assertEqual(str(cm.exception), "Posição ocupada no placar")

    def test_quadra1(self):
        self.assertTrue(self.p1.checkQuadra([2,2,2,2,5]))

    def test_quadra2(self):
        self.assertTrue(self.p1.checkQuadra([3,6,6,6,6]))

    def test_quina1(self): 
        self.assertTrue(self.p1.checkQuina([4,4,4,4,4]))

    def test_quina2(self):
        self.assertFalse(self.p1.checkQuina([4,4,4,4,5]))

    def test_sequencia1(self):
        self.assertTrue(self.p1.checkSeqMaior([2,3,4,5,6]))

    def test_sequencia2(self):
        self.assertFalse(self.p1.checkSeqMaior([1,2,3,4,6]))

    # def test_str1(self)
    # def test_str2(self)


if __name__ == '__name__':
    unittest.main()