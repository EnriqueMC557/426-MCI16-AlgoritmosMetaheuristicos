#! /usr/bin/env python3
"""Crossover utilities."""

import numpy as np


def one_point_crossover(population: np.ndarray, parents: np.ndarray):
    childrens = np.empty_like(population)
    for idx, couple in enumerate(parents):
        crossover_point = population.shape[1]//2
        childrens[idx*2, :crossover_point] = population[couple[0], :crossover_point]
        childrens[idx*2, crossover_point:] = population[couple[1], crossover_point:]
        childrens[idx*2+1, :crossover_point] = population[couple[1], :crossover_point]
        childrens[idx*2+1, crossover_point:] = population[couple[0], crossover_point:]

    return childrens


def two_point_crossover(population: np.ndarray, parents: np.ndarray):
    childrens = np.empty_like(population)
    for idx, couple in enumerate(parents):
        crossover_point = population.shape[1]//3
        childrens[idx*2, :crossover_point] = population[couple[0], :crossover_point]
        childrens[idx*2, crossover_point:2*crossover_point] = population[couple[1], crossover_point:2*crossover_point]
        childrens[idx*2, 2*crossover_point:] = population[couple[0], 2*crossover_point:]
        childrens[idx*2+1, :crossover_point] = population[couple[1], :crossover_point]
        childrens[idx*2+1, crossover_point:2*crossover_point] = population[couple[0], crossover_point:2*crossover_point]
        childrens[idx*2+1, 2*crossover_point:] = population[couple[1], 2*crossover_point:]

    return childrens


def partially_mapped_crossover(popoulation: np.ndarray, parents: np.ndarray):
    def map_value(value, mapping):
        while value in mapping:
            value = mapping[value]
        return value
    
    childrens = np.empty_like(popoulation)
    size = len(popoulation[0])
    middle_ = size//2
    crop_len = size//6
    point1, point2 = middle_-crop_len, middle_+crop_len

    for idx, couple in enumerate(parents):     
        childrens[idx*2,   point1:point2+1] = popoulation[couple[0], point1:point2+1]
        childrens[idx*2+1, point1:point2+1] = popoulation[couple[1], point1:point2+1]

        parent1_mapping = dict(zip(popoulation[couple[0], point1:point2+1], popoulation[couple[1], point1:point2+1]))
        parent2_mapping = dict(zip(popoulation[couple[1], point1:point2+1], popoulation[couple[0], point1:point2+1]))

        for i in range(size):
            if i < point1 or i > point2:
                childrens[idx*2  ][i] = map_value(popoulation[couple[1]][i], parent1_mapping)
                childrens[idx*2+1][i] = map_value(popoulation[couple[0]][i], parent2_mapping)

    return childrens


def cycle_crossover(population: np.ndarray, parents: np.ndarray):
    childrens = np.empty_like(population)
    for idx, couple in enumerate(parents):
        parent1, parent2 = population[couple[0]], population[couple[1]]
        child1, child2 = np.empty_like(parent1), np.empty_like(parent2)
        visited = np.zeros_like(parent1, dtype=bool)
        cycle_start = 0
        while not visited[cycle_start]:
            visited[cycle_start] = True
            child1[cycle_start] = parent1[cycle_start]
            child2[cycle_start] = parent2[cycle_start]
            cycle_start = np.where(parent1 == parent2[cycle_start])[0][0]
        for i in range(len(parent1)):
            if not visited[i]:
                child1[i] = parent2[i]
                child2[i] = parent1[i]
        childrens[idx*2] = child1
        childrens[idx*2+1] = child2
    return childrens


if __name__ == "__main__":
    p1 = np.array([15, 10, 4, 18, 5, 3, 13, 7, 1, 11, 14, 8, 9, 16, 17, 2, 12, 6])
    p2 = np.array([4, 6, 7, 5, 17, 10, 8, 1, 16, 12, 13, 3, 2, 11, 15, 14, 9, 18])
    population = np.vstack([p1, p2])
    parents = np.array([[0, 1]])
    childrens = partially_mapped_crossover(population, parents)

    p1 = np.array([15, 10, 4, 18, 5, 3, 13, 7, 1, 11, 14, 8, 9, 16, 17, 2, 12, 6])
    p2 = np.array([4, 6, 7, 5, 17, 10, 8, 15, 16, 12, 13, 3, 2, 11, 1, 14, 9, 18])
    population = np.vstack([p1, p2])
    parents = np.array([[0, 1]])
    childrens = cycle_crossover(population, parents)
    