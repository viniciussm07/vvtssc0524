import unittest
import placar


class TestPlacar(unittest.TestCase):

    def setUp(self):
        self.p1 = placar.Placar()

    # Domínio (recebe inteiro e lista de inteiros):
    #   - conta(i -> int de 1 a 10, l -> lista de ints de 1 a 6)
    #   - retorna a quantidade de números i dentro de l
    # 
    def test_conta(self):
        self.assertEqual(self.p1.conta(3, [1, 2, 3, 3, 3]), 3)
        self.assertEqual(self.p1.conta(3, [1, 2, 4, 5, 6]), 0)
        self.assertEqual(self.p1.conta(1, [1, 1, 1, 1, 1]), 5)
    def test_conta2(self):
        self.assertEqual(self.p1.conta(5, [5, 5, 2, 3, 4]), 2)
        self.assertEqual(self.p1.conta(5, [1, 2, 3, 4, 6]), 0)
        self.assertEqual(self.p1.conta(6, [6, 6, 6, 6, 6]), 5)
    
    # Domínio (recebe lista de inteiros):
    #   - checkFull(lista de inteiros de 1 a 6)
    #   - retorna verdadeiro ou falso
    # 4 testes: 1 abaixo e 1 acima do domínio de aplicação, 1 que retorna true e outro que retorna false
    def test_full_house1(self):
        self.assertTrue(self.p1.checkFull([3,3,3,2,2]))
    def test_full_house2(self):
        self.assertTrue(self.p1.checkFull([5,5,5,5,5]))

    # Domínio (recebe um inteiro e uma lista de inteiros):
    #   - add(i -> int de 1 a 10 intervalo fechado, l -> lista de ints de 1 a 6 intervalo fechado)
    #   - não retorna nada
    def test_posicao_invalida(self):
        with self.assertRaises(IndexError) as cm:
            self.p1.add(12 , [1, 2, 3, 4, 5, 6])
        self.assertEqual(str(cm.exception), "Valor da posição no placar é ilegal")
    def test_posicao_ocupada(self):
        self.p1.add(1, [1, 1, 1, 2, 2])
        with self.assertRaises(ValueError) as cm:
            self.p1.add(1, [3, 3, 3, 4, 4])
        self.assertEqual(str(cm.exception), "Posição ocupada no placar")

    # Domínio (recebe lista de inteiros):
    #   - checkQuadra(lista de inteiros de 1 a 6)
    #   - retorna verdadeiro ou falso
    # 4 testes: 1 abaixo e 1 acima do domínio de aplicação, 1 que retorna true e outro que retorna false
    def test_quadra1(self):
        self.assertTrue(self.p1.checkQuadra([2,2,2,2,5]))
    def test_quadra2(self):
        self.assertTrue(self.p1.checkQuadra([3,6,6,6,6]))

    # Domínio (recebe lista de inteiros):
    #   - checkQuina(lista de inteiros de 1 a 6)
    #   - retorna verdadeiro ou falso
    # 4 testes: 1 abaixo e 1 acima do domínio de aplicação, 1 que retorna true e outro que retorna false
    def test_quina1(self): 
        self.assertTrue(self.p1.checkQuina([4,4,4,4,4]))
    def test_quina2(self):
        self.assertFalse(self.p1.checkQuina([4,4,4,4,5]))

    # Domínio (recebe lista de inteiros):
    #   - checkSeqMaior(lista de inteiros de 1 a 6)
    #   - retorna verdadeiro ou falso
    # 4 testes: 1 abaixo e 1 acima do domínio de aplicação, 1 que retorna true e outro que retorna false
    def test_sequencia1(self):
        self.assertTrue(self.p1.checkSeqMaior([2,3,4,5,6]))
    def test_sequencia2(self):
        self.assertFalse(self.p1.checkSeqMaior([1,2,3,4,6]))

    # Domínio (recebe lista de inteiros):
    #   - str(lista de inteiros de 1 a 6)
    #   - retorna string específica
    def test_str1(self):
        expected = "(1)    |   (7)    |  (4) \n-------|----------|-------\n(2)    |   (8)    |  (5) \n-------|----------|-------\n(3)    |   (9)    |  (6) \n-------|----------|-------\n       |   (10)   |\n       +----------+\n"
        self.assertEqual(str(self.p1), expected)
    def test_str2(self):
        self.p1.add(1, [1, 1, 1, 2, 2])
        self.p1.add(7, [3, 3, 3, 2, 2])
        self.p1.add(10, [4, 4, 4, 4, 4])
        
        self.assertEqual(self.p1.getScore(0), 3)
        self.assertEqual(self.p1.getScore(6), 15)
        self.assertEqual(self.p1.getScore(9), 40)
        
        self.assertTrue(self.p1.getTaken(0))
        self.assertTrue(self.p1.getTaken(6))
        self.assertTrue(self.p1.getTaken(9))


if __name__ == '__main__':
    unittest.main()
