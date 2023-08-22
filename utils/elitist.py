#! /usr/bin/env python3
"""Elitist utilities."""

import numpy as np

from utils.aptitude import evaluate_population


def genetic_competence(population: np.ndarray, childrens: np.ndarray):
    all_population = np.vstack([population, childrens])
    sorted_population, _, _, _ = evaluate_population(all_population, (-1, 1), lambda x: x**2)
    return sorted_population[:population.shape[0]]
