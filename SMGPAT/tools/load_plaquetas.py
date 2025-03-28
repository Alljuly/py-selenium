import pandas as pd

def load_plaquetas(csv_path: str):
    df = pd.read_csv(csv_path, usecols=['numero_plaqueta'])
    plaqueta_init_value = df['numero_plaqueta'].iloc[0]
    plaqueta_final_value = df['numero_plaqueta'].iloc[1] 

    return plaqueta_init_value, plaqueta_final_value