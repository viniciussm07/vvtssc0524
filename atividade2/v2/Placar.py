class ComputaPlacar:
    def __init__(self):
        self.jogadas = []
        self.placar = 0

    def calcula_placar(self, s: str) -> int:
        self.jogadas = self._parse_jogadas(s)
        self.placar = 0
        
        i = 0
        for frame in range(10):
            if i >= len(self.jogadas):
                break
                
            if self._is_strike(i):
                self.placar += 10 + self._strike_bonus(i)
                i += 1
            elif self._is_spare(i):
                self.placar += 10 + self._spare_bonus(i)
                i += 2
            else:
                self.placar += self._valor_pinos(self.jogadas[i]) + self._valor_pinos(self.jogadas[i+1])
                i += 2
        
        return self.placar

    def _parse_jogadas(self, s: str) -> list:
        return list(s.replace("-", "0"))

    def _is_strike(self, i: int) -> bool:
        return i < len(self.jogadas) and self.jogadas[i] == "X"

    def _is_spare(self, i: int) -> bool:
        return (i + 1 < len(self.jogadas) and 
                self.jogadas[i + 1] == "/")

    def _strike_bonus(self, i: int) -> int:
        bonus = 0
        if i + 1 < len(self.jogadas):
            bonus += self._valor_pinos(self.jogadas[i + 1])
        if i + 2 < len(self.jogadas):
            if self.jogadas[i + 2] == "/":
                bonus = 10
            else:
                bonus += self._valor_pinos(self.jogadas[i + 2])
        return bonus

    def _spare_bonus(self, i: int) -> int:
        if i + 2 < len(self.jogadas):
            return self._valor_pinos(self.jogadas[i + 2])
        return 0

    def _valor_pinos(self, jogada: str) -> int:
        if jogada == "X":
            return 10
        elif jogada.isdigit():
            return int(jogada)
        else:
            return 0