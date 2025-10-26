class ComputaPlacar:
    def __init__(self):
        self.jogadas = 21 * [None]
        self.rodadas = 10
        self.placar = 0

    def calcula_placar(self, s: str):
        self.jogadas = list(s.replace("-", "0"))  
        self.placar = 0
        frame = 0
        i = 0

        while frame < self.rodadas and i < len(self.jogadas):
            jogada = self.jogadas[i]

            if jogada == "X":
                self.placar += 10
                i += 1
            elif i+1 < len(self.jogadas) and self.jogadas[i+1] == "/":
                self.placar += 10
                i += 2
            else: 
                self.placar += self._valor_pinos(jogada) + self._valor_pinos(self.jogadas[i+1]) if i+1 < len(self.jogadas) else 0
                i += 2
            frame += 1

        return self.placar

    def _valor_pinos(self, jogada: str) -> int:
        if jogada == "X":
            return 10
        elif jogada.isdigit():
            return int(jogada)
        else:
            return 0