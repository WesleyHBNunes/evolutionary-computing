import random
import numpy as np

from deap import base
from deap import creator
from deap import tools

D = 2  # NRO DIMENSOES
TAM_POP = 30  # tamanho da populacao
GEN = 100  # numero de geracoes

LIM_INF = -5.12  # limites iniciais pontos
LIM_SUP = 5.12  # limites iniciais pontos


def matyas_function(x):
    return 0.26 * ((x[0] ** 2) + (x[1] ** 2)) - .48 * x[0] * x[1],


def atualizarHof(hof, pop):
    # atualiza listagem de melhores individuos
    hof.update(pop)


def prepararStats():
    # ferramenta para calculo de estatisticas
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)
    return stats


def prepararLogBook(stats):
    # ferramenta para log da saida
    logbook = tools.Logbook()
    logbook.header = ["gen"] + stats.fields
    return logbook


def mostrarLog(stats, logbook, pop, g):
    # mostrar estatisticas atuais
    record = stats.compile(pop)
    logbook.record(gen=g, **record)
    print(logbook.stream)


def calcularFitness(toolbox, pop):
    # calcula fitness de uma populacao
    fitnesses = toolbox.map(toolbox.evaluate, pop)
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit


def atualizarProfessor(ind, prof, media, TF):
    for i in range(D):
        ind[i] += random.uniform(0, 1) * (prof[i] - (TF * media[i]))
    ind.fitness.values = toolbox.evaluate(ind)
    return ind


def atualizarAluno(ind, passo):
    for i in range(D):
        ind[i] += random.uniform(0, 1) * passo[i]
    ind.fitness.values = toolbox.evaluate(ind)
    return ind


def getPos(i, n):
    p = random.randint(0, n)
    while p != i:
        p = random.randint(0, n)
    return p


creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, LIM_INF, LIM_SUP)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, D)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("evaluate", matyas_function)


def tlbo():
    stats = prepararStats()
    logbook = prepararLogBook(stats)

    # gerar populacao inicial
    pop = toolbox.population(n=TAM_POP)

    # ferramenta para selecao do professor
    hof = tools.HallOfFame(1)

    # avalia todos os individuos
    calcularFitness(toolbox, pop)

    atualizarHof(hof, pop)

    for g in range(1, GEN + 1):

        atualizarHof(hof, pop)

        # fase professor

        # seleciona professor
        prof = hof[0]

        # calcula media
        med = np.mean(pop, axis=0)

        # print("G: {0}, Fit_Prof: {1}, Fit_Med: {2}".format(g, prof.fitness.values, avaliaT3(med), ))

        for i in range(TAM_POP):
            # fator aprendizagem
            TF = random.choice([1, 2])

            new_ind = toolbox.clone(pop[i])

            new_ind = atualizarProfessor(new_ind, prof, med, TF)

            if pop[i].fitness.values > new_ind.fitness.values:
                pop[i] = new_ind

        # fase learning
        for i in range(TAM_POP):
            k = getPos(i, TAM_POP)

            if pop[i].fitness.values < pop[k].fitness.values:
                passo = np.subtract(pop[k], pop[i])
            else:
                passo = np.subtract(pop[i], pop[k])

            new_ind = toolbox.clone(pop[i])
            new_ind = atualizarAluno(new_ind, passo)
            # print(pop[i].fitness.values)
            # print(new_ind.fitness.values)
            if pop[i].fitness.values > new_ind.fitness.values:
                pop[i] = new_ind

    return hof[0].fitness.values[0]
