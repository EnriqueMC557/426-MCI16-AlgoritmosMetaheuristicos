import numpy as np
import pandas as pd

predefined_data = "./predefined_distances.xlsx"
data = pd.read_excel(predefined_data)

# data = data.set_index("KM")
# data = data.replace({"ND": np.nan})

# data.to_csv("./predefined_distances.csv")

data = data.rename(columns={"KM": "City"})

data.to_csv("./predefined_distances_2.csv", index=False)
