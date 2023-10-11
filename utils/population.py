#! /usr/bin/env python3
"""Population utilities."""
import sys
sys.path.append("..")


import numpy as np

from utils.casting import int_to_bin_array, int_to_oct_array, int_to_hex_array


def init_binary_population(n: int = 10, genes: int = 10):
    min = 0
    max = 2**genes
    population = np.random.randint(min, max, n)
    population = [int_to_bin_array(individue, genes) for individue in population]
    population = np.array(population)
    
    return population


def init_octal_population(n: int = 10, genes: int = 10):
    min_octal = 0o0
    max_octal = 0o7 * (8**genes) 
    population = np.random.randint(min_octal, max_octal, n, dtype=np.uint64)
    population = [int_to_oct_array(individue, genes) for individue in population]
    population = np.array(population)

    return population


def init_hexadecimal_population(n: int = 10, genes: int = 10):
    min_hex = 0x0
    max_hex = 0xF * (16**genes)
    population = np.random.randint(min_hex, max_hex, n, dtype=np.uint64)
    population = [int_to_hex_array(individue, genes) for individue in population]
    population = np.array(population)

    return population


def init_nobinary_population(n: int, genes: int = 10):
    available_genes = np.arange(1, genes+1)
    population = [np.random.choice(available_genes, (1, genes), replace=False)[0]
                  for _ in range(n)]
    
    return np.vstack(population)
