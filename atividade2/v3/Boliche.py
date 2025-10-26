from Placar import ComputaPlacar

if __name__ == "__main__":

    jogadas = input("Digite a quantidades de pinos derrubados em cada jogada: (1891X-91725382126372-)")

    placar = ComputaPlacar()
    placar.calcula_placar(jogadas)