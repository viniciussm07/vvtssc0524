# ===MATA MUTANTE 1216====
def test_posicao_9_quadra():
    from placar import Placar
    p = Placar()
    dados = [4, 4, 4, 4, 2]  
    p.add(9, dados)
    assert p.placar[8] == 30  
def test_posicao_9_sem_quadra():
    from placar import Placar
    p = Placar()
    dados = [1, 2, 3, 4, 5]   
    p.add(9, dados)
    assert p.placar[8] == 0


# ==EQUIVALENTE MUTANTE 1212==
def test_posicao_7_full():
    from placar import Placar
    p = Placar()
    dados = [2,2,2,3,3]  
    p.add(7, dados)
    assert p.placar[6] == 15  


# ==1208==
def test_posicao_1_com_dados():
    from placar import Placar
    p = Placar()
    dados = [1,1,2,3,4]  
    p.add(1, dados)
    assert p.placar[0] == 1


# # ===MATA MUTANTES QUE MUDAM k=0 PARA OUTROS VALORES (79, 302, 530, etc.)===
# def test_posicao_7_sem_full_k_deve_ser_0():
#     from placar import Placar
#     p = Placar()
#     dados = [1, 2, 3, 4, 5]  # Não é full
#     p.add(7, dados)
#     assert p.placar[6] == 0  # Deve ser 0, não 1, -1, ou dados

# def test_posicao_8_sem_seq_k_deve_ser_0():
#     from placar import Placar
#     p = Placar()
#     dados = [1, 1, 2, 3, 4]  # Não é sequência
#     p.add(8, dados)
#     assert p.placar[7] == 0  # Deve ser 0

# def test_posicao_10_sem_quina_k_deve_ser_0():
#     from placar import Placar
#     p = Placar()
#     dados = [4, 4, 4, 4, 5]  # Não é quina
#     p.add(10, dados)
#     assert p.placar[9] == 0  # Deve ser 0


# # ===MATA MUTANTE 80 (range(1,7) -> range(0,7))===
# def test_posicao_1_deve_funcionar():
#     from placar import Placar
#     p = Placar()
#     dados = [1, 2, 3, 4, 5]
#     p.add(1, dados)
#     assert p.placar[0] == 1  # Deve contar 1 um


# # ===MATA MUTANTES QUE MUDAM posicao == 7 (83, 84)===
# def test_posicao_7_full_deve_ser_15():
#     from placar import Placar
#     p = Placar()
#     dados = [2, 2, 2, 3, 3]  # Full
#     p.add(7, dados)
#     assert p.placar[6] == 15  # Deve ser 15, não tratar como posição 0 ou 1


# # ===MATA MUTANTE 85 (k=15 -> k=1)===
# def test_posicao_7_full_valor_correto():
#     from placar import Placar
#     p = Placar()
#     dados = [1, 1, 1, 2, 2]  # Full
#     p.add(7, dados)
#     assert p.placar[6] == 15  # Deve ser 15, não 1


# # ===MATA MUTANTES EM checkFull (1017, 1018, etc.)===
# def test_checkFull_primeira_condicao():
#     from placar import Placar
#     p = Placar()
#     # Testa primeira condição: v[0]==v[1] and v[1]==v[2] and v[3]==v[4]
#     dados = [3, 3, 3, 4, 4]
#     assert p.checkFull(dados) == True

# def test_checkFull_segunda_condicao():
#     from placar import Placar
#     p = Placar()
#     # Testa segunda condição: v[0]==v[1] and v[2]==v[3] and v[3]==v[4]
#     dados = [2, 2, 4, 4, 4]
#     assert p.checkFull(dados) == True

# def test_checkFull_nao_full():
#     from placar import Placar
#     p = Placar()
#     dados = [1, 1, 2, 3, 4]
#     assert p.checkFull(dados) == False


# # ===MATA MUTANTES EM uma_linha (1049, 1050, etc.)===
# def test_uma_linha_posicao_9():
#     from placar import Placar
#     p = Placar()
#     # Testa que i==9 funciona corretamente (não i>=9 ou i<9)
#     result = p.uma_linha(9)
#     assert result == "(10)"  # Deve ser (10), não usar formatação de outras posições

# def test_uma_linha_posicao_8():
#     from placar import Placar
#     p = Placar()
#     # Testa que posição 8 não é tratada como 9
#     result = p.uma_linha(8)
#     assert result == "(9) "  # Deve ser (9) com espaço, não (10)


# # ===MATA MUTANTES QUE MUDAM VALORES EM add (86, 87, 100-117, etc.)===
# def test_posicao_8_seq_valor_correto():
#     from placar import Placar
#     p = Placar()
#     dados = [2, 3, 4, 5, 6]  # Sequência
#     p.add(8, dados)
#     assert p.placar[7] == 20  # Deve ser 20, não outros valores

# def test_posicao_8_sem_seq_valor_zero():
#     from placar import Placar
#     p = Placar()
#     dados = [1, 2, 3, 4, 6]  # Não é sequência completa
#     p.add(8, dados)
#     assert p.placar[7] == 0  # Deve ser 0

# def test_posicao_10_quina_valor_correto():
#     from placar import Placar
#     p = Placar()
#     dados = [5, 5, 5, 5, 5]  # Quina
#     p.add(10, dados)
#     assert p.placar[9] == 40  # Deve ser 40, não outros valores


# # ===MATA MUTANTES EM checkQuadra===
# def test_checkQuadra_primeira_condicao():
#     from placar import Placar
#     p = Placar()
#     # Testa primeira condição: v[0]==v[1] and v[1]==v[2] and v[2]==v[3]
#     dados = [3, 3, 3, 3, 4]
#     assert p.checkQuadra(dados) == True

# def test_checkQuadra_segunda_condicao():
#     from placar import Placar
#     p = Placar()
#     # Testa segunda condição: v[1]==v[2] and v[2]==v[3] and v[3]==v[4]
#     dados = [2, 3, 3, 3, 3]
#     assert p.checkQuadra(dados) == True

# def test_checkQuadra_nao_quadra():
#     from placar import Placar
#     p = Placar()
#     dados = [1, 1, 2, 2, 3]
#     assert p.checkQuadra(dados) == False


# # ===MATA MUTANTES EM checkSeqMaior===
# def test_checkSeqMaior_sequencia_completa():
#     from placar import Placar
#     p = Placar()
#     dados = [1, 2, 3, 4, 5]
#     assert p.checkSeqMaior(dados) == True

# def test_checkSeqMaior_nao_sequencia():
#     from placar import Placar
#     p = Placar()
#     dados = [1, 2, 3, 4, 6]  # Falta o 5
#     assert p.checkSeqMaior(dados) == False


# # ===MATA MUTANTES EM checkQuina===
# def test_checkQuina_quina():
#     from placar import Placar
#     p = Placar()
#     dados = [6, 6, 6, 6, 6]
#     assert p.checkQuina(dados) == True

# def test_checkQuina_nao_quina():
#     from placar import Placar
#     p = Placar()
#     dados = [5, 5, 5, 5, 6]  # Quatro iguais, não cinco
#     assert p.checkQuina(dados) == False


# # ===MATA MUTANTES QUE MUDAM RANGES (158, 159, 162, etc.)===
# def test_posicoes_1_a_6_todas_funcionam():
#     from placar import Placar
#     p = Placar()
#     # Testa que todas as posições 1-6 funcionam corretamente
#     for pos in range(1, 7):
#         dados = [pos] * 2 + [1, 2, 3]  # Dois do número da posição
#         p.add(pos, dados)
#         assert p.placar[pos-1] == pos * 2  # Deve ser pos * 2


# # ===MATA MUTANTES QUE MUDAM VALORES ESPECÍFICOS (169, 173, etc.)===
# def test_posicao_2_valor_correto():
#     from placar import Placar
#     p = Placar()
#     dados = [2, 2, 2, 3, 4]  # Três 2's
#     p.add(2, dados)
#     assert p.placar[1] == 6  # Deve ser 2 * 3 = 6

# def test_posicao_3_valor_correto():
#     from placar import Placar
#     p = Placar()
#     dados = [3, 3, 1, 2, 4]  # Dois 3's
#     p.add(3, dados)
#     assert p.placar[2] == 6  # Deve ser 3 * 2 = 6

# def test_posicao_4_valor_correto():
#     from placar import Placar
#     p = Placar()
#     dados = [4, 4, 4, 4, 1]  # Quatro 4's
#     p.add(4, dados)
#     assert p.placar[3] == 16  # Deve ser 4 * 4 = 16

# def test_posicao_5_valor_correto():
#     from placar import Placar
#     p = Placar()
#     dados = [5, 5, 1, 2, 3]  # Dois 5's
#     p.add(5, dados)
#     assert p.placar[4] == 10  # Deve ser 5 * 2 = 10

# def test_posicao_6_valor_correto():
#     from placar import Placar
#     p = Placar()
#     dados = [6, 6, 6, 1, 2]  # Três 6's
#     p.add(6, dados)
#     assert p.placar[5] == 18  # Deve ser 6 * 3 = 18


# # ===MATA MUTANTE 158 (v[0]==v[1] -> v[0]==v[0] em checkFull)===
# def test_checkFull_primeira_condicao_v0_v1_importante():
#     from placar import Placar
#     p = Placar()
#     # Testa que v[0]==v[1] é necessário (não v[0]==v[0] que sempre é True)
#     dados = [1, 2, 2, 3, 3]  # v[0]!=v[1], mas v[1]==v[2] e v[3]==v[4]
#     assert p.checkFull(dados) == False  # Não é full porque v[0]!=v[1]


# # ===MATA MUTANTE 216 (v[0]==v[1] -> v[0]==v[0] em checkQuadra)===
# def test_checkQuadra_primeira_condicao_v0_v1_importante():
#     from placar import Placar
#     p = Placar()
#     # Testa que v[0]==v[1] é necessário (não v[0]==v[0] que sempre é True)
#     dados = [1, 2, 2, 2, 2]  # v[0]!=v[1], mas v[1]==v[2]==v[3]==v[4]
#     assert p.checkQuadra(dados) == True  # É quadra na segunda condição
#     # Mas se mudarmos v[0]==v[1] para v[0]==v[0], o teste falhará


# # ===MATA MUTANTE 304 (k=0 -> k=posicao)===
# def test_posicao_7_sem_full_k_nao_deve_ser_posicao():
#     from placar import Placar
#     p = Placar()
#     dados = [1, 2, 3, 4, 5]  # Não é full
#     p.add(7, dados)
#     assert p.placar[6] == 0  # Deve ser 0, não 7 (posicao)


# # ===MATA MUTANTE 1065 (posicao == 7 -> posicao < 7)===
# def test_posicao_7_exata():
#     from placar import Placar
#     p = Placar()
#     dados = [2, 2, 2, 3, 3]  # Full
#     p.add(7, dados)
#     assert p.placar[6] == 15  # Deve ser 15, não tratar posições < 7 como full


# # ===MATA MUTANTE 1021 (remove parte da condição checkFull)===
# def test_checkFull_ambas_condicoes_necessarias():
#     from placar import Placar
#     p = Placar()
#     # Testa que ambas as condições são necessárias
#     dados = [1, 1, 1, 2, 2]  # Primeira condição: v[0]==v[1]==v[2] e v[3]==v[4]
#     assert p.checkFull(dados) == True
#     dados2 = [1, 1, 2, 2, 2]  # Segunda condição: v[0]==v[1] e v[2]==v[3]==v[4]
#     assert p.checkFull(dados2) == True


# # ===MATA MUTANTES QUE MUDAM OPERADORES EM checkSeqMaior===
# def test_checkSeqMaior_todas_condicoes_necessarias():
#     from placar import Placar
#     p = Placar()
#     # Testa que todas as condições v[i]+1 == v[i+1] são necessárias
#     dados = [1, 2, 3, 4, 5]
#     assert p.checkSeqMaior(dados) == True
#     dados2 = [1, 2, 3, 4, 6]  # Falta o 5
#     assert p.checkSeqMaior(dados2) == False
#     dados3 = [1, 2, 4, 5, 6]  # Falta o 3
#     assert p.checkSeqMaior(dados3) == False


# # ===MATA MUTANTES QUE MUDAM OPERADORES EM checkQuina===
# def test_checkQuina_todas_condicoes_necessarias():
#     from placar import Placar
#     p = Placar()
#     # Testa que todas as condições v[i]==v[i+1] são necessárias
#     dados = [5, 5, 5, 5, 5]
#     assert p.checkQuina(dados) == True
#     dados2 = [5, 5, 5, 5, 6]  # Quatro iguais, não cinco
#     assert p.checkQuina(dados2) == False


# # ===MATA MUTANTES QUE MUDAM VALORES ESPECÍFICOS (100-117)===
# def test_posicao_7_full_valor_15_especifico():
#     from placar import Placar
#     p = Placar()
#     dados = [3, 3, 3, 4, 4]  # Full
#     p.add(7, dados)
#     assert p.placar[6] == 15  # Deve ser exatamente 15

# def test_posicao_8_seq_valor_20_especifico():
#     from placar import Placar
#     p = Placar()
#     dados = [1, 2, 3, 4, 5]  # Sequência
#     p.add(8, dados)
#     assert p.placar[7] == 20  # Deve ser exatamente 20

# def test_posicao_9_quadra_valor_30_especifico():
#     from placar import Placar
#     p = Placar()
#     dados = [4, 4, 4, 4, 1]  # Quadra
#     p.add(9, dados)
#     assert p.placar[8] == 30  # Deve ser exatamente 30

# def test_posicao_10_quina_valor_40_especifico():
#     from placar import Placar
#     p = Placar()
#     dados = [1, 1, 1, 1, 1]  # Quina
#     p.add(10, dados)
#     assert p.placar[9] == 40  # Deve ser exatamente 40


# # ===MATA MUTANTES QUE MUDAM OPERADORES EM RANGES (162, 163, etc.)===
# def test_range_posicoes_1_a_6_exato():
#     from placar import Placar
#     p = Placar()
#     # Testa que range(1,7) funciona corretamente (não range(0,7) ou range(1,6))
#     dados = [1, 2, 3, 4, 5]
#     p.add(1, dados)
#     assert p.placar[0] == 1  # Posição 1 deve funcionar
#     p2 = Placar()
#     p2.add(6, dados)
#     assert p2.placar[5] == 0  # Posição 6 deve funcionar (sem 6 nos dados)


# # ===MATA MUTANTES QUE MUDAM OPERADORES EM CONDIÇÕES (169, 173, etc.)===
# def test_posicao_7_igual_nao_menor():
#     from placar import Placar
#     p = Placar()
#     dados = [2, 2, 2, 3, 3]  # Full
#     p.add(7, dados)
#     assert p.placar[6] == 15  # Deve ser 15, não tratar posições < 7

# def test_posicao_8_igual_nao_menor():
#     from placar import Placar
#     p = Placar()
#     dados = [2, 3, 4, 5, 6]  # Sequência
#     p.add(8, dados)
#     assert p.placar[7] == 20  # Deve ser 20, não tratar posições < 8

# def test_posicao_9_igual_nao_menor():
#     from placar import Placar
#     p = Placar()
#     dados = [4, 4, 4, 4, 1]  # Quadra
#     p.add(9, dados)
#     assert p.placar[8] == 30  # Deve ser 30, não tratar posições < 9


# # ===MATA MUTANTES QUE MUDAM ÍNDICES EM checkQuadra (217, 220, 230, etc.)===
# def test_checkQuadra_indices_corretos():
#     from placar import Placar
#     p = Placar()
#     # Testa que v[1]==v[2] é necessário (não v[0]==v[2])
#     dados = [1, 2, 2, 2, 3]  # v[0]!=v[2], mas v[1]==v[2]==v[3]
#     assert p.checkQuadra(dados) == True  # É quadra na segunda condição
#     # Mas se mudarmos v[1]==v[2] para v[0]==v[2], o teste falhará
    
#     # Testa que v[2]==v[3] é necessário (não v[0]==v[3])
#     dados2 = [1, 1, 1, 1, 2]  # v[0]==v[1]==v[2]==v[3]
#     assert p.checkQuadra(dados2) == True  # É quadra na primeira condição
#     # Mas se mudarmos v[2]==v[3] para v[0]==v[3], pode passar incorretamente
    
#     # Testa que v[1]==v[2] é necessário (não v[1]==v[3])
#     dados3 = [1, 2, 3, 3, 3]  # v[1]!=v[2], mas v[2]==v[3]==v[4]
#     assert p.checkQuadra(dados3) == False  # Não é quadra porque v[1]!=v[2]


# # ===MATA MUTANTE 532 (range(1,7) -> range(-1,7))===
# def test_range_1_7_exato_nao_negativo():
#     from placar import Placar
#     p = Placar()
#     # Testa que range(1,7) funciona corretamente (não range(-1,7))
#     dados = [1, 2, 3, 4, 5]
#     p.add(1, dados)
#     assert p.placar[0] == 1  # Posição 1 deve funcionar corretamente


# # ===MATA MUTANTE 1024 (remove v[0]+1==v[1] de checkSeqMaior)===
# def test_checkSeqMaior_primeira_condicao_necessaria():
#     from placar import Placar
#     p = Placar()
#     # Testa que v[0]+1==v[1] é necessário
#     dados = [1, 3, 4, 5, 6]  # v[0]+1 != v[1] (1+1=2 != 3)
#     assert p.checkSeqMaior(dados) == False  # Não é sequência


# # ===MATA MUTANTE 1071 (posicao == 8 -> posicao <= 8)===
# def test_posicao_8_igual_nao_menor_igual():
#     from placar import Placar
#     p = Placar()
#     # Testa que posicao == 8 funciona corretamente (não posicao <= 8)
#     dados = [1, 2, 3, 4, 5]  # Sequência
#     p.add(8, dados)
#     assert p.placar[7] == 20  # Deve ser 20
#     # Se fosse posicao <= 8, posição 7 também seria tratada como sequência
#     p2 = Placar()
#     dados2 = [2, 2, 2, 3, 3]  # Full
#     p2.add(7, dados2)
#     assert p2.placar[6] == 15  # Deve ser 15, não 20


# # ===MATA MAIS MUTANTES EM checkSeqMaior===
# def test_checkSeqMaior_todas_condicoes_sequenciais():
#     from placar import Placar
#     p = Placar()
#     # Testa que todas as condições v[i]+1 == v[i+1] são necessárias
#     dados = [1, 2, 3, 4, 5]
#     assert p.checkSeqMaior(dados) == True
#     # Testa cada condição individualmente
#     dados2 = [2, 3, 4, 5, 6]  # Falta v[0]+1==v[1] (2+1=3, mas v[0]=2)
#     assert p.checkSeqMaior(dados2) == True  # Ainda é sequência
#     # Mas se removermos v[0]+1==v[1], pode passar incorretamente para [1,3,4,5,6]


# # ===MATA MUTANTES QUE MUDAM OPERADORES EM CONDIÇÕES (1114, 1119, etc.)===
# def test_posicao_8_igual_nao_maior():
#     from placar import Placar
#     p = Placar()
#     dados = [2, 3, 4, 5, 6]  # Sequência
#     p.add(8, dados)
#     assert p.placar[7] == 20  # Deve ser 20, não tratar posições > 8

# def test_posicao_9_igual_nao_maior():
#     from placar import Placar
#     p = Placar()
#     dados = [4, 4, 4, 4, 1]  # Quadra
#     p.add(9, dados)
#     assert p.placar[8] == 30  # Deve ser 30, não tratar posições > 9


# # ===MATA MUTANTES QUE MUDAM VALORES EM checkFull (159, 162, etc.)===
# def test_checkFull_condicoes_completas():
#     from placar import Placar
#     p = Placar()
#     # Testa primeira condição completa: v[0]==v[1] and v[1]==v[2] and v[3]==v[4]
#     dados = [3, 3, 3, 4, 4]
#     assert p.checkFull(dados) == True
#     # Se qualquer parte for removida ou alterada, falhará
    
#     # Testa segunda condição completa: v[0]==v[1] and v[2]==v[3] and v[3]==v[4]
#     dados2 = [2, 2, 4, 4, 4]
#     assert p.checkFull(dados2) == True


# # ===MATA MUTANTES QUE MUDAM OPERADORES EM checkQuadra (221-259)===
# def test_checkQuadra_condicoes_completas():
#     from placar import Placar
#     p = Placar()
#     # Testa primeira condição completa: v[0]==v[1] and v[1]==v[2] and v[2]==v[3]
#     dados = [3, 3, 3, 3, 4]
#     assert p.checkQuadra(dados) == True
    
#     # Testa segunda condição completa: v[1]==v[2] and v[2]==v[3] and v[3]==v[4]
#     dados2 = [2, 3, 3, 3, 3]
#     assert p.checkQuadra(dados2) == True
    
#     # Testa que não é quadra quando condições não são satisfeitas
#     dados3 = [1, 1, 2, 2, 3]
#     assert p.checkQuadra(dados3) == False


# # ===MATA MUTANTE 1025 (remove v[1]+1==v[2] de checkSeqMaior)===
# def test_checkSeqMaior_segunda_condicao_necessaria():
#     from placar import Placar
#     p = Placar()
#     # Testa que v[1]+1==v[2] é necessário
#     dados = [1, 2, 4, 5, 6]  # v[1]+1 != v[2] (2+1=3 != 4)
#     assert p.checkSeqMaior(dados) == False  # Não é sequência


# # ===MATA MUTANTE 1088 (v[0]==v[1] -> v[0]>v[1] em checkFull)===
# def test_checkFull_v0_igual_v1_nao_maior():
#     from placar import Placar
#     p = Placar()
#     # Testa que v[0]==v[1] é necessário (não v[0]>v[1])
#     dados = [1, 1, 1, 2, 2]  # v[0]==v[1], não v[0]>v[1]
#     assert p.checkFull(dados) == True  # É full
#     # Se mudarmos para v[0]>v[1], dados ordenados sempre terão v[0]<=v[1], então sempre False


# # ===MATA MUTANTE 638 (v[0]==v[1] -> v[-1]==v[1] em checkQuadra)===
# def test_checkQuadra_v0_igual_v1_nao_vmenos1():
#     from placar import Placar
#     p = Placar()
#     # Testa que v[0]==v[1] é necessário (não v[-1]==v[1])
#     dados = [1, 1, 1, 1, 2]  # v[0]==v[1], mas v[-1]!=v[1]
#     assert p.checkQuadra(dados) == True  # É quadra
#     # Se mudarmos para v[-1]==v[1], pode passar incorretamente


# # ===MATA MUTANTE 1026 (remove v[2]+1==v[3] de checkSeqMaior)===
# def test_checkSeqMaior_terceira_condicao_necessaria():
#     from placar import Placar
#     p = Placar()
#     # Testa que v[2]+1==v[3] é necessário
#     dados = [1, 2, 3, 5, 6]  # v[2]+1 != v[3] (3+1=4 != 5)
#     assert p.checkSeqMaior(dados) == False  # Não é sequência


# # ===MATA MUTANTE 1091 (v[0]==v[1] -> v[0]<=v[1] em checkFull)===
# def test_checkFull_v0_igual_v1_nao_menor_igual():
#     from placar import Placar
#     p = Placar()
#     # Testa que v[0]==v[1] é necessário (não v[0]<=v[1])
#     # Para dados ordenados, v[0]<=v[1] sempre é True, então precisa ser ==
#     dados = [1, 2, 2, 3, 3]  # v[0]!=v[1], mas v[0]<=v[1] é True
#     assert p.checkFull(dados) == False  # Não é full porque v[0]!=v[1]


# # ===MATA MUTANTE 1093 (v[1]==v[2] -> v[1]>v[2] em checkFull)===
# def test_checkFull_v1_igual_v2_nao_maior():
#     from placar import Placar
#     p = Placar()
#     # Testa que v[1]==v[2] é necessário (não v[1]>v[2])
#     # Para dados ordenados, v[1]<=v[2] sempre, então v[1]>v[2] sempre False
#     dados = [1, 1, 1, 2, 2]  # v[1]==v[2], não v[1]>v[2]
#     assert p.checkFull(dados) == True  # É full


# # ===MATA MUTANTE 86 (k=15 -> k=0 em posição 7)===
# def test_posicao_7_full_nao_deve_ser_zero():
#     from placar import Placar
#     p = Placar()
#     dados = [2, 2, 2, 3, 3]  # Full
#     p.add(7, dados)
#     assert p.placar[6] == 15  # Deve ser 15, não 0


# # ===MATA MUTANTE 100 (k=20 -> k=1 quando não é sequência)===
# def test_posicao_8_sem_seq_nao_deve_ser_1():
#     from placar import Placar
#     p = Placar()
#     dados = [1, 2, 3, 4, 6]  # Não é sequência completa
#     p.add(8, dados)
#     assert p.placar[7] == 0  # Deve ser 0, não 1


# # ===MATA MUTANTE 162 (v[3]==v[4] -> v[0]==v[4] em checkFull)===
# def test_checkFull_v3_igual_v4_nao_v0():
#     from placar import Placar
#     p = Placar()
#     # Testa que v[3]==v[4] é necessário (não v[0]==v[4])
#     dados = [1, 1, 1, 2, 3]  # v[3]!=v[4], mas v[0]!=v[4] também
#     assert p.checkFull(dados) == False  # Não é full
#     dados2 = [1, 1, 1, 2, 2]  # v[3]==v[4], mas v[0]!=v[4]
#     assert p.checkFull(dados2) == True  # É full


# # ===MATA MUTANTE 163 (v[3]==v[4] -> v[1]==v[4] em checkFull)===
# def test_checkFull_v3_igual_v4_nao_v1():
#     from placar import Placar
#     p = Placar()
#     # Testa que v[3]==v[4] é necessário (não v[1]==v[4])
#     dados = [1, 1, 1, 2, 3]  # v[3]!=v[4], mas v[1]!=v[4] também
#     assert p.checkFull(dados) == False  # Não é full
#     dados2 = [1, 1, 1, 2, 2]  # v[3]==v[4], mas v[1]!=v[4]
#     assert p.checkFull(dados2) == True  # É full


# # ===MATA MUTANTE 164 (v[3]==v[4] -> v[2]==v[4] em checkFull)===
# def test_checkFull_v3_igual_v4_nao_v2():
#     from placar import Placar
#     p = Placar()
#     # Testa que v[3]==v[4] é necessário (não v[2]==v[4])
#     dados = [1, 1, 1, 2, 3]  # v[3]!=v[4], mas v[2]!=v[4] também
#     assert p.checkFull(dados) == False  # Não é full
#     dados2 = [1, 1, 1, 2, 2]  # v[3]==v[4], mas v[2]!=v[4]
#     assert p.checkFull(dados2) == True  # É full


# # ===MATA MUTANTES QUE MUDAM VALORES EM posicao 8 (101-104)===
# def test_posicao_8_sem_seq_valor_zero_especifico():
#     from placar import Placar
#     p = Placar()
#     dados = [1, 2, 3, 4, 6]  # Não é sequência
#     p.add(8, dados)
#     assert p.placar[7] == 0  # Deve ser 0, não 7, 15, 8, ou 20


# # ===MATA MUTANTE 105 (posicao == 9 -> posicao == 1)===
# def test_posicao_9_nao_deve_ser_tratada_como_1():
#     from placar import Placar
#     p = Placar()
#     dados = [4, 4, 4, 4, 1]  # Quadra
#     p.add(9, dados)
#     assert p.placar[8] == 30  # Deve ser 30, não tratar posição 1 como quadra


# # ===MATA MUTANTES QUE MUDAM posicao == 9 (106-117)===
# def test_posicao_9_exata_nao_outras_posicoes():
#     from placar import Placar
#     p = Placar()
#     dados = [4, 4, 4, 4, 1]  # Quadra
#     p.add(9, dados)
#     assert p.placar[8] == 30  # Deve ser 30, não tratar outras posições como quadra
#     # Testa que posição 7 não é tratada como quadra
#     p2 = Placar()
#     dados2 = [2, 2, 2, 3, 3]  # Full
#     p2.add(7, dados2)
#     assert p2.placar[6] == 15  # Deve ser 15, não 30
#     # Testa que posição 8 não é tratada como quadra
#     p3 = Placar()
#     dados3 = [1, 2, 3, 4, 5]  # Sequência
#     p3.add(8, dados3)
#     assert p3.placar[7] == 20  # Deve ser 20, não 30