
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