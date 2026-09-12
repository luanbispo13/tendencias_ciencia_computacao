Atividade de Fixação: Meu Primeiro Repositório — Engenharia de Prompt

Disciplina: Tendências em Ciência da Computação  
Professora: Kadidja Valéria Reginaldo de Oliveira  
Aluno: Luan Bispo Silva  
Matrícula: 32635648  
Ferramenta de IA generativa utilizada: Google Gemini, modelo Gemini 2.5 Flash  

---

## Introdução

Este documento apresenta a resolução da Atividade de Fixação da Unidade I — Fundamentos de IA e Engenharia de Prompt, estruturada para compor o arquivo `README.md` do repositório público do GitHub intitulado `engenharia-de-prompt-fundamentos`. O objetivo principal é exercitar na prática a transição de comandos vagos para comandos técnicos estruturados, demonstrando como a formulação orientada a componentes reduz ambiguidades, previne alucinações e eleva o nível técnico da resposta gerada por Modelos de Linguagem de Grande Porte (LLMs).

---

## 1. Passo 1: Repositório Criado

* **Nome do Repositório:** `unidade1`
* **Visibilidade:** Pública
* **Plataforma:** GitHub
* **Finalidade:** Hospedagem da documentação experimental comparativa entre prompts genéricos e estruturados.

---

## 2. Passo 2: Comparação Prática (README.md)

### 2.1. Experimento com Prompt Genérico

* **Comando enviado (Prompt Genérico):**
```text
O que é Machine Learning?
```

* **Resposta gerada pela IA:**
```text
Machine Learning (ou Aprendizado de Máquina) é uma área da inteligência artificial 
que permite que computadores aprendam a partir de dados sem serem explicitamente 
programados. Em vez de regras fixas escritas por humanos, o algoritmo analisa grandes 
volumes de informação, identifica padrões matemáticos e faz previsões ou toma decisões 
por conta própria. É amplamente utilizado em filtros de spam, recomendações de filmes, 
carros autônomos e diagnósticos médicos.
```

---

### 2.2. Experimento com Prompt Estruturado

* **Fórmula aplicada:** `[Papel / Persona]` + `[Objetivo / Instrução]` + `[Contexto]` + `[Restrições / Formato]`

* **Comando enviado (Prompt Estruturado):**
```text
## [Papel / Persona]
Atue como um professor experiente e didático de Ciência da Computação.

## [Contexto]
Você está explicando fundamentos de tecnologia para um aluno iniciante que gosta muito de esportes, mas não possui familiaridade com matemática avançada ou código.

## [Objetivo]
Explique o conceito de Machine Learning utilizando uma analogia prática com futebol ou basquete.

## [Restrições / Formato]
- Limite a resposta a exatamente 2 parágrafos.
- Mantenha tom encorajador e linguagem acessível, evitando jargões técnicos complexos sem explicação.
- Idioma: Português do Brasil.
```

* **Resposta gerada pela IA:**
```text
Pense no Machine Learning como o treinamento de um jogador de basquete arremessando lances livres. Na programação tradicional, um técnico desenharia um manual com regras milimétricas estáticas — o ângulo exato do cotovelo e a força nos pulsos — e o jogador tentaria apenas obedecer cegamente a essas ordens. No Machine Learning, o processo é diferente: a máquina é como um novato que arremessa a bola à cesta milhares de vezes; a cada tentativa falha ou certeira, ela observa o resultado, ajusta a postura e descobre por conta própria o arco perfeito para pontuar com precisão.

Com o passar do tempo e centenas de repetições, esse "atleta virtual" já não precisa pensar nas instruções iniciais do técnico, pois desenvolveu memória muscular estatística a partir dos erros e acertos do treino. Em termos de computação, os lances livres passados são os dados, as cestas convertidas são os acertos que moldam o modelo e a melhora progressiva do atleta durante a temporada é o aprendizado de máquina em pleno funcionamento, pronto para encarar partidas contra qualquer adversário inédito.
```

---

## 3. Passo 3: Análise Crítica

A resposta gerada pelo **Prompt Estruturado** foi significativamente mais útil, didática e assertiva. Enquanto o prompt genérico gerou uma resposta enciclopédica correta, porém fria, impessoal e repleta de termos abstratos comuns da internet, o prompt estruturado converteu a explicação em uma narrativa palpável e imersiva. 

A inclusão explícita do **papel**, do **contexto de recepção** e do **formato com restrições** eliminou completamente as ambiguidades:
1. **Controle de Escopo e Tom:** Ao definir a persona e o público esportista, a IA abandonou definições secas e articulou uma metáfora contínua (arremessos como dados de treino e calibragem como ajuste de pesos sinápticos).
2. **Previsibilidade Estrutural:** A imposição de limites precisos (exatamente dois parágrafos) impediu respostas prolixas e dispersas, garantindo síntese cirúrgica.
3. **Redução de Ruído (*Lixo In, Lixo Out*):** O prompt detalhado operou como uma restrição matemática ao espaço vetorial probabilístico do modelo, direcionando a predição de tokens para um vocabulário motivador, rigorosamente adaptado ao nível iniciante do estudante.

---

## 4. Passo 4: Link de Entrega

* **Link do Repositório GitHub:** `https://github.com/luanbisposilva/engenharia-de-prompt-fundamentos`
* **Status da Submissão:** Documentação integrada e pronta para envio via Blackboard UDF.

---

## Declaração de uso de Inteligência Artificial

Em conformidade com as diretrizes institucionais de responsabilidade acadêmica e ética no Centro Universitário do Distrito Federal (UDF), declaro que utilizei a ferramenta de IA generativa **Google Gemini (modelo Gemini 2.5 Flash)** como apoio na execução dos experimentos comparativos de prompt (genérico vs. estruturado) e na formatação das respostas documentadas neste relatório. Reafirmo a autoria intelectual deste trabalho, atestando que todo o conteúdo gerado foi criticamente testado, revisado e validado por mim antes da consolidação final.

---

## Referências

* ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6023**: informação e documentação — referências — elaboração. Rio de Janeiro: ABNT, 2018.
* ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 14724**: informação e documentação — trabalhos acadêmicos — apresentação. Rio de Janeiro: ABNT, 2011.
* BRASIL. **Lei nº 13.709, de 14 de agosto de 2018**. Lei Geral de Proteção de Dados Pessoais (LGPD). Brasília, DF: Presidência da República, 2018. Disponível em: <http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>. Acesso em: 12 set. 2026.
* GOOGLE. **Gemini** (modelo Gemini 2.5 Flash). Mountain View: Google, 2026. Disponível em: <https://gemini.google.com>. Acesso em: 12 set. 2026.
* LARGUESA, Ricardo Pupo. **Engenharia de prompt para DEVS: um guia para aprender a usar a IA antes que a IA aprenda a usar você**. 2. ed. São Paulo: Casa do Código, 2025.
* LIMA, Welton Dias de. **Aula 01 - Engenharia de Prompt, IA e Responsabilidade Acadêmica**. Brasília: Centro Universitário UDF, 2026.
* RUSSELL, Stuart; NORVIG, Peter. **Inteligência Artificial: uma abordagem moderna**. 4. ed. Rio de Janeiro: GEN LTC, 2022.
* UDF CENTRO UNIVERSITÁRIO. **Plano de Ensino: Engenharia de Prompt e Aplicações em IA**. Brasília: UDF, 2026.
