#! /usr/bin/env python3
"""cities."""

cities_list = [
    "Mexico City",
    "Quito",
    "Miami",
    "San Salvador",
    "Mendoza",
    "Guadalajara",
    "Merida",
    "Washington",
    "Monterrey",
    "Managua",
    "Caracas",
    "Boston",
    "Buenos Aires",
    "New York",
    "Panama City",
    "Brasilia",
    "Montevideo",
    "Bogotá",
]

cities_mapper = {idx+1: city for idx, city in enumerate(cities_list)}
