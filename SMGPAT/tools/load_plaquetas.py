import pandas as pd

def load_plaquetas(csv_path: str):
    df = pd.read_csv(csv_path, usecols=['plaqueta_inicial', 'plaqueta_final'])
    plaqueta_init_value = df['plaqueta_inicial'].iloc[0]
    plaqueta_final_value = df['plaqueta_final'].iloc[0] 

    return plaqueta_init_value, plaqueta_final_value