#! /usr/bin/env python3
"""Casting utilities."""

import numpy as np


def int_to_bin_array(number: int, padding: int = 8):
    bin_str = np.binary_repr(number).zfill(padding)
    bin_array = np.zeros(padding)
    for idx in range(padding):
        bin_array[idx] = bin_str[idx]

    return bin_array


def bin_array_to_int(bin_array: np.ndarray):
    n = bin_array.shape[0]
    pows = [2**pow for pow in range(n)]
    pows = np.array(pows[::-1])
    int_number = np.dot(bin_array, pows)

    return int_number
