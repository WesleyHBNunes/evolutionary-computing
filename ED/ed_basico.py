import random
import array

import numpy

from deap import base
from deap import creator
from deap import tools

# Problem dimension
NDIM = 2

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessMin)


def matyas_function(x):
    return 0.26 * ((x[0] ** 2) + (x[1] ** 2)) - .48 * x[0] * x[1],


toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, -10, 10)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, NDIM)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("select", tools.selRandom, k=3)
toolbox.register("evaluate", matyas_function)


def ed_basico():
    CR = 0.25
    F = 1
    MU = 300
    NGEN = 200

    pop = toolbox.population(n=MU);
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)

    logbook = tools.Logbook()
    logbook.header = "gen", "evals", "std", "min", "avg", "max"

    # Evaluate the individuals
    fitnesses = toolbox.map(toolbox.evaluate, pop)
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    record = stats.compile(pop)
    logbook.record(gen=0, evals=len(pop), **record)

    for g in range(1, NGEN):
        for k, agent in enumerate(pop):
            a, b, c = toolbox.select(pop)
            y = toolbox.clone(agent)
            index = random.randrange(NDIM)
            for i, value in enumerate(agent):
                if i == index or random.random() < CR:
                    y[i] = a[i] + F * (b[i] - c[i])
            y.fitness.values = toolbox.evaluate(y)
            if y.fitness > agent.fitness:
                pop[k] = y
        hof.update(pop)
        record = stats.compile(pop)
        logbook.record(gen=g, evals=len(pop), **record)

    return hof[0].fitness.values[0]
