# Aula 01 — Fundamentos de IA e Modelos Generativos
### Atividade Avaliativa A1 — Identificando a IA e Checkpoint de Compreensão

## 1. Identificação
- **Disciplina:** Tendências em Ciências da Computação
- **Unidade:** I — Fundamentos de IA e Modelos Generativos
- **Data:** 12/09/2026
- **Integrantes:** Luan Bispo Silva (32635648)
- **Valor da atividade:** 0,5 ponto
- **Ferramenta de IA generativa utilizada:** Google Gemini, modelo Gemini 2.5 Flash

## 2. Problema escolhido

### Contexto
Na disciplina de Tendências em Ciência da Computação, a Aula 01 ministrada pela Profa.
Kadidja Valéria abordou a base conceitual de Inteligência Artificial: a hierarquia entre
IA, Machine Learning (ML), Deep Learning (DL) e IA Generativa; o motor do aprendizado
(comparando a programação tradicional baseada em regras manuais com o aprendizado
automático indutivo); a regra de ouro "Garbage In, Garbage Out"; o contraste entre o
paradigma preditivo e o generativo; e os desafios de alucinação e necessidade de
pensamento crítico e engenharia de prompt. Ao final da aula, foram propostas duas
atividades complementares:
1. Uma **Atividade Prática** de mapeamento analítico de 5 tecnologias/aplicativos do
   cotidiano, respondendo a 5 perguntas estruturadas para cada um.
2. Um **Checkpoint de Compreensão** composto por 6 perguntas conceituais para validação
   dos conhecimentos adquiridos.

### Problema
O estudante precisa consolidar e aplicar os conceitos teóricos da aula tanto na análise
crítica de aplicações do dia a dia quanto na resolução conceitual e rigorosa do
checkpoint, estruturando o relatório em conformidade com as diretrizes acadêmicas.

### Objetivo
Utilizar a IA generativa como suporte para (a) identificar, analisar criticamente e
organizar o mapeamento de 5 tecnologias do cotidiano sob a ótica dos fundamentos de IA
e (b) formular respostas técnicas, fundamentadas e precisas para as 6 perguntas do
checkpoint de compreensão, validando-as contra o material de aula.

> **Por que esse caso combina os dois casos de uso da atividade?**
> A identificação empírica da IA nas ferramentas cotidianas (Atividade Prática) e a
> consolidação conceitual teórica (Checkpoint) não são tarefas isoladas: a capacidade de
> identificar os dados, benefícios e riscos nas aplicações reais decorre diretamente da
> compreensão sobre como a máquina aprende e se diferencia dos paradigmas preditivos e
> generativos. Por isso, o trabalho tratou as duas entregas como **um único fluxo de prompt**,
> garantindo coerência terminológica e rigor metodológico.

## 3. Prompt inicial

```text
Responda a atividade prática das 5 tecnologias e as 6 perguntas do checkpoint da aula 1 de IA.
```

## 4. Resultado inicial

```text
Atividade Prática:
1. Google Maps: IA no trânsito. Resolve rotas lentas. Usa GPS. Benefício: chegar mais rápido. Risco: mandar para ruas ruins.
2. Spotify: IA na recomendação. Resolve achar música boa. Usa histórico de escuta. Benefício: músicas que você gosta. Risco: tocar sempre o mesmo estilo.
3. Filtro de Spam: IA na caixa de entrada. Resolve e-mails falsos. Usa texto da mensagem. Benefício: e-mail limpo. Risco: mandar e-mail certo pro spam.
4. Apple Face ID: IA no desbloqueio. Resolve segurança do aparelho. Usa mapa do rosto. Benefício: rápido de desbloquear. Risco: falhar no escuro.
5. ChatGPT: IA no texto. Resolve demora para escrever. Usa dados da internet. Benefício: textos rápidos. Risco: alucinação.

Checkpoint:
1. IA é a área geral e Machine Learning é quando aprende com dados.
2. Preditiva prevê dados e generativa cria coisas novas.
3. Deep Learning usa redes neurais com várias camadas.
4. Os dados servem para treinar a máquina ("Garbage In, Garbage Out").
5. O prompt detalhado dá contexto para o modelo responder melhor.
6. É necessário verificar porque a IA alucina e pode inventar coisas.
```

## 5. Análise crítica

- **O que funcionou:** a IA identificou as duas solicitações da aula (a lista dos 5
  aplicativos e as 6 perguntas teóricas) e apresentou respostas corretas em sua essência.
- **O que não funcionou:** as respostas foram excessivamente telegráficas, rasas e sem
  fundamentação técnica — não refletem o nível acadêmico de um estudante de Ciência da
  Computação nem exploram os mecanismos operacionais explicados nos slides (como camadas
  ocultas, probabilidade de tokens e regras manuais vs. indução).
- **O que faltou:** numeração formal das 5 perguntas por tecnologia, detalhamento
  específico dos tipos de dados e técnicas envolvidas, contraste aprofundado entre os
  paradigmas e uma síntese estruturada em tabela comparativa.
- **O que precisa ser validado:** os riscos reais apontados (ex.: limitações biométricas e
  efeito manada no trânsito) precisavam de terminologia técnica precisa e correlação com a
  LGPD e ética algorítmica.

## 6. Prompt refinado

```text
PAPEL:
Você é um professor e pesquisador em Ciência da Computação especialista em Inteligência
Artificial, Aprendizado de Máquina e Modelos Generativos.

CONTEXTO:
Sou discente de Ciência da Computação no Centro Universitário do Distrito Federal (UDF).
A Aula 01 da Profa. Kadidja Valéria cobriu: a taxonomia (IA -> ML -> DL -> IA Generativa);
a mecânica do aprendizado (programação tradicional com regras manuais vs. machine learning
com dados e respostas conhecidas gerando regras/padrões); a regra de ouro "Garbage In,
Garbage Out"; o contraste entre IA Preditiva e IA Generativa; redes neurais profundas
(camadas de entrada, ocultas e de saída); engenharia de prompt; e o fenômeno das
alucinações exigindo pensamento crítico humano.

OBJETIVO:
Elaborar a entrega completa das atividades avaliativas da Aula 01 com rigor conceitual,
clareza e profundidade.

TAREFA:
1. Resolver a Atividade Prática selecionando 5 tecnologias cotidianas: Google Maps/Waze,
   Spotify, Filtro de Spam do Gmail, Reconhecimento Facial (Apple Face ID) e ChatGPT/Gemini.
   Para cada tecnologia, responda detalhadamente aos 5 itens do slide:
   - 1 Onde a IA está presente neste app?
   - 2 Qual problema ela procura resolver?
   - 3 Quais dados provavelmente são utilizados?
   - 4 Qual é o benefício direto para o usuário?
   - 5 Existe algum risco ou limitação observável?
   Em seguida, sintetize essas informações em uma tabela comparativa.
2. Responder de forma analítica e fundamentada às 6 questões do Checkpoint de Compreensão:
   - Qual a diferença entre IA e Machine Learning?
   - O que diferencia a IA Preditiva da Generativa?
   - O que caracteriza o Deep Learning?
   - Qual a função dos dados no aprendizado de máquina?
   - Por que um prompt detalhado gera resultados melhores?
   - Por que é necessário verificar as respostas de uma IA?

RESTRIÇÕES:
- Vocabulário técnico de Ciência da Computação, porém claro e didático.
- Conectar diretamente as respostas aos esquemas conceituais apresentados no material da aula.
- Evitar respostas monossilábicas ou superficiais.

FORMATO:
- Tópicos numerados para cada tecnologia e para o checkpoint.
- Tabela comparativa estruturada com as colunas: Tecnologia | Tipo de IA | Entrada de Dados | Saída do Modelo | Limitação Central.

CRITÉRIOS DE QUALIDADE:
- Precisão terminológica (redes neurais profundas, Transformers, probabilidades de tokens, GIGO).
- Postura crítica em relação a limitações éticas, técnicas e regulatórias (LGPD).
```

## 7. Resultado refinado

### Atividade Prática: Identificando a IA no Cotidiano

#### 1. Google Maps / Waze (Mobilidade Urbana e Roteirização)
1. **Onde a IA está presente:** No algoritmo de roteamento preditivo, no cálculo dinâmico de tempo estimado de chegada (ETA) e na detecção de padrões de lentidão e anomalias de trânsito em tempo real.
2. **Qual problema ela procura resolver:** Reduzir o tempo de deslocamento urbano e rodoviário, mitigando congestionamentos e otimizando o consumo de combustível dos motoristas.
3. **Quais dados provavelmente são utilizados:** Coordenadas de GPS em tempo real de milhões de dispositivos móveis, velocidade média de deslocamento nas vias, histórico volumétrico de tráfego por dia e horário, relatórios colaborativos da comunidade (bloqueios, obras, acidentes) e variáveis meteorológicas.
4. **Qual é o benefício direto para o usuário:** Rotas otimizadas dinamicamente com desvios automáticos de gargalos, previsibilidade exata de horários de chegada e maior segurança nos trajetos.
5. **Existe algum risco ou limitação observável:** Ocorrência do "efeito manada" (redirecionar fluxo excessivo de veículos para vias residenciais pacatas e estreitas), risco de guiar desavisadamente motoristas para áreas com altos índices de violência urbana e perda temporária de precisão em túneis e corredores de edifícios altos.

#### 2. Spotify (Sistema de Recomendação de Áudio)
1. **Onde a IA está presente:** Nos mecanismos de curadoria e recomendação personalizada (*Descobertas da Semana*, *Radar de Novidades*, rádio de faixas e mix diários), que combinam filtragem colaborativa com redes neurais de Deep Learning para análise direta do sinal espectral do áudio.
2. **Qual problema ela procura resolver:** A sobrecarga de escolha diante de um catálogo superior a 100 milhões de faixas, permitindo que o usuário descubra novos artistas com mínimo atrito de busca ativa.
3. **Quais dados provavelmente são utilizados:** Histórico de reprodução, taxas de pulo (*skips* antes dos 30 segundos), repetições, faixas curtidas, horários de acesso, listas criadas pelo próprio usuário e extração matemática de atributos do áudio (espectrogramas de frequência, tempo, dançabilidade, tom acústico).
4. **Qual é o benefício direto para o usuário:** Experiência auditiva hiperpersonalizada e fluida, facilitando o consumo passivo de novas músicas alinhadas às preferências estéticas individuais.
5. **Existe algum risco ou limitação observável:** Formação de "bolhas de filtro" (o algoritmo tende a reforçar apenas o mesmo nicho sonoro, empobrecendo a diversidade musical do ouvinte) e assimetria algorítmica em prol de faixas impulsionadas por grandes gravadoras em detrimento de artistas independentes.

#### 3. Filtro de Spam do Gmail / Google Workspace (Segurança e Triagem)
1. **Onde a IA está presente:** Na classificação e roteamento automatizado de mensagens (Principal, Promoções, Social, Spam) e nos motores heurísticos de detecção de campanhas de *phishing* e malwares baseados em Processamento de Linguagem Natural (PLN) e TensorFlow.
2. **Qual problema ela procura resolver:** Sobrecarga da caixa de entrada provocada por mensagens indesejadas em massa e proteção dos usuários contra fraudes cibernéticas, furto de credenciais e infecções por arquivos executáveis maliciosos.
3. **Quais dados provavelmente são utilizados:** Metadados e cabeçalhos de envio (autenticações SPF, DKIM, DMARC, endereço de IP de origem), análise textual sintática e semântica do corpo e linha de assunto do e-mail, reputação histórica do domínio remetente e ações em massa de outros usuários (marcação manual de spam).
4. **Qual é o benefício direto para o usuário:** Ambiente corporativo e pessoal de comunicação seguro, priorizado e limpo, blindando o usuário leigo contra ataques sofisticados de engenharia social.
5. **Existe algum risco ou limitação observável:** Ocorrência de falsos positivos (comunicações críticas, faturas e avisos institucionais retidos incorretamente na pasta de spam) e constante necessidade de re-treinamento perante e-mails de *phishing* gerados por criminosos com suporte de IA generativa.

#### 4. Reconhecimento Facial — Apple Face ID (Biometria e Visão Computacional)
1. **Onde a IA está presente:** No subsistema de segurança biométrica executado localmente na *Neural Engine* do processador, operando redes neurais convolucionais profundas treinadas para mapeamento e inferência facial biométrica.
2. **Qual problema ela procura resolver:** Eliminar a vulnerabilidade e o atrito ergonômico do uso exclusivo de senhas alfanuméricas, que podem ser esquecidas ou visualizadas por terceiros (*shoulder surfing*).
3. **Quais dados provavelmente são utilizados:** Nuvem de mais de 30.000 pontos infravermelhos estruturados projetados sobre o rosto do usuário gerando uma malha tridimensional de profundidade, imagens infravermelhas 2D de suporte e histórico progressivo de adaptações faciais morfológicas do usuário (barba, maquiagem, acessórios e envelhecimento biológico).
4. **Qual é o benefício direto para o usuário:** Autenticação e validação de pagamentos com altíssima taxa de segurança, quase instantânea e transparente para a rotina diária.
5. **Existe algum risco ou limitação observável:** Potencial disparidade histórica de acurácia se os dados de calibração não forem equânimes e diversos entre grupos étnicos e tonalidades de pele; além do risco legal decorrente da possibilidade de coação física para desbloqueio forçado do aparelho por agentes externos.

#### 5. ChatGPT / Google Gemini (Assistente de IA Generativa e LLM)
1. **Onde a IA está presente:** No núcleo arquitetural completo da solução, que consiste em Modelos de Linguagem de Grande Escala (LLMs) alicerçados na arquitetura *Transformer*, capacitados a contextualizar prompts complexos e gerar texto coerente, resumo documental e código-fonte.
2. **Qual problema ela procura resolver:** Mitigar a lentidão e o desgaste cognitivo na redação textual, prototipação rápida de códigos, estruturação de ideias, tradução e análise analítica de bases de conhecimento extensas.
3. **Quais dados provavelmente são utilizados:** Centenas de bilhões de tokens derivados de páginas web indexadas, livros digitalizados, manuais técnicos, repositórios de código aberto e corpora refinados por Aprendizado por Reforço com Feedback Humano (RLHF).
4. **Qual é o benefício direto para o usuário:** Aceleração exponencial da produtividade intelectual, permitindo obter sínteses e soluções de engenharia sob demanda em frações de segundo.
5. **Existe algum risco ou limitação observável:** **Alucinações** (produção de premissas factualmente falsas ou códigos com vulnerabilidades lógicas formuladas com tom de certeza categórica) e riscos de quebra de sigilo ou privacidade na submissão de dados corporativos confidenciais em instâncias públicas.

**Tabela Comparativa das Tecnologias Analisadas**

| Tecnologia | Tipo de IA | Entrada de Dados | Saída do Modelo | Limitação Central |
|---|---|---|---|---|
| Google Maps / Waze | Preditiva / Otimização | GPS, velocidade em tempo real, incidentes | Rota otimizada e previsão de tempo (ETA) | Efeito manada em bairros residenciais |
| Spotify | Preditiva / Recomendação | Histórico, taxa de pulo, áudio espectral | Playlists dinâmicas e rádio de faixas | Criação de "bolhas de filtro" sonoras |
| Gmail Spam Filter | Preditiva / Classificação | Cabeçalhos de e-mail, texto, links | Rótulo (Spam vs. Caixa de Entrada) | Falsos positivos de e-mails importantes |
| Apple Face ID | Preditiva / Visão Computacional | Malha de pontos 3D infravermelha | Decisão binária (Autorizado / Negado) | Dependência de diversidade na base de treino |
| ChatGPT / Gemini | Generativa / LLM | Prompts em linguagem natural | Textos, resumos e códigos inéditos | Alucinações apresentadas com convicção |

---

### Checkpoint de Compreensão

1. **Qual a diferença entre IA e Machine Learning?**
   - *Inteligência Artificial (IA):* É a grande área da computação dedicada ao estudo e desenvolvimento de sistemas capazes de reproduzir competências que convencionalmente exigiriam inteligência humana (interpretação da linguagem, reconhecimento de padrões complexos e raciocínio deliberativo).
   - *Machine Learning (ML):* É uma disciplina contida dentro da IA. O que a diferencia fundamentalmente é a mudança no paradigma de programação: enquanto a programação tradicional requer que o engenheiro humano codifique previamente todas as regras lógicas e condicionais (`if-else`), no Machine Learning os dados brutos e as respostas conhecidas são alimentados ao algoritmo para que ele próprio induza os padrões matemáticos e construa o modelo de forma autônoma.

2. **O que diferencia a IA Preditiva da Generativa?**
   - *IA Preditiva (Tradicional):* Tem como finalidade primordial **identificar padrões para classificar ou estimar** probabilidades sobre dados pré-existentes. O modelo avalia a entrada e infere uma probabilidade (ex.: diagnosticar se uma transação é fraudulenta ou prever a probabilidade de rotatividade de clientes).
   - *IA Generativa (Moderna):* Tem como objetivo **produzir conteúdos novos, funcionais e inéditos**. A partir de uma instrução (*prompt*), a rede neural constrói sequencialmente novos tokens (sejam palavras, códigos de computador, imagens sintéticas ou áudio), gerando uma solução original ajustada à demanda.

3. **O que caracteriza o Deep Learning?**
   - O Deep Learning (Aprendizado Profundo) é uma subcategoria do Machine Learning caracterizada pela utilização de **Redes Neurais Artificiais Profundas**, compostas por uma Camada de Entrada (*Input Layer*), múltiplas Camadas Ocultas profundas (*Hidden Layers*) e uma Camada de Saída (*Output Layer*).
   - Esse arranjo matemático profundo viabiliza a extração hierárquica automática de representações em dados não estruturados de alta complexidade (como áudio, imagens ou texto natural), eliminando a etapa clássica e restrita de engenharia manual de atributos (*feature engineering*).

4. **Qual a função dos dados no aprendizado de máquina?**
   - Os dados constituem o elemento basilar de instrução do algoritmo. É a partir do processamento estatístico de correlações e distribuições numéricas contidas nos dados que o modelo calibra seus parâmetros internos e matrizes de pesos sinápticos.
   - Por esse motivo, vigora o princípio fundamental **"Garbage In, Garbage Out" (GIGO)**: a qualidade do sistema treinado é diretamente ditada pela qualidade dos dados fornecidos. Bases com registros incompletos, incorretos, ruidosos ou enviesados resultarão inevitavelmente em predições inconsistentes, discriminação algorítmica e respostas alucinadas.

5. **Por que um prompt detalhado gera resultados melhores?**
   - Os modelos generativos (como os LLMs) comportam-se como motores probabilísticos guiados pelo contexto de entrada. Prompts vagos mantêm um espaço vetorial de busca extremamente amplo, levando o modelo a previsões genéricas, extensas demais ou desconectadas do objetivo pretendido.
   - Ao formular um prompt estruturado — explicitando **papel/persona, contexto, objetivo, restrições e formato desejado** —, o usuário condiciona matematicamente o modelo a estreitar seu espaço probabilístico, gerando saídas precisas, com tom adequado e pronta aderência à necessidade do usuário.

6. **Por que é necessário verificar as respostas de uma IA?**
   - Os modelos de linguagem operam prevendo estocasticamente a sequência mais verossímil da próxima palavra com base nos padrões estatísticos do seu treinamento; eles **não possuem consciência semântica intrínseca nem acessam um repositório de verdade absoluta**.
   - Devido a essa natureza probabilística, os modelos estão sujeitos ao fenômeno da **alucinação**, isto é, formulam assertivas factualmente incorretas, dados inventados ou citações fictícias exibindo extrema consistência gramatical e tom de convicção inquestionável. Por isso, a supervisão crítica humana (*human-in-the-loop*) é indispensável para validação e garantia de precisão.

## 8. Técnicas utilizadas

- [x] Role Prompting
- [x] Contexto
- [x] Restrições
- [x] Formato de saída
- [x] Prompt em etapas (Atividade Prática → Tabela → Checkpoint)
- [x] Refinamento iterativo
- [ ] Few-Shot Prompting
- [ ] Outra

## 9. Comparação

| Critério | Prompt A (inicial) | Prompt B (refinado) |
|---|---|---|
| Clareza | Baixa | Alta |
| Contexto | Ausente | Completo (disciplina, docente, conceitos da aula) |
| Relevância | Genérica | Específica para a formação em Ciência da Computação |
| Organização | Fraca | Estruturada (itens numerados + tabela comparativa) |
| Precisão | Baixa | Alta (fundamentação em Redes Profundas, GIGO e Transformers) |
| Utilidade | Limitada (inviável para entrega formal) | Pronta para submissão avaliativa |

**Qual prompt produziu o resultado mais adequado? Por quê?**
O Prompt B, pois forneceu o papel de autoridade científica, o contexto pedagógico da Aula 01 da Profa. Kadidja Valéria e delimitou critérios estritos de entrega técnica. Isso eliminou respostas telegráficas e garantiu que o resultado final refletisse conceitos essenciais de engenharia, como camadas ocultas de DL, princípio GIGO e a arquitetura probabilística de LLMs.

## 10. Teste de robustez

Para averiguar a sensibilidade do modelo a uma restrição de público, o estudante alterou o papel de "professor e pesquisador universitário" para "professor explicando para alunos do 5º ano do ensino fundamental", mantendo inalteradas as 5 tecnologias e as 6 questões conceituais.

- **O que mudou na resposta:** A IA substituiu termos técnicos como "redes neurais convolucionais", "extração de representações" e "predição estocástica de tokens" por metáforas do universo infantil, comparando o aprendizado de máquina a "aprender a andar de bicicleta caindo várias vezes", os dados a "ingredientes de bolo" e as camadas ocultas a "vários detetives em fila passando a lupa em cada pedaço do desenho".
- **Por que acreditamos que mudou:** A alteração deliberada da variável de público restringiu o espaço semântico e vocabular do LLM, provando que o modelo calibra ativamente seu nível de abstração com base direta nas restrições de papel e audiência fornecidas.
- **A alteração melhorou ou piorou o resultado?** Para um contexto de divulgação didática infantil, a resposta adaptou-se com sucesso; no entanto, para a avaliação acadêmica no ensino superior, a versão técnica formal é indispensável. O teste evidenciou a consistência e maleabilidade do controle por engenharia de prompt.

## 11. Validação

O discente validou o resultado obtido da seguinte forma:

- Conferiu minuciosamente as definições do Checkpoint de Compreensão em relação ao conteúdo do arquivo de aula (*Tendencias_Aula01_FundamentosIA_ModelosGenerativos.pdf*), certificando-se de que a representação dos diagramas de "Programação Tradicional vs. Machine Learning" e "Camadas Neurais" estivesse fidedigna às lâminas da Profa. Kadidja Valéria.
- Checou se as 5 perguntas obrigatórias do slide da Atividade Prática haviam sido respondidas de forma unívoca para cada uma das 5 aplicações selecionadas.
- Confirmou tecnicamente a coerência da descrição dos componentes de hardware biométrico do Face ID (projetor de pontos de infravermelho e rede neural local na *Neural Engine*).
- Assegurou que a explicação do fenômeno de alucinação refletisse a mecânica real dos modelos autorregressivos (previsão estocástica de tokens), evitando personificações ingênuas da IA.

## 12. Ética e responsabilidade

- **Viés algorítmico e amplificação de desigualdades:** Em virtude do princípio GIGO, dados de treinamento enviesados reproduzem e intensificam preconceitos históricos em algoritmos de recrutamento, policiamento preditivo e liberação de crédito. É dever ético fundamental do cientista da computação auditar a integridade e representatividade dos conjuntos de dados.
- **Privacidade e Proteção de Dados (LGPD):** Tecnologias como Google Maps e reconhecimento facial realizam coleta intensiva de geolocalização contínua e dados biométricos sensíveis, demandando estrita conformidade com a Lei Geral de Proteção de Dados (Lei nº 13.709/2018), com criptografia de ponta e princípios de minimização.
- **Responsabilidade pela alucinação:** Modelos generativos não devem ser utilizados de forma acrítica como instâncias autônomas de decisão em ambientes de alto impacto (saúde, sistema penal, infraestrutura crítica). A responsabilidade final e indelegável por todo conteúdo ou decisão recai sempre sobre o supervisor humano (*human-in-the-loop*).
- **Direitos de autor e consentimento na web:** A captura em larga escala de dados públicos na internet para treinamento de LLMs levanta debates éticos e regulatórios sobre o consentimento e a remuneração devida a desenvolvedores de software, autores e artistas criadores das obras originais.

## 13. Take Away

**O que mudou na nossa compreensão sobre IA depois de aprender a estruturar um prompt?**
Compreendemos que os modelos generativos não constituem entidades oraculares, mas sistemas probabilísticos altamente sensíveis ao contexto de entrada. Aprender a formular prompts estruturados (com persona, objetivos, restrições e formatação) transforma uma interação antes genérica e propensa a retrabalho em um instrumento potente de apoio intelectual e desenvolvimento de software.

**Qual é a principal responsabilidade de uma pessoa que utiliza IA generativa para produzir conhecimento ou tomar decisões?**
A principal responsabilidade é exercer julgamento crítico e ceticismo permanente, assumindo a validação rigorosa de cada dado, código ou argumento gerado antes de sua aplicação prática — reconhecendo que a máquina prevê probabilidades linguísticas, enquanto a ponderação ética, técnica e decisória pertence unicamente ao ser humano.

## 14. Declaração de uso de Inteligência Artificial

Em conformidade com as boas práticas de integridade científica e transparência acadêmica, o discente declara que utilizou a ferramenta de IA generativa **Google Gemini, modelo Gemini 2.5 Flash**, como recurso instrumental para a elaboração de prompts exploratórios, formatação e revisão conceitual das respostas das seções 3 a 7 deste documento. Todo o conteúdo gerado pela IA foi lido criticamente, conferido perante os slides oficiais da Aula 01 da disciplina e validado pelo discente Luan Bispo Silva, que assume plena responsabilidade pelo trabalho apresentado.

## 15. Referências

ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 6023**: informação e documentação — referências — elaboração. Rio de Janeiro: ABNT, 2018.

ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **NBR 14724**: informação e documentação — trabalhos acadêmicos — apresentação. Rio de Janeiro: ABNT, 2011.

BRASIL. **Lei nº 13.709, de 14 de agosto de 2018**. Lei Geral de Proteção de Dados Pessoais (LGPD). Brasília, DF: Presidência da República, 2018. Disponível em: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm. Acesso em: 12 set. 2026.

GOOGLE. **Gemini** (modelo Gemini 2.5 Flash). Mountain View: Google, 2026. Disponível em: https://gemini.google.com. Acesso em: 12 set. 2026.

RUSSELL, Stuart; NORVIG, Peter. **Inteligência Artificial: uma abordagem moderna**. 4. ed. Rio de Janeiro: GEN LTC, 2022.

VALÉRIA, Kadidja. **Tendências em Ciência da Computação — Aula 01: Fundamentos de IA e Modelos Generativos**. Brasília: Centro Universitário do Distrito Federal (UDF), 2026.
