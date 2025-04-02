"""
import pandas as pd

data_fake = {
    'numero_plaqueta': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'organograma_name': ['A', 'A', 'C', 'B', 'C', 'B', 'C', 'D', 'D', 'A'],
    'status': ['ativo', 'baixado', 'ativo', 'ativo', 'baixado', 'ativo', 'ativo', 'baixado', 'ativo', 'ativo']
}

df = pd.DataFrame(data_fake)
"""

def get_active_items(list_items_df):
    list_items_df = list_items_df[list_items_df['status'] != 'Baixado']
    list_sorted = list_items_df.sort_values(by='organograma_name')
    list_items = list_sorted[['numero_plaqueta','organograma_name']].to_dict(orient='records')
    return list_items

def order_items(data):
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
