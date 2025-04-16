import pandas as pd
from backend.tools import load_plaquetas

def get_active_items(list_items_df):
    list_items_df = list_items_df[list_items_df['status'] != 'Baixado']
    list_sorted = list_items_df.sort_values(by='organograma_name')
    list_items = list_sorted[['patplaqueta','organograma_name']].to_dict(orient='records')
    return list_items

def order_items(data):
    if data is None:
        return 
    
    if not isinstance(data, pd.DataFrame):
        data = load_plaquetas(data)

    list_items = get_active_items(data)
    list_transferences = []
        
    current_group = []
    current_organograma = None
    
    for item in list_items:
        if current_organograma is None or item['organograma_name'] == current_organograma:
            current_group.append(item)
        else:
            list_transferences.append(current_group)
            current_group = [item]
        
        current_organograma = item['organograma_name']
    
    if current_group:
        list_transferences.append(current_group)
    
    return list_transferences
