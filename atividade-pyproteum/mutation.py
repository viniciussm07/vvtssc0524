import unittest
from placar import Placar

class TestPlacarMutation(unittest.TestCase):
    def setUp(self):
        self.p = Placar()

    def test_checkFull_desordenado(self):
        self.assertTrue(self.p.checkFull([2, 3, 2, 3, 2]))

    def test_checkSeqMaior_desordenado(self):
        self.assertTrue(self.p.checkSeqMaior([5, 1, 4, 2, 3]))

    def test_checkQuadra_desordenado(self):
        self.assertTrue(self.p.checkQuadra([1, 5, 1, 1, 1]))

    def test_quadra_falsa_buraco_no_meio_caso_1(self):
        self.assertFalse(self.p.checkQuadra([1, 1, 1, 2, 2]))

    def test_quadra_falsa_buraco_no_meio_caso_2(self):
        self.assertFalse(self.p.checkQuadra([1, 1, 2, 2, 2]))

    def test_quadra_falsa_buraco_nas_pontas_caso_1(self):
        self.assertFalse(self.p.checkQuadra([1, 1, 2, 2, 3]))

    def test_quadra_falsa_buraco_nas_pontas_caso_2(self):
        self.assertFalse(self.p.checkQuadra([1, 2, 2, 2, 3]))

    def test_quina_falsa_intruso_inicio(self):
        self.assertFalse(self.p.checkQuina([1, 2, 2, 2, 2]))

    def test_quina_falsa_intruso_meio(self):
        self.assertFalse(self.p.checkQuina([2, 1, 2, 2, 2]))

    def test_quina_falsa_intruso_fim(self):
        self.assertFalse(self.p.checkQuina([2, 2, 2, 2, 1]))

    def test_limite_inferior_numero_1(self):
        self.p.add(1, [1, 2, 3, 4, 5]) 
        self.assertEqual(self.p.getScore(0), 1)

    def test_limite_superior_numero_6(self):
        self.p.add(6, [6, 2, 3, 4, 5])
        self.assertEqual(self.p.getScore(5), 6)

    def test_full_house_soma_correta(self):
        self.p.add(7, [1, 1, 1, 2, 2])
        self.assertEqual(self.p.getScore(6), 15)

    def test_getScore_soma_total_sem_parametro(self):
        self.p.add(1, [1, 2, 3, 4, 5])
        self.p.add(10, [5, 5, 5, 5, 5])
        self.assertEqual(self.p.getScore(), 41)


    def test_formatacao_exata_uma_linha(self):
        self.p.add(10, [6, 6, 6, 6, 6]) 
        resultado = self.p.uma_linha(9)
        self.assertEqual(resultado, " 40 ")


    def test_posicao_especial_retorna_zero_quando_condicao_falsa(self):
        self.p.add(7, [1, 2, 3, 4, 5])
        self.assertEqual(self.p.placar[6], 0)

    def test_range_inicio_correto_posicao_1(self):
        self.p.add(1, [1, 1, 1, 1, 1])
        self.assertEqual(self.p.placar[0], 5)

    def test_k_deve_ser_numerico_nao_lista(self):
        self.p.add(7, [1, 2, 3, 4, 5])
        self.assertNotIsInstance(self.p.placar[6], list)
        self.assertEqual(self.p.placar[6], 0)

    def test_posicao_7_full_invalido_retorna_zero(self):
        self.p.add(7, [1, 2, 3, 4, 5])
        self.assertEqual(self.p.placar[6], 0)

    def test_posicao_8_sequencia_invalida_retorna_zero(self):
        self.p.add(8, [1, 1, 1, 1, 1])
        self.assertEqual(self.p.placar[7], 0)

    def test_posicao_9_quadra_invalida_retorna_zero(self):
        self.p.add(9, [1, 2, 3, 4, 5])
        self.assertEqual(self.p.placar[8], 0)

    def test_posicao_10_quina_invalida_retorna_zero(self):
        self.p.add(10, [1, 2, 3, 4, 5])
        self.assertEqual(self.p.placar[9], 0)

    def test_taken_deve_ser_boolean_true(self):
        self.p.add(1, [1, 1, 1, 1, 1])
        self.assertTrue(self.p.taken[0])
        self.assertIsInstance(self.p.taken[0], bool)

    def test_checkFull_primeira_parte_v1_diferente_v2(self):
        self.assertFalse(self.p.checkFull([1, 1, 2, 2, 2]))

    def test_checkFull_segunda_parte_v0_igual_v1_true(self):
        self.assertTrue(self.p.checkFull([1, 1, 1, 2, 2]))

    def test_checkFull_segunda_parte_v0_igual_v1_invertido(self):
        self.assertTrue(self.p.checkFull([2, 2, 2, 1, 1]))

    def test_checkFull_segunda_parte_v2_diferente_v3(self):
        self.assertFalse(self.p.checkFull([1, 1, 2, 2, 3]))

    def test_checkFull_segunda_parte_v3_diferente_v4(self):
        self.assertFalse(self.p.checkFull([1, 1, 2, 3, 3]))

    def test_checkFull_sem_par_v0_v1(self):
        self.assertFalse(self.p.checkFull([1, 2, 2, 3, 3]))

    def test_checkFull_v3_diferente_v4_sem_trinca(self):
        self.assertFalse(self.p.checkFull([1, 1, 1, 2, 3]))

    def test_checkFull_v0_diferente_v1_sem_trinca(self):
        self.assertFalse(self.p.checkFull([1, 2, 2, 2, 3]))

    def test_checkFull_v0_maior_v1_invalido(self):
        self.assertFalse(self.p.checkFull([2, 1, 1, 1, 1]))

    def test_checkSeqMaior_v4_sequencia_completa(self):
        self.assertTrue(self.p.checkSeqMaior([1, 2, 3, 4, 5]))

    def test_checkSeqMaior_v0_v1_quebrada(self):
        self.assertFalse(self.p.checkSeqMaior([1, 3, 4, 5, 6]))

    def test_checkSeqMaior_v1_v2_quebrada(self):
        self.assertFalse(self.p.checkSeqMaior([1, 2, 4, 5, 6]))

    def test_checkSeqMaior_v2_v3_quebrada(self):
        self.assertFalse(self.p.checkSeqMaior([1, 2, 3, 5, 6]))

    def test_checkSeqMaior_v3_v4_quebrada(self):
        self.assertFalse(self.p.checkSeqMaior([1, 2, 3, 4, 6]))

    def test_checkQuadra_primeira_v1_diferente_v2(self):
        self.assertFalse(self.p.checkQuadra([1, 2, 2, 2, 3]))

    def test_checkQuadra_primeira_v2_diferente_v3_false(self):
        self.assertFalse(self.p.checkQuadra([1, 1, 1, 2, 2]))

    def test_checkQuadra_primeira_v2_igual_v3_true(self):
        self.assertTrue(self.p.checkQuadra([1, 1, 1, 1, 2]))

    def test_checkQuadra_segunda_v1_quadra_valida(self):
        self.assertTrue(self.p.checkQuadra([1, 2, 2, 2, 2]))

    def test_checkQuadra_segunda_v3_diferente_v4(self):
        self.assertFalse(self.p.checkQuadra([1, 2, 2, 2, 3]))

    def test_checkQuadra_v0_diferente_v1_false(self):
        self.assertFalse(self.p.checkQuadra([1, 2, 2, 2, 2]))

    def test_checkQuadra_v1_diferente_v2_false(self):
        self.assertFalse(self.p.checkQuadra([1, 1, 2, 2, 2]))

    def test_checkQuadra_v2_diferente_v3_false(self):
        self.assertFalse(self.p.checkQuadra([1, 1, 1, 2, 2]))

    def test_checkQuina_v1_diferente_v2(self):
        self.assertFalse(self.p.checkQuina([1, 2, 2, 2, 2]))

    def test_checkQuina_v2_diferente_v3(self):
        self.assertFalse(self.p.checkQuina([1, 1, 2, 2, 2]))

    def test_checkQuina_v2_todas_iguais_true(self):
        self.assertTrue(self.p.checkQuina([1, 1, 1, 1, 1]))

    def test_checkQuina_v3_diferente_v4(self):
        self.assertFalse(self.p.checkQuina([1, 1, 1, 2, 2]))

    def test_checkQuina_v0_diferente_ultima(self):
        self.assertFalse(self.p.checkQuina([1, 2, 2, 2, 2]))

    def test_checkQuina_v1_diferente_ultima(self):
        self.assertFalse(self.p.checkQuina([1, 1, 2, 2, 2]))

    def test_checkQuina_v2_diferente_ultima(self):
        self.assertFalse(self.p.checkQuina([1, 1, 1, 2, 2]))

    def test_uma_linha_i_8_mostra_posicao_9(self):
        resultado = self.p.uma_linha(8)
        self.assertIn("(9)", resultado)

    def test_uma_linha_i_9_mostra_posicao_10(self):
        resultado = self.p.uma_linha(9)
        self.assertIn("(10)", resultado)

    def test_add_posicao_6_full_valido(self):
        self.p.add(6, [1, 1, 1, 2, 2])
        self.assertEqual(self.p.placar[5], 6)

    def test_add_posicao_7_invalido_retorna_zero(self):
        self.p.add(7, [1, 2, 3, 4, 5])
        self.assertEqual(self.p.placar[6], 0)

    def test_add_posicao_8_invalido_retorna_zero(self):
        self.p.add(8, [1, 1, 1, 2, 2])
        self.assertEqual(self.p.placar[7], 0)
