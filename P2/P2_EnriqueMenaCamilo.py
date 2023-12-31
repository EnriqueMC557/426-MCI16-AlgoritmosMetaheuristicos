import sys

import numpy as np

from tqdm import tqdm

sys.path.append("..")

from cities import cities_mapper
from distance_helper import DistanceHelper
from utils.population import init_nobinary_population
from utils.aptitude import evaluate_tsp_population
from utils.selection import roulette_selection, tournament_selection
from utils.crossover import partially_mapped_crossover, cycle_crossover
from utils.mutation import insert_mutation, inverse_mutation
from utils.visualization import plot_aptitude


def genetic_competence(population: np.ndarray, childrens: np.ndarray):
    all_population = np.vstack([population, childrens])
    sorted_population, _, _, _ = evaluate_tsp_population(all_population, distances, cities_mapper)
    return sorted_population[:population.shape[0]]


distances = DistanceHelper(offline_mode=True)

genes = 18
generations = 50
max_stagnant_generations = 10
delta = 100

# Roulette + PMx
population = init_nobinary_population(n=100, genes=18)
avg_aptitudes_ = []
min_aptitudes_ = []
evolution_ = []
last_best_aptitude = float("inf")
stagnant_generations = 0

for _ in tqdm(range(generations), desc="Generation"):
    population, aptitudes, avg_aptitude, min_aptitude = evaluate_tsp_population(population, distances, cities_mapper)
    avg_aptitudes_.append(avg_aptitude)
    min_aptitudes_.append(min_aptitude)

    if abs(min_aptitude - last_best_aptitude) < delta:
        stagnant_generations += 1
        if stagnant_generations > max_stagnant_generations:
            break
    else:
        stagnant_generations = 0

    last_best_aptitude = min_aptitude
    parents = roulette_selection(aptitudes)
    childrens = partially_mapped_crossover(population, parents)
    childrens = insert_mutation(childrens)
    population = genetic_competence(population, childrens)

print(f"Best aptitude: {min_aptitudes_[-1]}")
print(f"Avg aptitude: {avg_aptitudes_[-1]}")

title = "Roulette selection + PMx"
plot_aptitude(avg_aptitudes_, min_aptitudes_, generations, title)


# Roulette + Cx
population = init_nobinary_population(n=250, genes=18)
avg_aptitudes_ = []
min_aptitudes_ = []
evolution_ = []
last_best_aptitude = float("inf")
stagnant_generations = 0

for _ in tqdm(range(generations), desc="Generation"):
    population, aptitudes, avg_aptitude, min_aptitude = evaluate_tsp_population(population, distances, cities_mapper)
    avg_aptitudes_.append(avg_aptitude)
    min_aptitudes_.append(min_aptitude)
    evolution_.append(population.copy())

    if abs(min_aptitude - last_best_aptitude) < delta:
        stagnant_generations += 1
        if stagnant_generations > max_stagnant_generations:
            break
    else:
        stagnant_generations = 0

    parents = roulette_selection(aptitudes)
    childrens = cycle_crossover(population, parents)
    childrens = inverse_mutation(childrens)
    population = genetic_competence(population, childrens)

print(f"Best aptitude: {min_aptitudes_[-1]}")
print(f"Avg aptitude: {avg_aptitudes_[-1]}")

title = "Roulette selection + Cx"
plot_aptitude(avg_aptitudes_, min_aptitudes_, generations, title)


# Tournament + PMx
population = init_nobinary_population(n=500, genes=18)
avg_aptitudes_ = []
min_aptitudes_ = []
evolution_ = []
last_best_aptitude = float("inf")
stagnant_generations = 0

for _ in tqdm(range(generations), desc="Generation"):
    population, _, avg_aptitude, min_aptitude = evaluate_tsp_population(population, distances, cities_mapper)
    avg_aptitudes_.append(avg_aptitude)
    min_aptitudes_.append(min_aptitude)
    evolution_.append(population.copy())

    if abs(min_aptitude - last_best_aptitude) < delta:
        stagnant_generations += 1
        if stagnant_generations > max_stagnant_generations:
            break
    else:
        stagnant_generations = 0

    parents = tournament_selection(population)
    childrens = partially_mapped_crossover(population, parents)
    childrens = insert_mutation(childrens)
    population = genetic_competence(population, childrens)

print(f"Best aptitude: {min_aptitudes_[-1]}")
print(f"Avg aptitude: {avg_aptitudes_[-1]}")

title = "Tournament selection + Cx"
plot_aptitude(avg_aptitudes_, min_aptitudes_, generations, title)


# Tournament + Cx
population = init_nobinary_population(n=1000, genes=18)
avg_aptitudes_ = []
min_aptitudes_ = []
evolution_ = []
last_best_aptitude = float("inf")
stagnant_generations = 0

for _ in tqdm(range(generations), desc="Generation"):
    population, _, avg_aptitude, min_aptitude = evaluate_tsp_population(population, distances, cities_mapper)
    avg_aptitudes_.append(avg_aptitude)
    min_aptitudes_.append(min_aptitude)
    evolution_.append(population.copy())

    if abs(min_aptitude - last_best_aptitude) < delta:
        stagnant_generations += 1
        if stagnant_generations > max_stagnant_generations:
            break
    else:
        stagnant_generations = 0

    parents = tournament_selection(population)
    childrens = cycle_crossover(population, parents)
    childrens = inverse_mutation(childrens)
    population = genetic_competence(population, childrens)

print(f"Best aptitude: {min_aptitudes_[-1]}")
print(f"Avg aptitude: {avg_aptitudes_[-1]}")

title = "Tournament selection + Cx"
plot_aptitude(avg_aptitudes_, min_aptitudes_, generations, title)
