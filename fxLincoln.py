import random
import math

# -----------------------------
# Parâmetros Configuráveis
# -----------------------------

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

# -----------------------------
# Funções Auxiliares
# -----------------------------

def binary_to_real(binary_vector, lower, upper, bits):
    """Converte um vetor binário para um número real no intervalo [lower, upper]."""
    integer = int("".join(str(bit) for bit in binary_vector), 2)
    max_int = 2**bits - 1
    real = lower + (integer / max_int) * (upper - lower)
    return real

def initialize_population(size, bits):
    """Inicializa a população com indivíduos aleatórios."""
    population = []
    for _ in range(size):
        cromossomo = [random.randint(0, 1) for _ in range(bits)]
        population.append(cromossomo)
    return population

def evaluate_fitness(population):
    """Avalia a aptidão de cada indivíduo na população."""
    fitness = []
    for crom in population:
        x = binary_to_real(crom, LOWER_BOUND, UPPER_BOUND, BITS)
        fx = f(x)
        fitness_val = 1 / fx  # Fitness inversamente proporcional a f(x) para minimização
        fitness.append(fitness_val)
    return fitness

def tournament_selection(population, fitness, tournament_size):
    """Seleciona indivíduos usando seleção por torneio."""
    selected = []
    for _ in range(len(population)):
        participantes = random.sample(list(zip(population, fitness)), tournament_size)
        vencedor = max(participantes, key=lambda x: x[1])
        selected.append(vencedor[0])
    return selected

def roulette_wheel_selection(population, fitness):
    """Seleciona indivíduos usando seleção por roleta."""
    total_fitness = sum(fitness)
    if total_fitness == 0:
        # Evita divisão por zero
        return random.choices(population, k=len(population))
    selection_probs = [fit / total_fitness for fit in fitness]
    selected = random.choices(population, weights=selection_probs, k=len(population))
    return selected

def crossover(parent1, parent2, points):
    """Realiza o crossover entre dois pais com 1 ou 2 pontos de corte."""
    if points == 1:
        ponto = random.randint(1, len(parent1) - 1)
        filho1 = parent1[:ponto] + parent2[ponto:]
        filho2 = parent2[:ponto] + parent1[ponto:]
    elif points == 2:
        ponto1 = random.randint(1, len(parent1) - 2)
        ponto2 = random.randint(ponto1 + 1, len(parent1) - 1)
        filho1 = parent1[:ponto1] + parent2[ponto1:ponto2] + parent1[ponto2:]
        filho2 = parent2[:ponto1] + parent1[ponto1:ponto2] + parent2[ponto2:]
    else:
        raise ValueError("Número de pontos de crossover deve ser 1 ou 2.")
    return filho1, filho2

def mutate(individual, mutation_rate):
    """Aplica mutação em um indivíduo."""
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]  # Inverte o bit
    return individual

def elitism_selection(population, fitness, elite_size):
    """Seleciona os melhores indivíduos para elitismo."""
    sorted_population = sorted(zip(population, fitness), key=lambda x: x[1], reverse=True)
    elites = [ind for ind, fit in sorted_population[:elite_size]]
    return elites

# -----------------------------
# Algoritmo Genético Principal
# -----------------------------

def genetic_algorithm():
    # Inicialização
    population = initialize_population(POPULATION_SIZE, BITS)
    fitness = evaluate_fitness(population)
    
    # Determinar o número de elites
    elite_size = math.ceil((ELITE_PERCENTAGE / 100) * POPULATION_SIZE) if ELITISM else 0
    
    for generation in range(1, MAX_GENERATIONS + 1):
        # Avaliação de aptidão
        fitness = evaluate_fitness(population)
        
        # Encontrar o melhor indivíduo da geração atual
        best_fitness = max(fitness)
        best_index = fitness.index(best_fitness)
        best_individual = population[best_index]
        best_x = binary_to_real(best_individual, LOWER_BOUND, UPPER_BOUND, BITS)
        best_fx = f(best_x)
        
        print(f"Geração {generation}: Melhor f(x) = {best_fx:.4f} para x = {best_x:.4f}")
        
        # Seleção
        if SELECTION_METHOD == 'tournament':
            selected = tournament_selection(population, fitness, TOURNAMENT_SIZE)
        elif SELECTION_METHOD == 'roulette':
            selected = roulette_wheel_selection(population, fitness)
        else:
            raise ValueError("Método de seleção inválido. Use 'tournament' ou 'roulette'.")
        
        # Crossover
        offspring = []
        for i in range(0, POPULATION_SIZE, 2):
            parent1 = selected[i]
            parent2 = selected[i+1] if i+1 < POPULATION_SIZE else selected[0]
            filhos = crossover(parent1, parent2, CROSSOVER_POINTS)
            offspring.extend(filhos)
        
        # Mutação
        offspring = [mutate(ind, MUTATION_RATE) for ind in offspring]
        
        # Elitismo
        if ELITISM:
            elites = elitism_selection(population, fitness, elite_size)
            offspring[:elite_size] = elites  # Substitui os primeiros 'elite_size' indivíduos pelos elites
        
        # Atualizar população
        population = offspring[:POPULATION_SIZE]
    
    # Avaliação final
    fitness = evaluate_fitness(population)
    best_fitness = max(fitness)
    best_index = fitness.index(best_fitness)
    best_individual = population[best_index]
    best_x = binary_to_real(best_individual, LOWER_BOUND, UPPER_BOUND, BITS)
    best_fx = f(best_x)
    
    print("\n--- Resultado Final ---")
    print(f"Melhor f(x) = {best_fx:.4f} para x = {best_x:.4f}")
    print(f"Cromossomo Binário: {''.join(str(bit) for bit in best_individual)}")

# -----------------------------
# Executar o Algoritmo
# -----------------------------

if __name__ == "__main__":
    genetic_algorithm()
