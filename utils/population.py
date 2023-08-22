#! /usr/bin/env python3
"""Population utilities."""

import numpy as np

from utils.casting import int_to_bin_array


def init_binary_population(n: int = 10, genes: int = 10):
    min = 0
    max = 2**genes
    population = np.random.randint(min, max, n)
    population = [int_to_bin_array(individue, genes) for individue in population]
    population = np.array(population, dtype=int)
    
    return population
