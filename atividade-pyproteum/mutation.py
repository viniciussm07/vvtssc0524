import unittest
import placar

class TestPlacarMutation(unittest.TestCase):
    def setUp(self):
        self.p1 = placar.Placar()

    # ===MATA MUTANTE 1216====
    def test_posicao_9_quadra(self):
        dados = [4, 4, 4, 4, 2]  
        self.p1.add(9, dados)
        assert self.p1.placar[8] == 30

    def test_posicao_9_sem_quadra(self):
        dados = [1, 2, 3, 4, 5]   
        self.p1.add(9, dados)
        assert self.p1.placar[8] == 0


    # ==EQUIVALENTE MUTANTE 1212==
    def test_posicao_7_full(self):
        dados = [2,2,2,3,3]  
        self.p1.add(7, dados)
        assert self.p1.placar[6] == 15  


    # ==1208==
    def test_posicao_1_com_dados(self):
        dados = [1,1,2,3,4]  
        self.p1.add(1, dados)
        assert self.p1.placar[0] == 1