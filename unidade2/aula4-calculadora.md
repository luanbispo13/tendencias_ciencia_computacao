# Programação Assistida por IA — Mini-Projeto: Jogo da Calculadora

## Identificação
- **Nome:** Luan Bispo Silva
- **Matrícula:** 32635648
- **Turma:** Ciência da Computação — UDF
- **Data:** 17/09/2026
- **Disciplina:** Tendências em Ciência da Computação
- **Professora:** Kadidja Valéria Reginaldo de Oliveira
- **Ferramenta de IA utilizada:** Google Gemini, modelo Gemini 2.5 Flash

---

## 1. Problema
Desenvolver um jogo interativo de raciocínio lógico-matemático baseado em console ("Jogo da Calculadora"). O jogo gera desafios aritméticos dinâmicos, pontua os acertos do jogador, oferece diferentes níveis de dificuldade e trata exceções operacionais (como divisão por zero e caracteres alfabéticos).

---

## 2. Entrada
- Escolha da dificuldade no menu inicial (1 - Fácil, 2 - Médio, 3 - Difícil).
- Respostas numéricas fornecidas pelo usuário para cada expressão aritmética gerada.

---

## 3. Processamento
1. Seleção aleatória de operadores (`+`, `-`, `*`, `/`) e operandos com base no nível de dificuldade.
2. Garantia de divisões exatas (resultado inteiro) e prevenção estrita de divisão por zero.
3. Cálculo do valor exato no backend para comparação.
4. Sanitização e validação das entradas do usuário com tratamento de exceções (`ValueError`).
5. Atualização da pontuação com sistema de bonificação por sequência de acertos (*streak*).

---

## 4. Saída esperada
- Feedback imediato a cada jogada (indicação de acerto/erro e pontuação adquirida).
- Painel final consolidado com total de pontos, taxa percentual de acerto e maior sequência alcançada.

---

## 5. Prompt utilizado

```text
PAPEL:
Atue como um desenvolvedor Python focado em lógica de programação e jogos educativos.

CONTEXTO:
Sou estudante de Ciência da Computação e estou desenvolvendo o mini-projeto 'Calculadora Simples/Jogo da Calculadora' da Unidade II (Programação Assistida por IA).

PROBLEMA:
Criar um jogo interativo no terminal onde o usuário resolve contas matemáticas geradas aleatoriamente e acumula pontos.

ENTRADA:
Respostas inteiras digitadas pelo jogador via terminal.

SAÍDA ESPERADA:
Feedback a cada questão e pontuação final acumulada.

LINGUAGEM E TECNOLOGIA:
Python 3 (módulos nativos).

RESTRIÇÕES:
- Operações: +, -, * e /.
- Na divisão, garantir quociente inteiro e evitar divisão por zero.
- Tratar exceções de entrada para evitar parada súbita do programa.

FORMATO:
Código funcional limpo com função de geração de contas e loop principal de jogo.
```

---

## 6. Código inicial

```python
import random

def gerar_pergunta():
    operadores = ['+', '-', '*', '/']
    op = random.choice(operadores)
    if op == '/':
        b = random.randint(1, 10)
        res = random.randint(1, 10)
        a = b * res
    else:
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        if op == '+':
            res = a + b
        elif op == '-':
            res = a - b
        else:
            res = a * b
    return a, op, b, res

def jogar():
    pontos = 0
    print('=== JOGO DA CALCULADORA ===')
    for i in range(5):
        a, op, b, correta = gerar_pergunta()
        print(f'Questao {i+1}: Quanto e {a} {op} {b}?')
        try:
            resp = int(input('Sua resposta: '))
            if resp == correta:
                print('Correto! +10 pts')
                pontos += 10
            else:
                print(f'Incorreto! Era {correta}.')
        except ValueError:
            print('Entrada invalida! Digite apenas inteiros.')
    print(f'Fim! Pontos: {pontos}')

if __name__ == '__main__':
    jogar()
```

---

## 7. Análise crítica

- **Compreensão e Funcionamento:** O código foi compreendido e atende ao requisito básico de funcionamento em console.
- **Fragilidades Técnicas Identificadas:**
  - **Usabilidade punitiva:** Se o jogador digita acidentalmente uma letra, a exceção `ValueError` é capturada, mas a pergunta é dada como encerrada, queimando a rodada.
  - **Ausência de progressão de dificuldade:** Os valores gerados são sempre aleatórios em faixas estáticas.
  - **Baixa coesão:** Lógica de interface com o usuário, regras matemáticas e acúmulo de pontos estão misturadas em uma única função imperativa.

---

## 8. Casos de teste

### Teste 1: Caso normal (Respostas corretas sequenciais)
- **Entrada:** Valores inteiros correspondentes aos cálculos.
- **Resultado esperado:** Incremento linear de 10 pontos por acerto.
- **Avaliação:** Sucesso funcional.

### Teste 2: Caso limite (Divisão por zero e dízimas)
- **Entrada:** Questões com o operador `/`.
- **Comportamento observado:** O artifício `a = b * res` gerou dividendos múltiplos exatos do divisor `b`, evitando divisão por zero e resultados fracionários.
- **Avaliação:** Sucesso na regra aritmética.

### Teste 3: Caso de erro (Entrada inválida)
- **Entrada:** Digitação de `abc` ou pressionar Enter sem valor.
- **Comportamento observado:** O programa exibiu a mensagem de erro, mas avançou para a rodada seguinte sem permitir nova tentativa para aquela questão.
- **Avaliação:** Falha na usabilidade do fluxo interativo.

---

## 9. Problemas encontrados

1. Queima de rodada em entradas com erro de digitação.
2. Falta de classes para controle de estado do jogo.
3. Ausência de níveis de dificuldade configuráveis.
4. Ausência de cálculo de taxa percentual de precisão.

---

## 10. Prompt de refatoração

```text
Atue como Tech Lead em Python.
Refatore o Jogo da Calculadora para um nível profissional.

REQUISITOS DE REFATORAÇÃO:
1. Arquitetura: Utilize Orientação a Objetos (classe JogoCalculadora) com type hints e docstrings.
2. Níveis: Permita selecionar Fácil (+ e - com números até 12), Médio (+, - e * com números até 30) e Difícil (+, -, * e / com números até 60).
3. Resiliência: Em caso de entrada inválida, repita a pergunta sem queimar a rodada.
4. Sistema de Streak: Adicione bônus para acertos consecutivos e exiba relatório estatístico completo ao final.
```

---

## 11. Código refatorado

```python
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
```

---

## 12. Comparação

| Critério | Versão Inicial | Versão Refatorada |
|---|:---:|:---:|
| Funcionamento correto | 4 | 5 |
| Clareza | 3 | 5 |
| Organização | 2 | 5 |
| Legibilidade | 3 | 5 |
| Tratamento de erros | 2 | 5 |
| Facilidade de manutenção | 2 | 5 |

---

## 13. Reflexão

- **Onde a IA mais ajudou?**  
  Na estruturação do esqueleto orientado a objetos e na matemática para garantir divisões inteiras sem restos fracionários.
- **Onde a IA errou?**  
  No primeiro código, a IA avançava o loop mesmo quando o input era inválido, encerrando a questão do usuário indevidamente.
- **O que precisei modificar?**  
  Adicionei um loop de validação em `ler_resposta()` para manter o jogador na mesma rodada até que digite um número válido, além de organizar os níveis de dificuldade e as métricas de tempo e precisão.
- **Consigo explicar o código?**  
  Sim. O código utiliza encapsulamento com `JogoCalculadora`, tuplas imutáveis `NamedTuple` para os desafios e funções puras para avaliação de acertos.

---

## 14. Take Away

Programar com IA não significa **aceitar passivamente o primeiro rascunho de código gerado. Significa assumir o papel de Tech Lead do processo, avaliando criticamente o código da máquina, identificando falhas de usabilidade e guiando a refatoração até obter um software robusto, legível e seguro.**
