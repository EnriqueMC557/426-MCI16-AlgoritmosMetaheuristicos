#! /usr/bin/env python3
"""Mutation utilities."""

import numpy as np


def insert_mutation(individues: np.ndarray, mr: float = 0.02):
    total_individues = individues.shape[0]
    to_mutate = np.random.choice(total_individues, int(total_individues*mr), replace=False)
    
    individue_len = individues.shape[1]
    segment_len = individue_len//5
    segments = [[idx, idx+segment_len] for idx in range(0, individue_len, segment_len)]

    for idx in to_mutate:
        segment1, segment2 = np.random.choice(len(segments), 2, replace=False)
        segment1, segment2 = segments[segment1], segments[segment2]
        org_individue = individues[idx].copy()
        individues[idx][segment1[0]:segment1[1]] = org_individue[segment2[0]:segment2[1]]
        individues[idx][segment2[0]:segment2[1]] = org_individue[segment1[0]:segment1[1]]

    return individues


def inverse_mutation(individues: np.ndarray, mr: float = 0.02):
    total_individues = individues.shape[0]
    individue_len = individues.shape[1]
    to_mutate = np.random.choice(total_individues, int(total_individues*mr))

    for idx in to_mutate:
        idx_l, idx_r = sorted(np.random.choice(individue_len, 2))
        idx_r = idx_r if idx_r == 17 else idx_r + 1
        individues[idx][idx_l:idx_r] = individues[idx][idx_l:idx_r][::-1]

    return individues


def scramble_mutation(individues: np.ndarray, mr: float = 0.02):
    pass
