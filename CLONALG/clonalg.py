import numpy as np
from numpy.random import uniform
from random import randint


b_lo, b_up = (-10, 10)

population_size = 100
selection_size = 10
problem_size = 2
random_cells_num = 20
clone_rate = 20
mutation_rate = 0.2
stop_codition = 100


def matyas_function(x):
    soma = 0.26 * ((x[0] ** 2) + (x[1] ** 2)) - .48 * x[0] * x[1]
    return soma


def create_random_cells(population_size, problem_size, b_lo, b_up):
    population = [uniform(low=b_lo, high=b_up, size=problem_size) for x in range(population_size)]

    return population


def clone(p_i, clone_rate):
    clone_num = int(clone_rate / p_i[1])
    clones = [(p_i[0], p_i[1]) for x in range(clone_num)]

    return clones


def hypermutate(p_i, mutation_rate, b_lo, b_up):

    if uniform() <= mutation_rate:
        ind_tmp = []
        for gen in p_i[0]:
            if uniform() <= mutation_rate:
                n = randint(0, 1)
                if n:
                    ind_tmp.append(gen - (p_i[1]/1000))
                else:
                    ind_tmp.append(gen + (p_i[1]/1000))
            else:
                ind_tmp.append(gen)

        return np.array(ind_tmp), matyas_function(ind_tmp)
    else:
        return p_i


def select(pop, pop_clones, pop_size):
    population = pop + pop_clones

    population = sorted(population, key=lambda x: x[1])[:pop_size]

    return population


def replace(population, population_rand, population_size):
    population = population + population_rand
    population = sorted(population, key=lambda x: x[1])[:population_size]

    return population


def clonalg():
    # Population <- CreateRandomCells(Population_size, Problem_size)
    population = create_random_cells(population_size, problem_size, b_lo, b_up)
    best_affinity_it = []
    for i in range(stop_codition):
        # Affinity(p_i)
        population_affinity = [(p_i, matyas_function(p_i)) for p_i in population]
        populatin_affinity = sorted(population_affinity, key=lambda x: x[1])

        best_affinity_it.append(populatin_affinity[:5])

        # Populatin_select <- Select(Population, Selection_size)
        population_select = populatin_affinity[:selection_size]

        # Population_clones <- clone(p_i, Clone_rate)
        population_clones = []
        for p_i in population_select:
            p_i_clones = clone(p_i, clone_rate)
            population_clones += p_i_clones

        # Hypermutate and affinity
        pop_clones_tmp = []
        for p_i in population_clones:
            ind_tmp = hypermutate(p_i, mutation_rate, b_lo, b_up)
            pop_clones_tmp.append(ind_tmp)
        population_clones = pop_clones_tmp
        del pop_clones_tmp

        population = select(populatin_affinity, population_clones, population_size)
        population_rand = create_random_cells(random_cells_num, problem_size, b_lo, b_up)
        population_rand_affinity = [(p_i, matyas_function(p_i)) for p_i in population_rand]
        population_rand_affinity = sorted(population_rand_affinity, key=lambda x: x[1])
        population = replace(population_affinity, population_rand_affinity, population_size)
        population = [p_i[0] for p_i in population]

    return best_affinity_it[stop_codition - 1][0][1]
