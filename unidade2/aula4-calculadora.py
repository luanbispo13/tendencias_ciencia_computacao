import random
import time
from typing import Dict, NamedTuple


class Desafio(NamedTuple):
    texto_conta: str
    resultado: int


class JogoCalculadora:
    """Gerencia o estado e as regras do Jogo da Calculadora."""

    CONFIGURACOES: Dict[int, Dict[str, object]] = {
        1: {"nome": "Facil", "max_val": 12, "ops": ["+", "-"]},
        2: {"nome": "Medio", "max_val": 30, "ops": ["+", "-", "*"]},
        3: {"nome": "Dificil", "max_val": 60, "ops": ["+", "-", "*", "/"]}
    }

    def __init__(self, rodadas: int = 5) -> None:
        self.total_rodadas = rodadas
        self.pontuacao = 0
        self.acertos = 0
        self.streak = 0
        self.maior_streak = 0
        self.nivel = 1

    def configurar_nivel(self) -> None:
        """Solicita e valida a escolha de dificuldade."""
        print("\nSelecione o nivel de dificuldade:")
        for k, v in self.CONFIGURACOES.items():
            print(f"  [{k}] {v['nome']}")
        while True:
            escolha = input("Opcao (1-3): ").strip()
            if escolha in ["1", "2", "3"]:
                self.nivel = int(escolha)
                break
            print(">> Opcao invalida. Digite 1, 2 ou 3.")

    def gerar_desafio(self) -> Desafio:
        """Gera uma operacao de acordo com o nivel selecionado."""
        cfg = self.CONFIGURACOES[self.nivel]
        max_n = int(cfg["max_val"])
        op = random.choice(list(cfg["ops"]))

        if op == "/":
            divisor = random.randint(2, 10)
            quociente = random.randint(1, 10)
            dividendo = divisor * quociente
            return Desafio(f"{dividendo} / {divisor}", quociente)
        
        n1 = random.randint(1, max_n)
        n2 = random.randint(1, max_n)

        if op == "+":
            return Desafio(f"{n1} + {n2}", n1 + n2)
        elif op == "-":
            return Desafio(f"{n1} - {n2}", n1 - n2)
        else:
            return Desafio(f"{n1} * {n2}", n1 * n2)

    def ler_resposta(self, expressao: str) -> int:
        """Garante a leitura de um inteiro sem interromper o jogo."""
        while True:
            entrada = input(f"Quanto e {expressao}? ").strip()
            try:
                return int(entrada)
            except ValueError:
                print(">> Entrada invalida. Digite um numero inteiro.")

    def avaliar_jogada(self, digitado: int, esperado: int) -> None:
        """Processa pontuacao e multiplicador de streak."""
        if digitado == esperado:
            self.acertos += 1
            self.streak += 1
            self.maior_streak = max(self.maior_streak, self.streak)
            ganho = 10 + (self.streak - 1) * 2
            self.pontuacao += ganho
            print(f"-> Correto! (+{ganho} pts) [Sequencia: {self.streak}x]")
        else:
            self.streak = 0
            print(f"-> Incorreto! O resultado correto era {esperado}.")

    def exibir_resumo(self, tempo_gasto: float) -> None:
        """Apresenta o painel final de metricas."""
        taxa = (self.acertos / self.total_rodadas) * 100
        print("\n=============================================")
        print("       RELATORIO DE DESEMPENHO")
        print("=============================================")
        print(f"Nivel Selecionado: {self.CONFIGURACOES[self.nivel]['nome']}")
        print(f"Pontuacao Final  : {self.pontuacao} pts")
        print(f"Acertos Totais   : {self.acertos}/{self.total_rodadas} ({taxa:.1f}%)")
        print(f"Maior Sequencia  : {self.maior_streak} acertos seguidos")
        print(f"Tempo de Partida : {tempo_gasto:.1f} segundos")
        print("=============================================\n")

    def iniciar(self) -> None:
        """Loop de execucao principal da partida."""
        print("=== BEM-VINDO AO JOGO DA CALCULADORA ===")
        self.configurar_nivel()
        inicio = time.time()
        for r in range(1, self.total_rodadas + 1):
            print(f"\n[Rodada {r} de {self.total_rodadas}]")
            desafio = self.gerar_desafio()
            resposta = self.ler_resposta(desafio.texto_conta)
            self.avaliar_jogada(resposta, desafio.resultado)
        self.exibir_resumo(time.time() - inicio)


if __name__ == '__main__':
    jogo = JogoCalculadora(rodadas=5)
    jogo.iniciar()