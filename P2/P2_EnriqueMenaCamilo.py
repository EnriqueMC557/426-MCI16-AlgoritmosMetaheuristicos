import sys

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


distances = DistanceHelper(offline_mode=True)

genes = 18
generations = range(50)

# Roulette + PMx
population = init_nobinary_population(n=100, genes=18)
avg_aptitudes_ = []
min_aptitudes_ = []
evolution_ = []

for _ in tqdm(generations, desc="Generation"):
    population, aptitudes, avg_aptitude, min_aptitude = evaluate_tsp_population(population, distances, cities_mapper)
    avg_aptitudes_.append(avg_aptitude)
    min_aptitudes_.append(min_aptitude)
    evolution_.append(population.copy())

    parents = roulette_selection(aptitudes)
    childrens = partially_mapped_crossover(population, parents)
    breakpoint()
    # childrens = insert_mutation(childrens)
    # population = genetic_competence(population, childrens)


# Roulette + Cx
population = init_nobinary_population(n=100, genes=18)
avg_aptitudes_ = []
min_aptitudes_ = []
evolution_ = []

for _ in tqdm(generations, desc="Generation"):
    population, aptitudes, avg_aptitude, min_aptitude = evaluate_tsp_population(population, distances, cities_mapper)
    avg_aptitudes_.append(avg_aptitude)
    min_aptitudes_.append(min_aptitude)
    evolution_.append(population.copy())

    parents = roulette_selection(aptitudes)
    childrens = cycle_crossover(population, parents)
    # childrens = inverse_mutation(childrens)
    # population = genetic_competence(population, childrens)


# Tournament + PMx
population = init_nobinary_population(n=100, genes=18)
avg_aptitudes_ = []
min_aptitudes_ = []
evolution_ = []

for _ in tqdm(generations, desc="Generation"):
    population, _, avg_aptitude, min_aptitude = evaluate_tsp_population(population, distances, cities_mapper)
    avg_aptitudes_.append(avg_aptitude)
    min_aptitudes_.append(min_aptitude)
    evolution_.append(population.copy())

    parents = tournament_selection(population)
    childrens = partially_mapped_crossover(population, parents)
    # childrens = insert_mutation(childrens)
    # population = genetic_competence(population, childrens)


# Tournament + Cx
population = init_nobinary_population(n=100, genes=18)
avg_aptitudes_ = []
min_aptitudes_ = []
evolution_ = []

for _ in tqdm(generations, desc="Generation"):
    population, _, avg_aptitude, min_aptitude = evaluate_tsp_population(population, distances, cities_mapper)
    avg_aptitudes_.append(avg_aptitude)
    min_aptitudes_.append(min_aptitude)
    evolution_.append(population.copy())

    parents = tournament_selection(population)
    childrens = cycle_crossover(population, parents)
    # childrens = inverse_mutation(childrens)
    # population = genetic_competence(population, childrens)
