def flatten_dict(nested_dict, parent_key=''):
    flat_dict = {}
    
    for key, value in nested_dict.items():
        new_key = f"{parent_key}_{key}" if parent_key else key
        
        if isinstance(value, dict):
            flat_dict.update(flatten_dict(value, new_key))
        else:
            flat_dict[new_key] = value
    
    return flat_dict
