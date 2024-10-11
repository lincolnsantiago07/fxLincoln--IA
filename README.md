# Algoritmo Genético para Minimização de Função em Python

## 📌 Índice

- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Como Executar](#como-executar)
- [Configurações](#configurações)
- [Exemplo de Saída](#exemplo-de-saída)
- [Considerações Finais](#considerações-finais)

---

## 📝 Descrição

Este projeto implementa um **Algoritmo Genético** (AG) em Python para encontrar o valor de \( x \) que minimiza a função matemática:

\[ f(x) = x^3 - 6x + 14 \]

O AG explora técnicas de evolução natural, como seleção, cruzamento (crossover) e mutação, para evoluir uma população de soluções em busca do mínimo global da função dentro do intervalo \([-10, +10]\).

---

## 🚀 Funcionalidades

- **Codificação Binária**: Representa o valor de \( x \) como um vetor binário, permitindo a exploração eficiente do espaço de soluções.
- **População Inicial Configurável**: Define o número de indivíduos na população inicial.
- **Taxa de Mutação Ajustável**: Controla a probabilidade de alteração de bits nos cromossomos.
- **Crossover de 1 ou 2 Pontos**: Escolha entre diferentes métodos de cruzamento para gerar novos indivíduos.
- **Métodos de Seleção Flexíveis**: Utiliza seleção por torneio ou roleta viciada para selecionar indivíduos para reprodução.
- **Elitismo Opcional**: Preserva os melhores indivíduos de cada geração para assegurar a qualidade das soluções.
- **Critério de Parada Configurável**: Define o número máximo de gerações para a execução do algoritmo.
- **Saída Informativa**: Exibe o progresso do algoritmo a cada geração e o resultado final com a melhor solução encontrada.

---

## 📋 Requisitos

- **Python 3.6** ou superior
- Nenhuma biblioteca externa é necessária; utiliza apenas módulos padrão do Python (`random`, `math`).

---

## 🔧 Instalação

1. **Clone o Repositório** (se aplicável) ou **baixe o script** diretamente.

   ```bash
   git clone https://github.com/lincolnsantiago07/fxLincoln--IA.git


▶️ Como Executar
Certifique-se de ter o Python Instalado

Verifique a versão do Python instalada:

python --version
Deve retornar algo como Python 3.8.5.

Execute o Script

No terminal ou prompt de comando, execute:

bash
Copiar código
python genetic_algorithm_minimize.py
Substitua genetic_algorithm_minimize.py pelo nome do arquivo onde o código foi salvo.

Acompanhe a Saída

O algoritmo exibirá o progresso a cada geração, mostrando o melhor valor de 
𝑓(𝑥)f(x) e o correspondente valor de 𝑥x. Após atingir o número máximo de gerações, apresentará o resultado final.

## ⚙️ Configurações

As principais configurações do algoritmo estão definidas no início do script. Você pode ajustar os parâmetros conforme necessário.

python
# Função a ser minimizada
def f(x):
    return x**3 - 6*x + 14

# Intervalo de x
LOWER_BOUND = -10
UPPER_BOUND = 10

# Configurações do Algoritmo Genético
BITS = 16  # Número de bits para codificação de x

POPULATION_SIZE = 10  # Número de indivíduos na população

MUTATION_RATE = 0.01  # Taxa de mutação (1%)

CROSSOVER_POINTS = 1  # 1 ou 2 pontos de corte

SELECTION_METHOD = 'tournament'  # 'tournament' ou 'roulette'

TOURNAMENT_SIZE = 3  # Tamanho do torneio (usado na seleção por torneio)

ELITISM = True  # Usar elitismo

ELITE_PERCENTAGE = 10  # Percentual de elitismo (usado se ELITISM=True)

MAX_GENERATIONS = 100  # Número máximo de gerações

Descrição dos Parâmetros

BITS: Define a precisão da representação de 𝑥x. Mais bits aumentam a precisão.

POPULATION_SIZE: Número de indivíduos na população inicial.

MUTATION_RATE: Probabilidade de cada bit ser mutado (invertido) durante a mutação.

CROSSOVER_POINTS: Número de pontos de corte utilizados no crossover (1 ou 2).

SELECTION_METHOD: Método de seleção de indivíduos para reprodução. Pode ser 'tournament' ou 'roulette'.

TOURNAMENT_SIZE: Número de indivíduos competindo em cada torneio (aplicável se SELECTION_METHOD for 'tournament').

ELITISM: Ativa ou desativa o elitismo. Se ativado, preserva os melhores indivíduos de cada geração.

ELITE_PERCENTAGE: Percentual da população que será preservado como elites (aplicável se ELITISM for True).

MAX_GENERATIONS: Número máximo de gerações que o algoritmo executará antes de parar.

Para ajustar qualquer configuração, simplesmente modifique os valores correspondentes no início do script antes de executar.

## 📈 Exemplo de Saída
Ao executar o algoritmo, você verá uma saída semelhante a esta no terminal:

Geração 1: Melhor f(x) = 3.8455 para x = 1.7500

Geração 2: Melhor f(x) = 2.5000 para x = -1.2000

Geração 100: Melhor f(x) = 2.6870 para x = -1.4142

### --- Resultado Final ---

Melhor f(x) = 2.6870 para x = -1.4142
Cromossomo Binário: 0110110010100110
Interpretação:

Geração X: Indica a geração atual do algoritmo.

Melhor f(x): O menor valor de  𝑓(𝑥)f(x) encontrado até aquela geração.

x: O valor de 𝑥x correspondente ao melhor 𝑓(𝑥)f(x).

Cromossomo Binário: A representação binária do valor de 𝑥x.

Nota: Os valores exatos podem variar a cada execução devido à natureza aleatória dos algoritmos genéticos.

## 🧠 Considerações Finais
Diversidade Genética: A taxa de mutação de 1% ajuda a manter a diversidade na população, prevenindo a convergência prematura para soluções subótimas.
Elitismo: Preservar uma porcentagem da população como elites garante que as melhores soluções sejam mantidas ao longo das gerações.
Ajuste de Parâmetros: Experimentar diferentes configurações (como tamanho da população, taxa de mutação, número de gerações) pode levar a melhores resultados ou acelerar a convergência.
Precisão vs. Desempenho: Mais bits na codificação aumentam a precisão, mas também aumentam o tempo de processamento.
