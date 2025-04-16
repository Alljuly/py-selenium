import pandas as pd

def load_plaquetas(data_json):
    df = pd.DataFrame(data_json)
    
    return df