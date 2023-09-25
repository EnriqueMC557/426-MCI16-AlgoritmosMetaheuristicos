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

    return couples


def roulette_selection(aptitudes: np.ndarray):
    total_aptitude = aptitudes.sum()

    couples = []
    couple = []

    for _ in range(aptitudes.shape[0]):
        accumulated = 0
        selection = np.random.uniform(0, total_aptitude)

        for idx, aptitude  in enumerate(aptitudes):
            accumulated += aptitude
            if accumulated >= selection:
                couple.append(idx)
                break
        
        if len(couple) == 2:
            couples.append(couple)
            couple = []

    return np.vstack(couples)


def tournament_selection(population: np.ndarray):
    population_len = population.shape[0]

    couples = []
    for idx in range(population_len//2):
        couples.append([idx, population_len-idx-1])

    return np.vstack(couples)
