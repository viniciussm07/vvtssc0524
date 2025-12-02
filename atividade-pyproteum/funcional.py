import unittest
import placar

class TestPlacar(unittest.TestCase):

    def setUp(self):
        self.p1 = placar.Placar()
    
    def test_str1(self):
        expected = "(1)    |   (7)    |  (4) \n-------|----------|-------\n(2)    |   (8)    |  (5) \n-------|----------|-------\n(3)    |   (9)    |  (6) \n-------|----------|-------\n       |   (10)   |\n       +----------+\n"
        self.assertEqual(str(self.p1), expected)

    def test_str2(self):
        expected = " 1     |    0     |   8  \n-------|----------|-------\n 2     |    20    |   5  \n-------|----------|-------\n 3     |    0     |   18 \n-------|----------|-------\n       |    0     |\n       +----------+\n"
        self.p1.add(1, [2, 6, 3, 4, 1]);
        self.p1.add(4, [6, 3, 6, 4, 4]);
        self.p1.add(2, [2, 5, 5, 3, 4]);
        self.p1.add(3, [3, 4, 4, 2, 5]);
        self.p1.add(5, [4, 2, 3, 5, 4]);
        self.p1.add(6, [3, 6, 6, 4, 6]);
        self.p1.add(7, [2, 1, 4, 1, 2]);
        self.p1.add(8, [4, 3, 2, 5, 1]);
        self.p1.add(9, [6, 4, 1, 5, 5]);
        self.p1.add(10, [3, 3, 1, 6, 3]);
        self.assertEqual(str(self.p1), expected)
    
    def test_uma_linha(self):
        expected_empty = ['(1) ', '(2) ', '(3) ', '(4) ', '(5) ', '(6) ', '(7) ', '(8) ', '(9) ', '(10)']
        for i in range(10):
            self.assertEqual(self.p1.uma_linha(i), expected_empty[i])

        for i in range(10):
            self.p1.placar[i] = i * 10 + 1
            self.p1.taken[i] = True

        expected_taken = [('{:^4d}'.format(self.p1.placar[i])) for i in range(10)]
        for i in range(10):
            self.assertEqual(self.p1.uma_linha(i), expected_taken[i])
    
    def test_add_posicao_invalida(self):
        with self.assertRaises(IndexError) as cm:
            self.p1.add(0, [1, 2, 3, 4, 5])
        self.assertEqual(str(cm.exception), "Valor da posição no placar é ilegal")
        
        with self.assertRaises(IndexError) as cm:
            self.p1.add(11, [1, 2, 3, 4, 5])
        self.assertEqual(str(cm.exception), "Valor da posição no placar é ilegal")
        
        with self.assertRaises(IndexError) as cm:
            self.p1.add(12, [1, 2, 3, 4, 5])
        self.assertEqual(str(cm.exception), "Valor da posição no placar é ilegal")

    def test_add_posicao_ocupada(self):
        self.p1.add(1, [1, 1, 1, 2, 2])
        with self.assertRaises(ValueError) as cm:
            self.p1.add(1, [3, 3, 3, 4, 4])
        self.assertEqual(str(cm.exception), "Posição ocupada no placar")
    
    def test_add_posicoes_1_a_6_validas(self):
        dados_variados = [
            [1, 1, 2, 3, 4],
            [2, 2, 3, 4, 5],
            [3, 3, 4, 5, 6],
            [4, 4, 1, 2, 6],
            [5, 5, 1, 2, 3],
            [6, 6, 1, 2, 3]
        ]
        for posicao in range(1, 7):
            self.p1.add(posicao, dados_variados[posicao - 1])
            self.assertTrue(self.p1.taken[posicao - 1])
            
    def test_add_posicao_7_satisfeita(self):
        dados = [2, 2, 3, 3, 3]
        self.p1.add(7, dados)
        self.assertTrue(self.p1.taken[6])
        self.assertIsInstance(self.p1.placar[6], int)

    def test_add_posicao_7_nao_satisfeita(self):
        dados = [1, 2, 3, 4, 5]
        self.p1.add(7, dados)
        self.assertTrue(self.p1.taken[6])
        self.assertIsInstance(self.p1.placar[6], int)

    def test_add_posicao_8_satisfeita(self):
        dados = [2, 3, 4, 5, 6]
        self.p1.add(8, dados)
        self.assertTrue(self.p1.taken[7])
        self.assertIsInstance(self.p1.placar[7], int)

    def test_add_posicao_8_nao_satisfeita(self):
        dados = [1, 1, 2, 3, 4] 
        self.p1.add(8, dados)
        self.assertTrue(self.p1.taken[7])
        self.assertIsInstance(self.p1.placar[7], int)

    def test_add_posicao_9_satisfeita(self):
        dados = [5, 5, 5, 5, 2]
        self.p1.add(9, dados)
        self.assertTrue(self.p1.taken[8])
        self.assertIsInstance(self.p1.placar[8], int)

    def test_add_posicao_9_nao_satisfeita(self):
        dados = [5, 5, 3, 2, 1] 
        self.p1.add(9, dados)
        self.assertTrue(self.p1.taken[8])
        self.assertIsInstance(self.p1.placar[8], int)

    def test_add_posicao_10_satisfeita(self):
        dados = [1, 1, 1, 1, 1] 
        self.p1.add(10, dados)
        self.assertTrue(self.p1.taken[9])
        self.assertIsInstance(self.p1.placar[9], int)

    def test_add_posicao_10_nao_satisfeita(self):
        dados = [4, 4, 4, 4, 5] 
        self.p1.add(10, dados)
        self.assertTrue(self.p1.taken[9])
        self.assertIsInstance(self.p1.placar[9], int)

    def test_getScore_sem_parametro(self):
        self.assertEqual(self.p1.getScore(), 0)

    def test_getScore_com_parametro(self):
        self.p1.add(1, [1, 1, 1, 1, 1])
        self.p1.add(2, [2, 2, 2, 2, 2])
        self.p1.add(3, [3, 3, 3, 3, 3])
        self.p1.add(10, [1, 1, 1, 1, 1])
        
        self.assertEqual(self.p1.getScore(0), 5)
        self.assertEqual(self.p1.getScore(1), 10)
        self.assertEqual(self.p1.getScore(2), 15)
        self.assertEqual(self.p1.getScore(9), 40)

    def test_getScore_index_nao_ocupado(self):
        self.assertEqual(self.p1.getScore(0), 0)
        self.assertEqual(self.p1.getScore(5), 0)
        self.assertEqual(self.p1.getScore(9), 0)

    def test_getScore_soma_varias_posicoes(self):
        self.p1.add(1, [1, 1, 1, 1, 1])
        self.p1.add(2, [2, 2, 2, 2, 2])
        self.p1.add(10, [1, 1, 1, 1, 1])
        self.assertEqual(self.p1.getScore(), 5 + 10 + 40)
    
    def test_getTaken_true(self):
        dados = [1, 1, 1, 4, 6] 
        self.p1.add(1, dados)
        self.assertTrue(self.p1.getTaken(0))

    def test_getTaken_false(self):
        self.assertFalse(self.p1.getTaken(5))

    def test_conta_0_ocorrencias(self):
        self.assertEqual(self.p1.conta(3, [1, 2, 4, 5, 6]), 0)

    def test_conta_1_ocorrencia(self):
        self.assertEqual(self.p1.conta(3, [1, 2, 3, 4, 5]), 1)

    def test_conta_2_ocorrencias(self):
        self.assertEqual(self.p1.conta(1, [1, 1, 3, 3, 3]), 2)

    def test_conta_3_ocorrencias(self):
        self.assertEqual(self.p1.conta(2, [2, 2, 2, 3, 4]), 3)

    def test_conta_4_ocorrencias(self):
        self.assertEqual(self.p1.conta(4, [4, 4, 4, 4, 5]), 4)

    def test_conta_5_ocorrencias(self):
        self.assertEqual(self.p1.conta(1, [1, 1, 1, 1, 1]), 5)

    def test_checkFull_true(self):
        self.assertTrue(self.p1.checkFull([3,3,3,2,2]))
        self.assertTrue(self.p1.checkFull([1,1,1,1,1]))
        self.assertTrue(self.p1.checkFull([1,1,5,5,5]))
        self.assertTrue(self.p1.checkFull([5,1,5,5,1]))
    
    def test_checkFull_false(self):
        self.assertFalse(self.p1.checkFull([1,2,3,4,2]))
        self.assertFalse(self.p1.checkFull([1,1,1,1,3]))
        self.assertFalse(self.p1.checkFull([1,1,3,5,5]))

    def test_checkSeqMaior_true(self):
        self.assertTrue(self.p1.checkSeqMaior([3,4,5,6,2]))
        self.assertTrue(self.p1.checkSeqMaior([1,2,3,4,5]))
        self.assertTrue(self.p1.checkSeqMaior([2,3,4,5,6]))

    def test_checkSeqMaior_false(self):
        self.assertFalse(self.p1.checkSeqMaior([1,1,1,1,1]))
    
    def test_checkQuadra_true(self):
        self.assertTrue(self.p1.checkQuadra([5,5,5,5,5]))
        self.assertTrue(self.p1.checkQuadra([1,2,2,2,2]))
    
    def test_checkQuadra_false(self):
        self.assertFalse(self.p1.checkQuadra([5,1,5,5,1]))

    def test_checkQuina_true(self):
        self.assertTrue(self.p1.checkQuina([3,3,3,3,3]))

    def test_checkQuina_false(self):
        self.assertFalse(self.p1.checkQuina([2,3,4,5,6]))

    def test_getName_values(self):
        expected_names = [
            "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes",
            "Full", "Sequence", "Four of a kind", "General"
        ]
        for i, name in enumerate(expected_names):
            self.assertEqual(self.p1.getName(i), name)
