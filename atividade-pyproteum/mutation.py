import unittest
from placar import Placar

class TestPlacarMutation(unittest.TestCase):
    def setUp(self):
        self.p = Placar()

    def test_posicao_9_quadra(self):
        dados = [4, 4, 4, 4, 2]  
        self.p.add(9, dados)
        self.assertEqual(self.p.placar[8], 30)

    def test_posicao_9_sem_quadra(self):
        dados = [1, 2, 3, 4, 5]   
        self.p.add(9, dados)
        self.assertEqual(self.p.placar[8], 0)

    def test_posicao_7_full(self):
        dados = [2,2,2,3,3]  
        self.p.add(7, dados)
        self.assertEqual(self.p.placar[6], 15)  

    def test_posicao_1_com_dados(self):
        dados = [1,1,2,3,4]  
        self.p.add(1, dados)
        self.assertEqual(self.p.placar[0], 2) 
    
    def test_checkFull_desordenado(self):
        self.assertTrue(self.p.checkFull([2, 3, 2, 3, 2]))

    def test_checkQuadra_desordenado(self):
        self.assertTrue(self.p.checkQuadra([1, 5, 1, 1, 1]))

    def test_quadra_falsa_buraco_no_meio_caso_1(self):
        self.assertFalse(self.p.checkQuadra([1, 1, 1, 2, 2]))

    def test_quadra_falsa_buraco_nas_pontas_caso_2(self):
        self.assertFalse(self.p.checkQuadra([1, 2, 2, 2, 3]))

    def test_quina_falsa_intruso_inicio(self):
        self.assertFalse(self.p.checkQuina([1, 2, 2, 2, 2]))

    def test_quina_falsa_intruso_fim(self):
        self.assertFalse(self.p.checkQuina([2, 2, 2, 2, 1]))

    def test_posicao_8_sequencia_invalida_retorna_zero(self):
        self.p.add(8, [1, 1, 1, 1, 1])
        self.assertEqual(self.p.placar[7], 0)

    def test_taken_deve_ser_boolean_true(self):
        self.p.add(1, [1, 1, 1, 1, 1])
        self.assertTrue(self.p.taken[0])
        self.assertIsInstance(self.p.taken[0], bool)
