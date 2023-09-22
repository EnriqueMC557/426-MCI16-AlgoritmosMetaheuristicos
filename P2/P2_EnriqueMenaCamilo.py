import sys

from tqdm import tqdm

sys.path.append("..")

from cities import cities_mapper
from distance_helper import DistanceHelper
from utils.population import init_nobinary_population
from utils.aptitude import evaluate_tsp_population
from utils.selection import roulette_selection, tournament_selection
from utils.crossover import partially_mapped_crossover, cycle_crossover
from utils.visualization import plot_aptitude, plot_evolution
from utils.mutation import insert_mutation, scramble_mutation


distances = DistanceHelper(offline_mode=True)

genes = 18
initial_population = init_nobinary_population(n=100, genes=18)
generations = range(100)

population = initial_population.copy()
avg_aptitudes_ = []
min_aptitudes_ = []
evolution_ = []

for _ in tqdm(generations, desc="Generations"):
    population, _, avg_aptitude, min_aptitude = evaluate_tsp_population(population, distances, cities_mapper)
    avg_aptitudes_.append(avg_aptitude)
    min_aptitudes_.append(min_aptitude)
    evolution_.append(population.copy())

breakpoint()
