
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