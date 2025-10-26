class ComputaPlacar:
    def __init__(self):
        self.jogadas = []
        self.placar = 0

    def calcula_placar(self, s: str) -> int:
        self.jogadas = self._parse_jogadas(s)
        self._validate_jogadas()
        self.placar = 0
        
        i = 0
        for frame in range(9):
            if i >= len(self.jogadas):
                break
                
            if self._is_strike(i):
                self.placar += 10 + self._strike_bonus(i)
                i += 1
            elif self._is_spare(i):
                self.placar += 10 + self._spare_bonus(i)
                i += 2
            else:
                primeiro = self._valor_pinos(self.jogadas[i]) if i < len(self.jogadas) else 0
                segundo = self._valor_pinos(self.jogadas[i+1]) if i+1 < len(self.jogadas) else 0
                self.placar += primeiro + segundo
                i += 2
        
        if i < len(self.jogadas):
            self.placar += self._calcular_decimo_frame(i)
        
        return self.placar

    def _calcular_decimo_frame(self, i: int) -> int:
        pontos = 0
        jogadas_restantes = len(self.jogadas) - i
        
        if jogadas_restantes == 0:
            return 0
        
        primeira_jogada = self.jogadas[i]
        primeiro_valor = self._valor_pinos(primeira_jogada)
        
        if primeira_jogada == "X":
            pontos += 10
            if jogadas_restantes > 1:
                segunda_jogada = self.jogadas[i + 1]
                segundo_valor = self._valor_pinos(segunda_jogada)
                pontos += segundo_valor
                
                if jogadas_restantes > 2:
                    terceira_jogada = self.jogadas[i + 2]
                    if terceira_jogada == "/":
                        pontos += (10 - segundo_valor)
                    else:
                        pontos += self._valor_pinos(terceira_jogada)
        else:
            pontos += primeiro_valor
            
            if jogadas_restantes > 1:
                segunda_jogada = self.jogadas[i + 1]
                
                if segunda_jogada == "/":
                    pontos += (10 - primeiro_valor)
                    
                    if jogadas_restantes > 2:
                        pontos += self._valor_pinos(self.jogadas[i + 2])
                else:
                    pontos += self._valor_pinos(segunda_jogada)
        
        return pontos

    def _parse_jogadas(self, s: str) -> list:
        if not s:
            raise ValueError("String de jogadas não pode estar vazia")
        s_limpa = s.replace("-", "")
        return list(s_limpa)

    def _validate_jogadas(self):
        for i, jogada in enumerate(self.jogadas):
            if jogada not in "X0123456789/":
                raise ValueError(f"Jogada inválida '{jogada}' na posição {i}")
        
        for i, jogada in enumerate(self.jogadas):
            if jogada == "/" and i == 0:
                raise ValueError("Spare não pode ser a primeira jogada")

    def _is_strike(self, i: int) -> bool:
        return i < len(self.jogadas) and self.jogadas[i] == "X"

    def _is_spare(self, i: int) -> bool:
        return (i + 1 < len(self.jogadas) and 
                self.jogadas[i + 1] == "/")

    def _strike_bonus(self, i: int) -> int:
        bonus = 0
        
        if i + 1 < len(self.jogadas):
            primeira_bonus = self.jogadas[i + 1]
            bonus += self._valor_pinos(primeira_bonus)
            
            if i + 2 < len(self.jogadas):
                segunda_bonus = self.jogadas[i + 2]
                if segunda_bonus == "/":
                    bonus = 10
                else:
                    bonus += self._valor_pinos(segunda_bonus)
        
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