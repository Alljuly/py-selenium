import pandas as pd

def load_plaquetas(csv_path: str):
    df = pd.read_csv(csv_path, usecols=['numero_plaqueta'])

    return df