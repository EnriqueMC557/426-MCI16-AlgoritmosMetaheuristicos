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


def int_to_oct_array(number: int, padding: int = 8):
    oct_str = oct(number)[2:].zfill(padding)
    oct_array = np.zeros(padding)
    for idx in range(padding):
        oct_array[idx] = oct_str[idx]

    return oct_array


def oct_array_to_int(oct_array: np.ndarray):
    n = oct_array.shape[0]
    pows = [8**pow for pow in range(n)]
    pows = np.array(pows[::-1])
    int_number = np.dot(oct_array, pows)

    return int_number


def int_to_hex_array(number: int, padding: int = 8):
    hex_str = hex(number)[2:].zfill(padding)
    hex_array = np.zeros(padding, dtype=str)
    for idx in range(padding):
        hex_array[idx] = hex_str[idx].upper()

    return hex_array


def hex_array_to_int(hex_array: np.ndarray):
    pass
