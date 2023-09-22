#! /usr/bin/env python3
"""Selection utilities."""

import numpy as np


def polygamous_random_selection(population: np.ndarray):
    n_couples = population.shape[0]//2
    couples = np.random.choice(population.shape[0], (n_couples, 2), replace=True)

    return couples


def monogamous_random_selection(population: np.ndarray):
    n_couples = population.shape[0]//2
    couples = np.random.choice(population.shape[0], (n_couples, 2), replace=False)

    return np.array(couples)


def roulette_selection(population: np.ndarray):
    pass


def tournament_selection(population: np.ndarray):
    pass
