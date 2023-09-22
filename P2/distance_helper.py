import requests
import pandas as pd
from geopy.distance import geodesic

import cities


class DistanceHelper:
    def __init__(self, offline_mode: bool = False, on_demad_measure: bool = True):
        if offline_mode:
            self.distances = pd.read_csv("./data/predefined_distances.csv")
            self.distances = self.distances.set_index("X")
            self.cities = self.distances.columns.to_list()

        else:
            self.cities = cities.cities_list
            self.distances = pd.DataFrame(index=self.cities, columns=self.cities)

            if on_demad_measure is False:
                for city1 in self.cities:
                    for city2 in self.cities:
                        self.distances.loc[city1][city2] = self.measure_distance(city1, city2)

    def get_coordinates(self, city: str):
        base_url = 'https://nominatim.openstreetmap.org/search'
        params = {'q': city, 'format': 'json'}
        response = requests.get(base_url, params=params).json()
        location = response[0]

        return float(location['lat']), float(location['lon'])

    def measure_distance(self, city1: str, city2: str):
        if city1 == city2:
            return 0

        coordinates1 = self.get_coordinates(city1),
        coordinates2 = self.get_coordinates(city2)

        return geodesic(coordinates1, coordinates2).kilometers
    
    def get_distance(self, city1: str, city2: str):
        distance = self.distances.loc[city1][city2]

        if pd.isnull(distance):
            distance = self.measure_distance(city1, city2)
            self.distances.loc[city1][city2] = distance

        return distance
    

if __name__ == "__main__":
    distances = DistanceHelper()
    