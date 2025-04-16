from backend.tools import generate_query_json, load_plaquetas


from .query_item_by_ID import query_random_item


def query_list_items_service(navigator, plaquetas_data):
    plaquetas_df = load_plaquetas(plaquetas_data)
    plaquetas_sorted = plaquetas_df.sort_values(by="patplaqueta") 
    print('sorted plaquetas', plaquetas_sorted)
    plaquetas = plaquetas_sorted["patplaqueta"].astype(str).tolist()
    print('plaquetas', plaquetas)

    items = []

    for plaqueta in plaquetas:
        item_description = query_random_item(navigator, plaqueta)
        print(f'item description: {item_description}')
        if item_description:
            items.append(item_description)
    
    result_json = []
    if items:
        result_json = generate_query_json(navigator, items=items)
        
    return result_json
