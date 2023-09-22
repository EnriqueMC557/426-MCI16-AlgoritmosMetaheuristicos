import pandas as pd

predefined_data = "./predefined_distances.xlsx"
data = pd.read_excel(predefined_data)

columns_mapper = {
    "Mexico_City": "Mexico City",
    "San_Salvador": "San Salvador",
    "New_York": "New York",
    "Panama_City": "Panama City",
}

data = data.rename(columns=columns_mapper)
data = data.replace(columns_mapper)
data = data.set_index("X")

data.to_csv("./predefined_distances.csv")
